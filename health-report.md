# Weekly Health Report — 2026-08-31

Generated: 2026-08-31 | Repos: `adelelo13/agentlenz`, `adelelo13/dockwright-macos-agent`

---

## adelelo13/agentlenz — ⚠️ Warning

### Stale Branches

No branches are merged-but-not-deleted on `main`. However, **8 standup draft PRs** have never been merged or closed and are accumulating since May 2026:

| PR | Branch | Open Since |
|----|--------|------------|
| #1 | standup-2026-05-27 | 2026-05-27 (96 days) |
| #2 | standup-2026-06-16 | 2026-06-16 (76 days) |
| #3 | standup-2026-06-17 | 2026-06-17 (75 days) |
| #4 | standup-2026-06-22 | 2026-06-22 (70 days) |
| #5 | standup-2026-06-29 | 2026-06-29 (63 days) |
| #6 | standup-2026-07-13 | 2026-07-13 (49 days) |
| #7 | standup-2026-08-24 | 2026-08-24 (7 days) |
| #8 | standup-2026-08-31 | 2026-08-31 (today) |

**Action needed:** Close or merge PRs #1–#7. Standup branches are reference docs and should be merged quickly after creation (or created directly on main).

### Dependency Health

- **Backend** (`backend/pyproject.toml`): Python ≥ 3.10, FastAPI ≥ 0.115, SQLAlchemy ≥ 2.0, Pydantic ≥ 2.0. No pinned upper bounds — latest-compatible installs. Dependency versions look reasonable; no known CVEs flagged. No automated dep-update tooling (Dependabot, Renovate) configured.
- **Dashboard** (`dashboard/package.json`): Next.js 16.2.1, React 19.2.4, Tailwind 4, TypeScript 5. These are recent versions. No `npm audit` available in this environment.
- **SDK** (`sdk/pyproject.toml`): Python package. No lock file checked in — `uv.lock` or `poetry.lock` would improve reproducibility.

### Code Quality

- **TODO/FIXME/HACK comments:** 0 across all Python, TS, JS files ✅
- Code appears clean with no inline debt markers.

### Test Status

```
backend/tests/ — 17 tests
17 passed in 0.41s ✅
```

All 17 backend tests pass. No test suite found for the dashboard or SDK packages.

### Git Hygiene

- Working tree: clean ✅
- Uncommitted changes: none ✅
- Stashes: none ✅
- Large files: none ✅
- HEAD is detached from `refs/heads/main` (expected in CI/remote session)

---

## adelelo13/dockwright-macos-agent — 🔴 Needs Attention

### Stale Branches

- **`fix/bug-audit-v1`** — 1 unmerged branch with an open (non-draft) PR.

### Open PRs — Critical

**PR #1: "fix: resolve 37 audited bugs + 2 hardening items across Dockwright"**
- Open since: **2026-07-11 (51 days)**
- Status: Open, not draft, not merged

This PR contains **critical security patches** that should not be sitting unmerged:

- **Unauthenticated LAN RCE (Critical):** A2A (`:8766`) and MCP (`:8767`) servers were bound to `0.0.0.0` with no authentication, exposing the shell tool surface to any device on the local network. Fixed to loopback-only.
- **Shell injection bypass:** The sudo gate and destructive-command blocklist were bypassable via chaining (`echo && sudo rm -rf ~`). Fixed with a tokenizing scanner.
- **Discord webhook exfiltration, Claude OAuth state bypass, WhatsApp HMAC missing** — all fixed in this PR.
- 37 total confirmed bugs fixed including Gemini tool call parsing, OpenAI `o3`/`o4` request format, cron POSIX DOM/DOW logic, atomic writes, and voice/screenshot threading issues.

**This PR has been open for 51 days with critical security fixes unmerged.** Recommend immediate review and merge.

### Dependency Health

No SPM packages (by design per CLAUDE.md). Pure Apple frameworks. No dependency version concerns.

Bundled binary models in `Dockwright/Resources/Models/`:
- `embedding_model.onnx` — 1.3 MB
- `hey_jarvis_v0.1.onnx` — 1.3 MB
- `melspectrogram.onnx` — 1.1 MB
- `assets/demo.mov` — 1.5 MB

All are intentional assets, not accidental large-file commits.

### Code Quality

- **TODO/FIXME/HACK comments:** 0 across all 104 Swift files ✅
- No inline debt markers.

### Test Status

No XCTest target exists in the project (noted in PR #1: adding one requires `project.pbxproj` surgery given `PBXFileSystemSynchronizedRootGroup` setup). Tests are verified via `xcodebuild` build success + standalone logic harness (documented in PR). Cannot run in this environment (macOS-only).

### Git Hygiene

- Working tree: clean ✅
- Uncommitted changes: none ✅
- Stashes: none ✅
- HEAD is detached at `refs/heads/main` (expected in CI/remote session)

---

## Summary

| Repo | Score | Top Issue |
|------|-------|-----------|
| agentlenz | ⚠️ Warning | 8 standup draft PRs open since May 2026, never merged/closed |
| dockwright-macos-agent | 🔴 Needs Attention | PR #1 with critical security fixes (LAN RCE, shell injection) open 51 days |

### Recommended Actions

1. **[Urgent] Merge or review `dockwright-macos-agent` PR #1.** It contains a critical unauthenticated RCE fix. 51 days is too long for a security patch to sit open.
2. **[Cleanup] Close agentlenz standup PRs #1–#7.** They are draft reference docs; merge them to main or close them to keep the PR list meaningful.
3. **[Hygiene] Add a lock file** (`uv.lock` or `poetry.lock`) to agentlenz backend and SDK for reproducible installs.
4. **[Testing] Add a dashboard test suite** (Vitest or Jest) to agentlenz — currently only the Python backend is tested.
