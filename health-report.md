# Weekly Health Report — 2026-05-04

> Generated automatically. Repos analysed: `agentlenz`, `DockWright-MacOS-Agent`.

---

## agentlenz — ⚠️ Warning

**Overall score: Warning** — SDK tests pass; backend tests newly broken (missing virtualenv deps); dashboard patch updates still unapplied; `.pyc` bytecode files remain tracked in git (5th week open).

### 1. Stale Branches
No stale merged branches. Only `main` exists locally and on `origin`. ✅

### 2. Dependency Health

| Ecosystem | File | Status |
|---|---|---|
| Node / npm | `dashboard/package.json` | ⚠️ Minor patch updates available — see below |
| Python (backend) | `backend/pyproject.toml` | ⚠️ Cannot verify — deps not installed in env |
| Python (sdk) | `sdk/pyproject.toml` | ✅ All project packages at latest |

**Dashboard — npm outdated:**

| Package | Pinned | Latest | Delta |
|---------|--------|--------|-------|
| next | 16.2.1 | 16.2.4 | ⚠️ patch |
| react | 19.2.4 | 19.2.5 | ⚠️ patch |
| react-dom | 19.2.4 | 19.2.5 | ⚠️ patch |
| @tanstack/react-query | ^5.95.1 | 5.100.9 | ⚠️ minor (was 5.100.5 last week) |
| recharts | ^3.8.0 | 3.8.1 | ✅ |

> `node_modules` not installed — run `npm install` in `dashboard/` before building or auditing.

### 3. Code Quality — TODO / FIXME / HACK
```
Count: 0 across all .py, .ts, .js source files
```
✅ No technical debt markers found.

### 4. Test Status

| Suite | Command | Result |
|---|---|---|
| SDK | `cd sdk && python3 -m pytest -q` | ✅ **25 passed, 1 skipped** |
| Backend | `cd backend && python3 -m pytest -q` | 🔴 **FAIL — `ModuleNotFoundError: No module named 'sqlalchemy'`** |
| Dashboard | — | ⚠️ No test suite configured |

**Backend regression (new this week):** `sqlalchemy` is not installed in the current Python environment, causing the test suite to fail at import time in `tests/conftest.py`. Run `pip install -e ".[dev]"` inside `backend/` to restore the test environment. Was passing (17 tests) as recently as 2026-04-27.

**Ongoing SDK warning (5th week):** An atexit `RuntimeError: Call agentlenz.init() before using AgentLenz` surfaces from `EventClient.flush` (`sdk/src/agentlenz/client.py:46`) during test teardown. Guard the flush handler against being called when `init()` was never invoked.

### 5. Git Hygiene

| Check | Status |
|---|---|
| Uncommitted changes | ✅ None |
| Stashes | ✅ None |
| Largest tracked file | ✅ `dashboard/package-lock.json` (244 KB — expected) |
| **Compiled bytecode tracked** | ⚠️ 50 `__pycache__/*.pyc` files still committed — 5th week open |

**Action required (carry-over — 5th week):** Run `git rm -r --cached '**/__pycache__/'` to untrack existing bytecode, then commit. `.gitignore` already has `**/__pycache__/` but `git rm --cached` was never run.

### Recent Activity
```
6dfe816 health: weekly report 2026-04-27
d0f277c health: weekly report 2026-04-20
5631d0d standup: 2026-04-20
28e0715 standup: 2026-04-16
4355e16 standup: 2026-04-15
```

No new feature or fix commits since the 2026-04-20 standup. Standup cadence active.

---

## DockWright-MacOS-Agent — ⚠️ Warning

**Overall score: Warning** — no new commits for the second consecutive week; structural issues (no automated tests, large binaries in git) remain open.

### 1. Stale Branches
No stale merged branches. Only `main` exists locally and on `origin`. ✅

### 2. Dependency Health
No standard package manifest (`Package.swift`, `package.json`, `requirements.txt`, `pyproject.toml`). Pure Xcode project — dependencies are managed through Xcode SPM integration.

⚠️ Cannot automatically check for outdated dependencies. Manually verify in Xcode → File → Packages → Update to Latest Package Versions.

### 3. Code Quality — TODO / FIXME / HACK
```
Count: 0 across all .swift source files
```
✅ No technical debt markers found.

### 4. Test Status
No `XCTest` target detected and no `swift test`-compatible `Package.swift`. `swift` CLI not available in this Linux environment.

⚠️ **No tests can be run automatically.** Carry-over — no progress in 5 weeks.

**Recommendation:** Add a GitHub Actions macOS workflow:
```yaml
- run: xcodebuild test -scheme Dockwright -destination 'platform=macOS'
```

### 5. Git Hygiene

| Check | Status |
|---|---|
| Uncommitted changes | ✅ None |
| Stashes | ✅ None |
| Large binary files in git | ⚠️ ~6.7 MB tracked — unchanged since first report |

**Large files tracked directly in git (5 weeks open):**

| File | Size |
|---|---|
| `assets/demo.mov` | 1.5 MB |
| `Dockwright/Resources/Models/hey_jarvis_v0.1.onnx` | 1.3 MB |
| `Dockwright/Resources/Models/embedding_model.onnx` | 1.3 MB |
| `Dockwright/Resources/Models/melspectrogram.onnx` | 1.1 MB |
| `assets/screenshot-empty.png` | 664 KB |
| `assets/screenshot-chat.png` | 600 KB |
| `assets/demo.mp4` | 92 KB |

Consider migrating ONNX models and media assets to Git LFS.

### Recent Activity
```
d6d3f3f chore: update UIAutomationTool
645d4ab fix: UI automation element search, Unicode typing, and threading
928f649 feat: whitelist safe sudo commands (pmset, systemsetup, defaults, etc.)
358b8d9 docs: simplify sudo instructions for non-devs
0837d7b docs: add optional sudo setup for system control
```

⚠️ No new commits since last week (or the week before).

---

## Action Items Summary

| Priority | Status | Repo | Action |
|---|---|---|---|
| **High** | 🔴 **New this week** | agentlenz | Restore backend test env: `pip install -e ".[dev]"` in `backend/` |
| High | ⚠️ Open (2nd week) | agentlenz | `npm install && npm update` in `dashboard/` — patch updates for `next`, `react`, `react-dom`, `@tanstack/react-query` |
| Medium | 🔴 Open (5th week) | agentlenz | Run `git rm -r --cached '**/__pycache__/'` to untrack 50 bytecode files |
| Medium | 🟡 Ongoing (5th week) | agentlenz | Fix `EventClient.flush` atexit guard in `sdk/src/agentlenz/client.py:46` |
| Medium | 🔴 Open (5th week) | DockWright-MacOS-Agent | Add `XCTest` target and CI test run via `xcodebuild test` |
| Low | 🔴 Open (5th week) | DockWright-MacOS-Agent | Migrate ONNX models + `demo.mov` to Git LFS |
| Low | 🔴 Open (4th week) | agentlenz | Set up CI to run `pytest` per subproject on each push |
