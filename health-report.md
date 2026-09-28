# Weekly Health Report — 2026-09-28

Generated: 2026-09-28 | Repos: `adelelo13/agentlenz`, `adelelo13/dockwright-macos-agent`

---

## adelelo13/agentlenz — ⚠️ Warning

### Stale Branches

10 remote branches total.

**`claude/temp-meters-dab-pots-lcvi3w`** — merged into `main`, still not deleted. Flagged since 2026-09-14.

**9 standup branches unmerged into main** (no change vs last report):

| Branch | Days Open |
|--------|-----------|
| standup-2026-05-27 | 124 days |
| standup-2026-06-16 | 104 days |
| standup-2026-06-17 | 103 days |
| standup-2026-06-22 | 98 days |
| standup-2026-06-29 | 91 days |
| standup-2026-07-13 | 77 days |
| standup-2026-08-24 | 35 days |
| standup-2026-08-31 | 28 days |
| standup-2026-09-15 | 13 days |

**Pattern:** Standup branches accumulate weekly and are never closed. The queue remains at 9 branches for the second consecutive week. These are reference documents — they should be merged or closed same-day.

### Dependency Health

- **Backend** (`backend/pyproject.toml`): FastAPI ≥ 0.115, SQLAlchemy ≥ 2.0, Pydantic ≥ 2.0. Minimum-version constraints only. No lock file.
- **Dashboard** (`dashboard/package.json`): Next.js 16.2.1, React 19.2.4, Recharts ^3.8.0. `package-lock.json` present ✅
- **SDK** (`sdk/pyproject.toml`): httpx ≥ 0.27, pydantic ≥ 2.0. No lock file.
- No known CVEs flagged for declared dependency ranges.
- **Recommendation:** Add `uv.lock` to `backend/` and `sdk/` for reproducible CI installs.

### Code Quality

- **TODO/FIXME/HACK comments:** 0 across all Python and TypeScript files ✅

### Test Status

| Suite | Result |
|-------|--------|
| `backend/tests/` (pytest) | ✅ 17 passed |
| `sdk/tests/` (pytest) | ✅ 25 passed, 1 skipped |

One benign atexit warning in SDK tests: `RuntimeError: Call agentlenz.init() before using AgentLenz` — occurs only at teardown, does not affect test outcomes.

### Git Hygiene

- Working tree: clean ✅
- Stashes: none ✅
- Untracked files: none ✅
- Last `main` commit: `standup: 2026-09-24`

### Change vs Last Report (2026-09-21)

- No new standup branches added (was +1/week previously)
- `claude/temp-meters-dab-pots-lcvi3w` still not deleted
- Tests: backend suite now runs (17 passed) — first confirmed run
- Otherwise unchanged

---

## adelelo13/dockwright-macos-agent — 🔴 Needs Attention

### Stale Branches

1 open branch:

| Branch | Status |
|--------|--------|
| `fix/bug-audit-v1` | 🔴 Open, **79 days** unmerged (was 72 at last report) |

`main` last commit: **2026-04-06** (175 days dormant).

`fix/bug-audit-v1` contains confirmed security patches that remain entirely unmerged:

| Severity | Issue |
|----------|-------|
| 🔴 Critical | Unauthenticated LAN RCE — A2A (`:8766`) and MCP (`:8767`) servers bound `0.0.0.0` with no auth |
| 🔴 Critical | Shell injection bypass via command chaining (`echo && sudo rm -rf ~`) |
| 🟠 High | Discord webhook host validation bypass |
| 🟠 High | Claude OAuth `state` parameter verification missing |
| 🟠 High | Gemini tool calls silently dropped; OpenAI o3/o4 requests returning 400 |
| 🟠 High | Cron DOM/DOW POSIX logic ANDed instead of ORed; next-run skips target minute |
| 🟡 Medium | 21 `Process` call sites with unbounded `waitUntilExit` (potential process leaks) |

**37 total confirmed bugs fixed in this PR. Unmerged for 79 days.**

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
- Large files: ONNX models and demo assets (intentional) ✅

### Change vs Last Report (2026-09-21)

- No commits to `main` or `fix/bug-audit-v1`
- PR age: 72 → 79 days (+7 days, zero activity)

---

## Summary

| Repo | Score | Top Issue | Change Since 2026-09-21 |
|------|-------|-----------|--------------------------|
| agentlenz | ⚠️ Warning | 9 unmerged standup PRs (124 days oldest), 1 merged branch not deleted | No new branches; backend tests confirmed passing (17) |
| dockwright-macos-agent | 🔴 Needs Attention | PR #1 with critical LAN RCE + shell injection fixes open **79 days** | Age: 72 → 79 days. Zero activity. |

### Recommended Actions

1. **[Urgent] Merge `dockwright-macos-agent` PR #1.** Critical LAN RCE and shell injection bypass are unpatched on `main`. Now 79 days old. Every week this stays open is another week the released binary carries two critical vulnerabilities.
2. **[Cleanup] Close agentlenz standup PRs** going back to May 2026. Consider: merge same-day or auto-close after 7 days via a GitHub Actions stale-branch policy.
3. **[Cleanup] Delete `origin/claude/temp-meters-dab-pots-lcvi3w`** — merged into main, safe to remove.
4. **[Hygiene] Add lock files** (`uv.lock`) to `backend/` and `sdk/` for reproducible installs.
5. **[Testing] Add dashboard test suite** (Vitest or Jest) — only Python backend/SDK is covered.
