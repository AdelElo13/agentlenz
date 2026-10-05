# Weekly Health Report — 2026-10-05

Generated: 2026-10-05 | Repos: `adelelo13/agentlenz`, `adelelo13/dockwright-macos-agent`

---

## adelelo13/agentlenz — ⚠️ Warning

### Stale Branches

11 non-main branches, 10 with open PRs, none merged.

**`claude/temp-meters-dab-pots-lcvi3w`** — merged into `main`, branch still not deleted. Flagged since 2026-09-14 (4+ weeks).

**10 standup branches with open PRs** (one new this week: #11):

| Branch | PR | Days Open |
|--------|----|-----------|
| standup-2026-05-27 | #1 | 131 days |
| standup-2026-06-16 | #2 | 111 days |
| standup-2026-06-17 | #3 | 110 days |
| standup-2026-06-22 | #4 | 105 days |
| standup-2026-06-29 | #5 | 98 days |
| standup-2026-07-13 | #6 | 84 days |
| standup-2026-08-24 | #7 | 42 days |
| standup-2026-08-31 | #8 | 35 days |
| standup-2026-09-15 | #10 | 20 days |
| standup-2026-10-05 | #11 | 0 days (today) |

**Pattern:** Standup branches and their PRs accumulate weekly, never closed. 10 open PRs serve no review purpose. Recommend closing all standup PRs and deleting their branches, or switch to committing standup docs directly to main.

### Dependency Health

**backend (`pyproject.toml`)** — min-version pins, no pinned exact versions:
- `fastapi>=0.115`, `uvicorn[standard]>=0.32`, `sqlalchemy[asyncio]>=2.0`, `asyncpg>=0.30`, `alembic>=1.14`, `pydantic>=2.0`, `psycopg2-binary>=2.9`
- Status: No lockfile in repo. Cannot verify installed vs. latest without running pip. Deps look current as of spec (FastAPI 0.115, SQLAlchemy 2.x are recent stable releases).

**sdk (`pyproject.toml`)** — minimal deps:
- `httpx>=0.27`, `pydantic>=2.0`; optional: `anthropic>=0.40`, `openai>=1.50`
- Status: Healthy. Lightweight and up-to-date spec.

**dashboard (`package.json`)** — Next.js app:
- `next: 16.2.1`, `react: 19.2.4`, `react-dom: 19.2.4`
- `@tanstack/react-query: ^5.95.1`, `recharts: ^3.8.0`
- Status: Healthy. Next.js 16 and React 19 are current.

### Code Quality

- Python files: **0 TODOs / FIXMEs / HACKs** across 46 files ✓
- TypeScript/JS files: **0 TODOs / FIXMEs / HACKs** across 8 files ✓

### Test Status

Test suites present in both `backend/tests/` and `sdk/tests/`:
- **backend tests:** `test_budgets.py`, `test_costs.py`, `test_ingest.py`, `test_pricing.py`, `test_recommender.py`, `test_waste_detector.py`
- **sdk tests:** `test_budget.py`, `test_client.py`, `test_config.py`, `test_integration.py`, `test_spans.py`, `test_trace.py`, `test_wrapper_anthropic.py`, `test_wrapper_openai.py`
- Status: Tests exist and are well-structured. (Not executed — no Python env available in this remote session.)

### Git Hygiene

- Working tree: clean ✓
- Uncommitted changes: none ✓
- Stashes: none ✓
- Large files: none detected ✓
- HEAD state: detached (ephemeral clone, expected)

---

## adelelo13/dockwright-macos-agent — ⚠️ Warning

### Stale Branches

1 non-main branch: **`fix/bug-audit-v1`**

| Branch | PR | Days Open | Description |
|--------|----|-----------|-------------|
| fix/bug-audit-v1 | #1 | **86 days** | "fix: resolve 37 audited bugs + 2 hardening items across Dockwright" |

**This is a concern.** PR #1 has been open since 2026-07-11 with a substantial fix scope (37 bugs). It has not been merged into `main` for 86 days. The branch and main have since diverged — main has 4+ subsequent commits. Either this work should be merged, rebased onto main, or closed if the fixes were applied separately.

### Dependency Health

- No `Package.swift` or SPM packages — project uses only Apple system frameworks (Swift, SwiftUI, AVFoundation, Speech, Vision, etc.)
- Status: **Healthy** — no third-party dependency exposure.
- Bundled ML model assets: `embedding_model.onnx`, `melspectrogram.onnx`, `hey_jarvis_v0.1.onnx` (wake word models, committed to repo)

### Code Quality

- Swift files: **104 files, 0 TODOs / FIXMEs / HACKs** ✓
- Coverage spans: App, Core (LLM, Tools, Scheduler, Memory, Channels, Voice, Sensory, Skills, Agent, Goals, Heartbeat), UI, Utilities

### Test Status

- No test suite found (no `XCTest` targets, no `Tests/` directory)
- Status: **No automated tests.** A macOS app of this complexity benefits from at minimum unit tests for the LLM pipeline, tool executor, and cron engine.

### Git Hygiene

- Working tree: clean ✓
- Uncommitted changes: none ✓
- Stashes: none ✓
- Large binary files committed to repo:
  - `assets/demo.mov` (video — should be in Git LFS or external storage)
  - `Dockwright/Resources/Models/embedding_model.onnx` (~large, ML model)
  - `Dockwright/Resources/Models/melspectrogram.onnx` (~large, ML model)
  - `Dockwright/Resources/Models/hey_jarvis_v0.1.onnx` (~large, ML model)
  - These inflate clone size for all contributors. Consider Git LFS.

---

## Summary

| Repo | Score | Top Issue |
|------|-------|-----------|
| agentlenz | ⚠️ Warning | 10 stale standup PRs accumulating weekly; merged branch not deleted |
| dockwright-macos-agent | ⚠️ Warning | PR #1 (37-bug fix) open 86 days, unmerged; no tests; large binaries in repo |

### Recommended Actions

1. **agentlenz:** Close all standup PRs (#1–#10) and delete their branches — they are reference docs, not code changes needing review. Delete the merged `claude/temp-meters-dab-pots-lcvi3w` branch.
2. **dockwright-macos-agent:** Decide fate of PR #1 — merge, close, or rebase onto current `main`. Add at least basic unit tests for core logic. Move large binaries to Git LFS.
