# Weekly Health Report — 2026-09-21

Generated: 2026-09-21 | Repos: `adelelo13/agentlenz`, `adelelo13/dockwright-macos-agent`

---

## adelelo13/agentlenz — ⚠️ Warning

### Stale Branches

10 remote branches total. **1 merged-but-not-deleted branch** (carryover from last report):

| Branch | Status |
|--------|--------|
| `claude/temp-meters-dab-pots-lcvi3w` | ✅ Merged into main — safe to delete |

**9 standup branches unmerged into main** (+1 vs last report; `standup-2026-09-15` added this week):

| Branch | Age |
|--------|-----|
| standup-2026-05-27 | ~117 days |
| standup-2026-06-16 | ~97 days |
| standup-2026-06-17 | ~96 days |
| standup-2026-06-22 | ~91 days |
| standup-2026-06-29 | ~84 days |
| standup-2026-07-13 | ~70 days |
| standup-2026-08-24 | ~28 days |
| standup-2026-08-31 | ~21 days |
| standup-2026-09-15 | 6 days (new) |

**Pattern:** Standup branches accumulate weekly and are never closed or merged. The queue now holds 9 open draft PRs. They serve as reference documents, not feature work — they should be merged or closed immediately after creation.

### Dependency Health

- **Backend** (`backend/pyproject.toml`): FastAPI ≥ 0.115, SQLAlchemy ≥ 2.0, Pydantic ≥ 2.0. Minimum-version constraints only (no upper bounds, no lock file). No change since last report.
- **Dashboard** (`dashboard/package.json`): Next.js 16.2.1, React 19.2.4, Recharts ^3.8.0. `package-lock.json` present ✅
- **SDK** (`sdk/pyproject.toml`): httpx ≥ 0.27, pydantic ≥ 2.0. No lock file.
- No known CVEs flagged for declared dependency ranges.
- **Recommendation:** Add `uv.lock` (backend + SDK) for reproducible installs and deterministic CI.

### Code Quality

- **TODO/FIXME/HACK comments:** 0 across all Python and TypeScript files ✅
- No inline debt markers.

### Test Status

| Suite | Result |
|-------|--------|
| `sdk/tests/` (pytest) | ✅ 25 passed, 1 skipped |
| `backend/tests/` (pytest) | ✅ 17 passed |
| `dashboard/` | ❌ No test suite |

Both Python test suites pass cleanly. Dashboard remains untested.

### Git Hygiene

- Working tree: clean ✅
- Stashes: none ✅
- Large files: none (largest tracked file: `package-lock.json` at 240 KB) ✅
- Recent activity: daily standup commits (latest: 2026-09-18) — repo actively maintained ✅

### Change vs Last Report (2026-09-14)

- Added `standup-2026-09-15` branch (now 9 unmerged standup branches, up from 8)
- `claude/temp-meters-dab-pots-lcvi3w` still not deleted (persists 7+ weeks)
- Test results confirmed passing (no regressions)

---

## adelelo13/dockwright-macos-agent — 🔴 Needs Attention

### Stale Branches

2 branches total. `fix/bug-audit-v1` has **1 commit ahead of main** that has not been merged in **72 days**.

### Open PR — Critical Security Fixes (72 Days Unmerged)

**`fix/bug-audit-v1` → "fix: resolve 37 audited bugs + 2 hardening items across Dockwright"**

- Branch last commit: 2026-07-11 (commit: `f38d3c0`)
- PR opened: ~2026-07-11
- **Age: 72 days** (was 65 days at last report — +7 days, zero new activity)
- Main last commit: **2026-04-06** (168 days ago — repo dormant for 5.5 months)

This PR contains confirmed security patches that remain entirely unmerged:

| Severity | Issue |
|----------|-------|
| 🔴 Critical | Unauthenticated LAN RCE — A2A (`:8766`) and MCP (`:8767`) servers bound `0.0.0.0` with no auth |
| 🔴 Critical | Shell injection bypass via command chaining (`echo && sudo rm -rf ~`) |
| 🟠 High | Discord webhook host validation bypass |
| 🟠 High | Claude OAuth `state` parameter verification missing |
| 🟠 High | Gemini tool calls silently dropped; OpenAI o3/o4 requests returning 400 |
| 🟠 High | Cron DOM/DOW POSIX logic ANDed instead of ORed; next-run skips target minute |
| 🟡 Medium | 21 `Process` call sites with unbounded `waitUntilExit` (potential process leaks) |

**37 total confirmed bugs fixed in this PR. Still unmerged after 72 days.**

### Dependency Health

No SPM packages by design (`CLAUDE.md` specifies Apple frameworks only for Phases 1–4). No version concerns.

### Code Quality

- **TODO/FIXME/HACK comments:** 0 across all 104 Swift source files ✅
- No inline debt markers.

### Test Status

No XCTest target exists. Build correctness verified by `xcodebuild` compile check only. Cannot run build in this Linux environment (macOS-only toolchain required).

### Git Hygiene

- Working tree: clean ✅
- Stashes: none ✅
- Untracked files: none ✅
- Large files: ONNX models and demo assets (intentional per project design) ✅

### Change vs Last Report (2026-09-14)

- No commits to `main` or `fix/bug-audit-v1` in 7 days
- PR #1 age: 65 → 72 days
- Repository continues to be dormant on `main` since 2026-04-06

---

## Summary

| Repo | Score | Top Issue | Change Since 2026-09-14 |
|------|-------|-----------|--------------------------|
| agentlenz | ⚠️ Warning | 9 unmerged standup PRs (117 days oldest), 1 merged branch not deleted | +1 standup branch; tests still passing |
| dockwright-macos-agent | 🔴 Needs Attention | PR #1 with critical LAN RCE + shell injection fixes open 72 days | Age: 65 → 72 days. Zero activity. |

### Recommended Actions

1. **[Urgent] Merge `dockwright-macos-agent` PR #1.** Critical LAN RCE and shell injection bypass are unpatched on `main`. Now 72 days old and worsening.
2. **[Cleanup] Close agentlenz standup PRs** going back to May 2026. Consider a policy: standup branches merge same-day or auto-close after 7 days.
3. **[Cleanup] Delete `origin/claude/temp-meters-dab-pots-lcvi3w`** — merged into main, abandoned Claude session branch, safe to remove.
4. **[Hygiene] Add lock files** (`uv.lock`) to `backend/` and `sdk/` for reproducible installs.
5. **[Testing] Add dashboard test suite** (Vitest or Jest) — only Python backend/SDK is tested.
