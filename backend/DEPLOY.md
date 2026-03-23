# Deploying AgentFinOps API to Fly.io

## Prerequisites

- [flyctl](https://fly.io/docs/hands-on/install-flyctl/) installed
- A Fly.io account

```bash
# Install flyctl (macOS)
brew install flyctl

# Log in
fly auth login
```

---

## First-time deployment

### 1. Create the Fly app

```bash
fly apps create agentfinops-api
```

> Change `agentfinops-api` to a globally unique name if that one is taken.
> Update `app = "..."` in `fly.toml` to match.

### 2. Create the Postgres cluster

```bash
fly postgres create --name agentfinops-db --region ams
```

Save the credentials printed at the end — they are shown only once.

### 3. Attach Postgres to the app

```bash
fly postgres attach agentfinops-db --app agentfinops-api
```

This automatically sets the `DATABASE_URL` secret on your app.

### 4. Set any additional secrets

```bash
# Example: a JWT secret, external API keys, etc.
fly secrets set SECRET_KEY=your-value-here --app agentfinops-api
```

### 5. Deploy

```bash
fly deploy
```

Fly will build the Docker image, run `alembic upgrade head` (inside the CMD),
and start the app. The public URL is printed at the end of the deploy.

---

## Subsequent deployments

```bash
fly deploy
```

That's it. Fly re-builds and does a rolling restart with zero downtime.

---

## Creating the first API key

After the database is up and running, use the helper script:

```bash
# Requires DATABASE_URL pointing at the Fly Postgres instance.
# Easiest way: open a proxy in another terminal:
#   fly proxy 5432 -a agentfinops-db
# Then in this terminal:
export DATABASE_URL="postgresql://postgres:<password>@localhost:5432/agentfinops_api"

python scripts/create_api_key.py "My Project"
```

The script will print the API key **once** — copy it immediately.
The key itself is never stored; only its SHA-256 hash lives in the database.

### Running the script via Fly SSH (no local proxy needed)

```bash
fly ssh console --app agentfinops-api
# Inside the container:
python scripts/create_api_key.py "My Project"
```

---

## Useful commands

| Task | Command |
|---|---|
| View logs | `fly logs --app agentfinops-api` |
| Open a shell | `fly ssh console --app agentfinops-api` |
| Connect to Postgres | `fly postgres connect -a agentfinops-db` |
| Scale down to zero | `fly scale count 0 --app agentfinops-api` |
| Check app status | `fly status --app agentfinops-api` |
