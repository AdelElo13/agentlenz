# Weekly Health Report — 2026-10-26

Generated: 2026-10-26 | Repos: `adelelo13/agentlenz`, `adelelo13/dockwright-macos-agent`

---

## adelelo13/agentlenz — ⚠️ Warning

### Stale Branches

13 branches total (main + 12 non-main). No change from last week.

**`claude/temp-meters-dab-pots-lcvi3w`** — merged into `main`, branch still not deleted. Flagged for **6+ weeks** (since ~2026-09-14). Action needed: delete it.

**11 standup branches with open PRs** — same count as last week (PR #9 was closed/merged at some point):

| Branch | PR | Age (days) |
|--------|-----|-----------|
| standup-2026-05-27 | #1 | 152 |
| standup-2026-06-16 | #2 | 132 |
| standup-2026-06-17 | #3 | 131 |
| standup-2026-06-22 | #4 | 126 |
| standup-2026-06-29 | #5 | 119 |
| standup-2026-07-13 | #6 | 105 |
| standup-2026-08-24 | #7 | 63 |
| standup-2026-08-31 | #8 | 56 |
| standup-2026-09-15 | #10 | 41 |
| standup-2026-10-05 | #11 | 21 |
| standup-2026-10-13 | #12 | 13 |

**Note:** This week's standups (2026-10-20 through 2026-10-26) are committed directly to `main` — no new branches/PRs opened. The backlog count holds at 11 open standup PRs; oldest is now 152 days.

### Dependency Health

| File | Status |
|------|--------|
| `backend/pyproject.toml` | `fastapi>=0.115`, `uvicorn>=0.32`, `sqlalchemy>=2.0`, `pydantic>=2.0` — version ranges, no conflicts |
| `sdk/pyproject.toml` | `httpx>=0.27`, `pydantic>=2.0`, `anthropic>=0.40`, `openai>=1.50` — version ranges satisfied |
| `dashboard/package.json` | `next@16.2.1`, `react@19.2.4`, `@tanstack/react-query@^5.95.1`, `recharts@^3.8.0` |

No lock files committed — builds are not fully reproducible. Consider committing `package-lock.json` (dashboard) and pinned requirements (backend/sdk).

### Code Quality

- **TODO/FIXME/HACK comments:** 0 across all `.py`, `.ts`, `.js` files — clean
- **Uncommitted changes:** None
- **Stashes:** None

### Test Status

- **SDK tests:** ✅ 25 passed, 1 skipped (0.05s)
- **Backend tests:** Not run (requires Postgres/asyncpg; skipped in this environment)
- **Dashboard tests:** No test script configured

### Git Hygiene

- No large files (all files <1MB, outside `node_modules`)
- No stashes

---

## adelelo13/dockwright-macos-agent — ⚠️ Warning

### Stale Branches

2 branches: `main`, `fix/bug-audit-v1`.

**`fix/bug-audit-v1`** has an open PR (#1) — **"fix: resolve 37 audited bugs + 2 hardening items across Dockwright"** — open since **2026-07-11 (107 days)**. This is a significant pending bug-fix PR that has not been merged. Needs review and a merge decision.

### Dependency Health

No `Package.swift` or other package manifests — project uses only Apple system frameworks. No dependency tracking needed.

**Large binary files in repo:**

| File | Size |
|------|------|
| `assets/demo.mov` | 1.5 MB |
| `Dockwright/Resources/Models/embedding_model.onnx` | 1.3 MB |
| `Dockwright/Resources/Models/hey_jarvis_v0.1.onnx` | 1.3 MB |
| `Dockwright/Resources/Models/melspectrogram.onnx` | 1.1 MB |

These are expected (wake-word models + demo video). No action needed, but consider Git LFS if the repo grows.

### Code Quality

- **TODO/FIXME/HACK comments:** 0 across all `.swift` files — clean
- **Swift source files:** 104 files (active, well-structured codebase)
- **Recent activity:** 4 commits this week — active development (UIAutomation improvements, bug fixes)

### Test Status

- **No Swift tests found** — no `*Tests*.swift` files or `Tests/` directory. The project has no automated test suite. Consider adding unit tests for core logic (LLMService, CronEngine, ToolExecutor).

### Git Hygiene

- **Uncommitted changes:** None
- **Stashes:** None

---

## Summary

| Repo | Health | Key Issue |
|------|--------|-----------|
| `agentlenz` | ⚠️ Warning | 11 stale standup PRs (oldest 152 days) + 1 merged branch not deleted |
| `dockwright-macos-agent` | ⚠️ Warning | PR #1 open 107 days (37 bug fixes unmerged), no test suite |

### Action Items

1. **agentlenz:** Delete `claude/temp-meters-dab-pots-lcvi3w` — been flagged 6 weeks.
2. **agentlenz:** Decide on standup PR strategy — bulk-close or bulk-merge the 11 open PRs; oldest is now 5 months stale.
3. **dockwright-macos-agent:** Review and merge or close PR #1 (`fix/bug-audit-v1`) — open 107 days with 37 bug fixes.
4. **dockwright-macos-agent:** Add a basic Swift test target.
