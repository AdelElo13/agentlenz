# AgentLenz — Everything You Need To Know

## What You Have

### 1. The Product (code)
Everything lives at `~/agentlens/` and on GitHub: https://github.com/AdelElo13/agentlenz

Three packages:
- **sdk/** — Python SDK that customers install (`pip install agentlenz`)
- **backend/** — FastAPI server that receives data from the SDK
- **dashboard/** — Next.js web dashboard where customers see their costs

### 2. The Website
- **Live at:** https://agentlenz.dev
- **Files at:** `~/agentlens/website/`
- **Admin panel:** https://agentlenz.dev/admin.php (password: AgentLenz2026!)
- **Signup form:** working, stores emails, sends you notifications

### 3. The Email
- **Address:** hello@agentlenz.dev
- **Password:** AgentLenz2026Mail!
- **Webmail:** https://s246.webhostingserver.nl:2223 → login → Email → Webmail
- **IMAP setup (for Apple Mail/Gmail):**
  - Server: s246.webhostingserver.nl
  - Port: 993 (SSL)
  - Username: hello@agentlenz.dev
  - Password: AgentLenz2026Mail!

### 4. The Outreach Kit
All at `~/agentlens/docs/cab-outreach/`:
- `dm-templates.md` — 5 cold DM templates
- `call-script.md` — 15-min CAB call script
- `loi-template.md` — Letter of Interest for CAB members
- `x-search-queries.md` — 24 Twitter search queries to find prospects

---

## The Plan (What To Do & When)

### RIGHT NOW — Weeks 1-4: Find Your First 10 Customers

You are NOT selling yet. You're finding 10 people who feel the pain of AI agent costs and asking them for advice.

**Daily routine:**
1. Open X/Twitter
2. Search: `"openai bill" OR "anthropic bill" -is:retweet lang:en`
3. Find people complaining about AI costs → DM them
4. Target: 50 DMs per day (weeks 1-2), then 15/day

**The DM (keep it short):**
> Hey — saw your post about AI costs. I'm building a tool that cuts agent costs 40-60% by detecting waste and routing to cheaper models. Would love to hear how you manage AI spend today. Quick 15-min chat?

**When they say yes:**
1. Get on a 15-min call (use the script in docs/cab-outreach/call-script.md)
2. Ask about their problems — genuinely listen
3. At the end, invite them to the Customer Advisory Board
4. Send them the LOI (docs/cab-outreach/loi-template.md)
5. They get 70% lifetime discount in exchange for feedback

**Goal: 10 signed LOIs**

### Weeks 5-12: Deploy The Product For Your 10 Customers

Once you have 10 CAB members, deploy the backend so they can actually use it.

**Deploy to Fly.io (see backend/DEPLOY.md for full steps):**
```bash
# Install Fly CLI
brew install flyctl

# Login
fly auth login

# Create app + database
fly apps create agentlenz-api
fly postgres create --name agentlenz-db --region ams
fly postgres attach agentlenz-db

# Deploy
cd ~/agentlens/backend
fly deploy

# Create API keys for your CAB members
fly ssh console
python3 scripts/create_api_key.py "Company Name"
# Save the key it prints — send it to the customer
```

**Tell each CAB member:**
```
pip install agentlenz
```

Then in their code:
```python
import agentlenz
agentlenz.init(api_key="alz_their_key_here")
client = agentlenz.wrap(their_existing_client)
# That's it — costs are now tracked
```

**Dashboard** — deploy separately or just run locally for now:
```bash
cd ~/agentlens/dashboard
npm run dev
# Opens at http://localhost:3000
```

### Months 3-6: Launch Publicly

- Open-source the SDK on GitHub (it's already there)
- Launch on Product Hunt, Hacker News (Show HN), Reddit
- Write a blog post: "How we cut our AI agent bill by 52%"
- Add TypeScript SDK support

### Months 6-12: Scale

- Hit $80K+ MRR
- Hire first 1-2 people when revenue > $20K MRR
- Add MCP cost gateway
- Enterprise features

---

## How To Run Things Locally

### Run the backend locally:
```bash
cd ~/agentlens/backend
source .venv/bin/activate

# Need a local Postgres database:
# brew install postgresql@16 && brew services start postgresql@16
# createdb agentlenz

# Run migrations
alembic upgrade head

# Start server
uvicorn agentlenz_api.main:app --reload --port 8000
```

### Run the dashboard locally:
```bash
cd ~/agentlens/dashboard
echo "NEXT_PUBLIC_AGENTLENZ_API_URL=http://localhost:8000" > .env.local
echo "NEXT_PUBLIC_AGENTLENZ_API_KEY=alz_your_key" >> .env.local
npm run dev
```

### Run SDK tests:
```bash
cd ~/agentlens/sdk
source .venv/bin/activate
pytest tests/ -v --ignore=tests/test_integration.py
```

### Run backend tests:
```bash
cd ~/agentlens/backend
source .venv/bin/activate
pytest tests/ -v
```

---

## Important Files & Passwords

| What | Where |
|------|-------|
| Code | ~/agentlens/ and github.com/AdelElo13/agentlenz |
| Website files | ~/agentlens/website/ |
| Design spec | ~/agentlens/docs/superpowers/specs/2026-03-23-agentlens-design.md |
| Implementation plan | ~/agentlens/docs/superpowers/plans/2026-03-23-agentlens-implementation.md |
| Outreach kit | ~/agentlens/docs/cab-outreach/ |
| Admin panel | agentlenz.dev/admin.php — password: AgentLenz2026! |
| Email | hello@agentlenz.dev — password: AgentLenz2026Mail! |
| Hosting panel | s246.webhostingserver.nl:2223 — deb95449n500 / fYtoq1taxcQsAZ41 |
