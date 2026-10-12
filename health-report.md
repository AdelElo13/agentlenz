# Weekly Health Report — 2026-10-12

Generated: 2026-10-12 | Repos: `adelelo13/agentlenz`, `adelelo13/dockwright-macos-agent`

---

## adelelo13/agentlenz — ⚠️ Warning

### Stale Branches

12 branches total (main + 11 non-main). No branches merged into main and undeleted since last week.

**`claude/temp-meters-dab-pots-lcvi3w`** — merged into `main`, branch still not deleted. Flagged for 4+ weeks (since ~2026-09-14). Action needed: delete it.

**10 standup branches with open PRs** — none have been merged or closed:

| Branch | PR | Age (days) |
|--------|-----|-----------|
| standup-2026-05-27 | #1 | 138 |
| standup-2026-06-16 | #2 | 119 |
| standup-2026-06-17 | #3 | 118 |
| standup-2026-06-22 | #4 | 113 |
| standup-2026-06-29 | #5 | 106 |
| standup-2026-07-13 | #6 | 92 |
| standup-2026-08-24 | #7 | 49 |
| standup-2026-08-31 | #8 | 42 |
| standup-2026-09-15 | #10 | 27 |
| standup-2026-10-05 | #11 | 7 |

**1 new standup branch this week:** `standup-2026-10-05` / PR #11 (opened 2026-10-05).

### Dependency Health

| File | Status |
|------|--------|
| `backend/pyproject.toml` | Version ranges (fastapi>=0.115, uvicorn>=0.32, sqlalchemy>=2.0, etc.) — no lock file in repo; no pinned conflicts detected |
| `sdk/pyproject.toml` | Version ranges (httpx>=0.27, pydantic>=2.0, anthropic>=0.40, openai>=1.50) — clean |
| `dashboard/package.json` | next@16.2.1, react@19.2.4, @tanstack/react-query@^5.95.1, recharts@^3.8.0 — looks current |

No obviously outdated pinned versions detected. No lock files committed (consider adding for reproducible builds).

### Code Quality

- **TODO/FIXME/HACK comments:** 0 in Python, 0 in TypeScript/JS — clean
- **Uncommitted changes:** None
- **Stashes:** None
- **Large files (>1MB):** None

### Test Status

| Suite | Result |
|-------|--------|
| `sdk/tests/` (25 tests) | ✅ 25 passed, 1 skipped |
| `backend/tests/` (17 tests) | ✅ 17 passed |

Note: Minor atexit warning in SDK test teardown (`RuntimeError: Call agentlenz.init() before using AgentLenz`) — benign, does not affect test outcomes.

### Git Hygiene

- Commits last 7 days: 4
- Commits last 30 days: 16
- Active development confirmed

### Summary

Good test coverage and clean code. The persistent backlog of 10 open standup PRs (oldest 138 days) remains the main hygiene concern. The `claude/temp-meters-dab-pots-lcvi3w` branch needs deletion — it has been merged for over a month.

---

## adelelo13/dockwright-macos-agent — ⚠️ Warning

### Stale Branches

2 branches: `main` and `fix/bug-audit-v1`.

**`fix/bug-audit-v1`** — open PR #1 ("fix: resolve 37 audited bugs + 2 hardening items across Dockwright"), opened **93 days ago** (2026-07-11). Not merged, not closed. This PR has been open since July and represents substantial work that hasn't landed.

No merged-but-undeleted branches.

### Dependency Health

No SPM packages declared — project uses Apple frameworks only (as per architecture spec). No external dependency risk.

4 binary assets in `Dockwright/Resources/Models/`:
- `embedding_model.onnx` (1.3 MB)
- `hey_jarvis_v0.1.onnx` (1.3 MB)
- `melspectrogram.onnx` (1.1 MB)
- `assets/demo.mov` (1.5 MB)

These are intentional bundled assets, not a concern. Total repo size: 8.4 MB.

### Code Quality

- **TODO/FIXME/HACK comments:** 0 in 104 Swift source files — clean
- **Deployment target:** macOS 14.0 ✅ (correct per spec)
- **Uncommitted changes:** None
- **Stashes:** None

### Test Status

No automated test suite (Xcode unit tests not present or not runnable in CI environment). Build verification requires macOS + Xcode — not available in this environment.

### Git Hygiene

- Commits last 7 days: **0**
- Commits last 30 days: **0**
- Last commit: `d6d3f3f chore: update UIAutomationTool` (over 30 days ago)
- **Development appears stalled**

### Open PR

**PR #1: "fix: resolve 37 audited bugs + 2 hardening items across Dockwright"** — 93 days open, targeting `main`. Needs a decision: merge, close, or rebase and update.

### Summary

No code quality issues, clean dependency profile. Two concerns: (1) development activity has stopped entirely for 30+ days, and (2) PR #1 with 37 bug fixes has been sitting unmerged for 93 days. If active development is resuming, merging or closing this PR should be the first step.

---

## Cross-Repo Summary

| Repo | Health | Tests | TODOs | Open PRs | Commits (7d) |
|------|--------|-------|-------|----------|--------------|
| agentlenz | ⚠️ Warning | ✅ 42/43 pass | 0 | 10 open (oldest 138d) | 4 |
| dockwright-macos-agent | ⚠️ Warning | N/A | 0 | 1 open (93d) | 0 |

**Key actions:**
1. **agentlenz**: Delete `claude/temp-meters-dab-pots-lcvi3w` branch. Consider closing or merging the backlog of standup PRs.
2. **dockwright-macos-agent**: Decide fate of PR #1 (93 days open). Resume development or archive.
