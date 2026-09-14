# Weekly Health Report — 2026-09-14

Generated: 2026-09-14 | Repos: `adelelo13/agentlenz`, `adelelo13/dockwright-macos-agent`

---

## adelelo13/agentlenz — ⚠️ Warning

### Stale Branches

9 branches total. No branches are merged-but-not-deleted on `main`.  
One extra non-standup branch: **`claude/temp-meters-dab-pots-lcvi3w`** — appears to be a stale Claude session branch with no open PR; safe to delete.

**8 standup draft PRs still open and unmerged since May 2026:**

| PR | Branch | Open Since | Age |
|----|--------|------------|-----|
| #1 | standup-2026-05-27 | 2026-05-27 | ~110 days |
| #2 | standup-2026-06-16 | 2026-06-16 | ~90 days |
| #3 | standup-2026-06-17 | 2026-06-17 | ~89 days |
| #4 | standup-2026-06-22 | 2026-06-22 | ~84 days |
| #5 | standup-2026-06-29 | 2026-06-29 | ~77 days |
| #6 | standup-2026-07-13 | 2026-07-13 | ~63 days |
| #7 | standup-2026-08-24 | 2026-08-24 | ~21 days |
| #8 | standup-2026-08-31 | 2026-08-31 | ~14 days |

**No change since last report (2026-08-31).** PRs #1–#7 remain open; #8 was newly opened in the last report and is now 14 days old.

**Action needed:** Close or merge PRs #1–#7. Standup branches are reference docs and should be merged quickly after creation or committed directly to main.

### Dependency Health

- **Backend** (`backend/pyproject.toml`): Python ≥ 3.10, FastAPI ≥ 0.115, SQLAlchemy ≥ 2.0, Pydantic ≥ 2.0. Minimum-version-only constraints (no upper bounds). No lock file committed — `uv.lock` or `poetry.lock` would improve reproducibility and CI determinism.
- **Dashboard** (`dashboard/package.json`): Next.js + React + Tailwind + TypeScript. `package-lock.json` present ✅. No Dependabot/Renovate configured for automated dep updates.
- **SDK** (`sdk/pyproject.toml`): Python package with no lock file.
- No known CVEs flagged for declared dependencies.

### Code Quality

- **TODO/FIXME/HACK comments:** 0 across all Python and TypeScript files ✅
- Code appears clean with no inline debt markers.

### Test Status

- `backend/tests/`: 17 tests — passed (last verified 2026-08-31, no new changes to rerun against).
- Dashboard: no test suite.
- SDK: no test suite visible.

### Git Hygiene

- Working tree: clean ✅
- Latest commit: `standup: 2026-09-14` (today) — repo is actively maintained
- Stashes: none ✅
- Large files: none ✅

---

## adelelo13/dockwright-macos-agent — 🔴 Needs Attention

### Stale Branches

2 branches total. `fix/bug-audit-v1` has an open (non-draft) PR with critical security fixes that has been open **65 days** with no activity.

### Open PRs — Critical

**PR #1: "fix: resolve 37 audited bugs + 2 hardening items across Dockwright"**
- Open since: **2026-07-11 (65 days, up from 51 days at last report)**
- Status: Open, not draft, not merged
- Last commit on branch: **2026-04-06** (no new commits since PR was opened on July 11 — branch predates the PR title)

This PR contains **critical security patches** that remain unmerged:

| Severity | Issue |
|----------|-------|
| 🔴 Critical | Unauthenticated LAN RCE — A2A (`:8766`) and MCP (`:8767`) servers bound `0.0.0.0` with no auth, exposing the shell surface to all LAN devices |
| 🔴 Critical | Shell injection bypass — sudo gate and destructive-command blocklist were bypassable via command chaining (`echo && sudo rm -rf ~`) |
| 🟠 High | Discord webhook host validation (substring match allowed exfiltration to attacker host) |
| 🟠 High | Claude OAuth `state` verification missing |
| 🟠 High | Gemini tool calls silently dropped; OpenAI o3/o4 requests 400ing |
| 🟠 High | Cron POSIX DOM/DOW logic (ANDed instead of ORed); next-run skipped target minute |
| 🟡 Medium | 21 process call sites with unbounded `waitUntilExit` (child processes could leak indefinitely) |

37 total confirmed bugs fixed in this PR. **Still unmerged after 65 days.**

### Activity Since Last Report (2026-08-31)

- **No commits** to `main` or `fix/bug-audit-v1` in the past 14 days.
- Last commit to `main`: **2026-04-06** (161 days ago — repo has been dormant for 5+ months).
- PR #1 has received no review activity.

### Dependency Health

No SPM packages (by design per `CLAUDE.md`). Pure Apple frameworks only. No dependency version concerns.

### Code Quality

- **TODO/FIXME/HACK comments:** 0 across all Swift files ✅
- No inline debt markers.

### Test Status

No XCTest target exists. Tests are verified via `xcodebuild` build success + standalone logic harness. Cannot run in this environment (macOS-only build).

### Git Hygiene

- Working tree on `main`: clean ✅
- Stashes: none ✅
- Large files: intentional assets only (`embedding_model.onnx`, `hey_jarvis_v0.1.onnx`, `melspectrogram.onnx`, `demo.mov`) ✅

---

## Summary

| Repo | Score | Top Issue | Change Since 2026-08-31 |
|------|-------|-----------|--------------------------|
| agentlenz | ⚠️ Warning | 8 standup draft PRs open 14–110 days, never merged/closed | No change — same PRs, new standup added |
| dockwright-macos-agent | 🔴 Needs Attention | PR #1 with critical LAN RCE + shell injection fixes open 65 days | Age: 51 → 65 days. Zero new activity. |

### Recommended Actions

1. **[Urgent] Merge `dockwright-macos-agent` PR #1.** It contains a critical unauthenticated LAN RCE fix. Now 65 days old — every day this is unmerged, any device on the user's LAN can execute arbitrary shell commands via the unpatched A2A/MCP servers.
2. **[Cleanup] Close agentlenz standup PRs #1–#7** (PRs going back to May 2026). They are draft reference docs; merge or close to keep the PR queue meaningful.
3. **[Cleanup] Delete `claude/temp-meters-dab-pots-lcvi3w`** branch in agentlenz — appears to be an abandoned Claude session branch with no PR.
4. **[Hygiene] Add a lock file** (`uv.lock` or `poetry.lock`) to agentlenz backend and SDK for reproducible installs.
5. **[Testing] Add a dashboard test suite** (Vitest or Jest) — only the Python backend is tested.
