# Weekly Health Report — 2026-10-19

Generated: 2026-10-19 | Repos: `adelelo13/agentlenz`, `adelelo13/dockwright-macos-agent`

---

## adelelo13/agentlenz — ⚠️ Warning

### Stale Branches

13 branches total (main + 12 non-main).

**`claude/temp-meters-dab-pots-lcvi3w`** — merged into `main`, branch still not deleted. Flagged for **5+ weeks** (since ~2026-09-14). Action needed: delete it.

**11 standup branches with open PRs** — 1 new this week (`standup-2026-10-13`), none closed:

| Branch | PR | Age (days) |
|--------|-----|-----------|
| standup-2026-05-27 | #1 | 145 |
| standup-2026-06-16 | #2 | 125 |
| standup-2026-06-17 | #3 | 124 |
| standup-2026-06-22 | #4 | 119 |
| standup-2026-06-29 | #5 | 112 |
| standup-2026-07-13 | #6 | 98 |
| standup-2026-08-24 | #7 | 56 |
| standup-2026-08-31 | #8 | 49 |
| standup-2026-09-15 | #10 | 34 |
| standup-2026-10-05 | #11 | 14 |
| standup-2026-10-13 | #12 | 6 |

**New this week:** `standup-2026-10-13` / PR #12 (opened 2026-10-13).

The backlog of open standup PRs continues to grow (+1 since last week, oldest now 145 days). These appear to be automated daily standup notes. Consider closing them or merging via a bulk script.

### Dependency Health

| File | Status |
|------|--------|
| `backend/pyproject.toml` | fastapi>=0.115 (latest: 0.146.0 ✅), uvicorn>=0.32, sqlalchemy>=2.0, pydantic>=2.0 — all using version ranges, no conflicts |
| `sdk/pyproject.toml` | httpx>=0.27 (latest: 0.28.1 ✅), pydantic>=2.0, anthropic>=0.40 (latest: 1.15.0 ✅), openai>=1.50 (latest: 3.35.1 ✅) |
| `dashboard/package.json` | next@16.2.1, react@19.2.4, @tanstack/react-query@^5.95.1, recharts@^3.8.0 |

No lock files committed — builds are not fully reproducible. Consider adding `package-lock.json` (dashboard) and pinned requirements files (backend/sdk).

**Notable:** `anthropic` SDK has jumped significantly (0.40 → 1.15.0 available). The `>=0.40` floor is still satisfied but there may be breaking changes worth tracking if integrating newer Claude features.

### Code Quality

- **TODO/FIXME/HACK comments:** 0 across all `.py`, `.ts`, `.js` files — clean
- **Uncommitted changes:** None
- **Stashes:** None
- **Large files:** No files >1MB tracked in git (largest: `package-lock.json` at 245KB)

### Test Status

| Suite | Result |
|-------|--------|
| `sdk/tests/` (25 tests) | ✅ 25 passed, 1 skipped |
| `backend/tests/` (17 tests) | ✅ 17 passed |

Note: A benign atexit warning persists in SDK test teardown (`RuntimeError: Call agentlenz.init() before using AgentLenz`) — does not affect test outcomes but could be silenced with a try/except in the atexit handler.

### Git Hygiene

- Commits last 7 days: **7** (standup: 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-19 + health report + 2 others)
- Active daily standups being committed
- No stashes, no uncommitted changes

### Summary

Active development with clean tests and no code quality issues. The persistent backlog of 11 open standup PRs (oldest 145 days) remains the top hygiene concern — up from 10 last week. The `claude/temp-meters-dab-pots-lcvi3w` merged branch is still undeleted (5+ weeks). No regressions since last report.

---

## adelelo13/dockwright-macos-agent — ⚠️ Warning

### Stale Branches

2 branches: `main` and `fix/bug-audit-v1`.

**`fix/bug-audit-v1`** — open PR #1 ("fix: resolve 37 audited bugs + 2 hardening items across Dockwright"), opened **100 days ago** (2026-07-11). Not merged, not closed. This PR has been stalled since July with 37 bug fixes unmerged.

No merged-but-undeleted branches.

### Dependency Health

No SPM packages declared — project uses Apple frameworks only (by design per CLAUDE.md). No external dependency risk.

**Binary assets tracked in git:**
- `assets/demo.mov` (1.5 MB)
- `Dockwright/Resources/Models/embedding_model.onnx` (1.3 MB)
- `Dockwright/Resources/Models/hey_jarvis_v0.1.onnx` (1.3 MB)
- `Dockwright/Resources/Models/melspectrogram.onnx` (1.1 MB)

These are intentional bundled model assets. Total tracked binary: ~5.2 MB. Consider Git LFS for these if repo grows further.

### Code Quality

- **TODO/FIXME/HACK comments:** 0 in all Swift source files — clean
- **Uncommitted changes:** None
- **Stashes:** None

### Test Status

No automated test suite present. Build verification requires macOS + Xcode — not available in this environment.

### Git Hygiene

- Commits last 7 days: **0**
- Commits last 30 days: **0**
- Last commit: `d6d3f3f chore: update UIAutomationTool` (October 13, 2026)
- **Development stalled for 30+ days** — same status as last week

### Open PR

**PR #1: "fix: resolve 37 audited bugs + 2 hardening items across Dockwright"** — now **100 days open**, targeting `main`. Needs a decision: merge, close, or rebase.

### Summary

No code quality regressions. The situation is unchanged from last week: development activity stopped over 30 days ago, and a 100-day-old PR with 37 bug fixes sits unmerged. If this project is on hold, consider archiving the repo or closing the PR with a note.

---

## Cross-Repo Summary

| Repo | Health | Tests | TODOs | Open PRs | Commits (7d) | Change vs last week |
|------|--------|-------|-------|----------|--------------|---------------------|
| agentlenz | ⚠️ Warning | ✅ 42/43 pass | 0 | 11 open (oldest 145d) | 7 | +1 PR, +3 commits |
| dockwright-macos-agent | ⚠️ Warning | N/A | 0 | 1 open (100d) | 0 | No change |

**Key actions (unchanged from last week, escalating):**
1. **agentlenz**: Delete `claude/temp-meters-dab-pots-lcvi3w` (merged 5+ weeks ago). Bulk-close or merge the 11 standup PRs — oldest is now 145 days.
2. **dockwright-macos-agent**: Decide fate of PR #1 (now 100 days open, 37 bug fixes). Merge or close.
