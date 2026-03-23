#!/usr/bin/env python3
"""
Create a project and its first API key.

Usage:
    python scripts/create_api_key.py <project-name>

Environment:
    DATABASE_URL  — PostgreSQL connection string
                    e.g. postgresql://user:pass@host:5432/dbname

The generated API key is printed ONCE and never stored in plain text.
Only the SHA-256 hash is kept in the database.
"""

import hashlib
import os
import secrets
import sys
import uuid


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python scripts/create_api_key.py <project-name>", file=sys.stderr)
        sys.exit(1)

    project_name = sys.argv[1].strip()
    if not project_name:
        print("Error: project name cannot be empty.", file=sys.stderr)
        sys.exit(1)

    database_url = os.environ.get("DATABASE_URL")
    if not database_url:
        print("Error: DATABASE_URL environment variable is not set.", file=sys.stderr)
        sys.exit(1)

    # asyncpg uses postgresql+asyncpg:// — psycopg2 needs plain postgresql://
    sync_url = database_url.replace("postgresql+asyncpg://", "postgresql://")

    # Generate key:  af_ + 32 random hex chars  (e.g. af_a3f9...)
    raw_token = secrets.token_hex(16)          # 32 hex chars
    api_key = f"af_{raw_token}"
    key_prefix = api_key[:10]                  # "af_" + first 7 chars
    key_hash = hashlib.sha256(api_key.encode()).hexdigest()

    project_id = uuid.uuid4()
    api_key_id = uuid.uuid4()

    try:
        import psycopg2  # type: ignore[import-untyped]
    except ImportError:
        print(
            "Error: psycopg2 is not installed. Run: pip install psycopg2-binary",
            file=sys.stderr,
        )
        sys.exit(1)

    try:
        conn = psycopg2.connect(sync_url)
        conn.autocommit = False
        cur = conn.cursor()

        cur.execute(
            """
            INSERT INTO projects (id, name)
            VALUES (%s, %s)
            """,
            (str(project_id), project_name),
        )

        cur.execute(
            """
            INSERT INTO api_keys (id, key_hash, key_prefix, project_id, is_active)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (str(api_key_id), key_hash, key_prefix, str(project_id), True),
        )

        conn.commit()
        cur.close()
        conn.close()
    except Exception as exc:
        print(f"Database error: {exc}", file=sys.stderr)
        sys.exit(1)

    print()
    print(f"  Project : {project_name}")
    print(f"  ID      : {project_id}")
    print()
    print(f"  API Key : {api_key}")
    print()
    print("  Save this key now — it will NOT be shown again.")
    print()


if __name__ == "__main__":
    main()
