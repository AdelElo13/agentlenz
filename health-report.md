# Weekly Health Report — 2026-04-27

> Generated automatically. Repos analysed: `agentlenz`, `DockWright-MacOS-Agent`.

---

## agentlenz — ⚠️ Warning

**Overall score: Warning** — both Python test suites pass; dashboard has minor npm patch updates available and `.pyc` bytecode files remain tracked in git (4th week open).

### 1. Stale Branches
No stale merged branches. Only `main` exists locally and on `origin`. ✅

### 2. Dependency Health

| Ecosystem | File | Status |
|---|---|---|
| Node / npm | `dashboard/package.json` | ⚠️ Minor patch updates available — see below |
| Python (backend) | `backend/pyproject.toml` | ✅ All packages at latest |
| Python (sdk) | `sdk/pyproject.toml` | ✅ All packages at latest |

**Python packages (installed):**

| Package | Installed | Latest |
|---------|-----------|--------|
| fastapi | 0.136.1 | 0.136.1 ✅ |
| httpx | 0.28.1 | 0.28.1 ✅ |
| pydantic | 2.13.3 | 2.13.3 ✅ |

**Dashboard — npm outdated:**

| Package | Pinned | Wanted | Latest |
|---------|--------|--------|--------|
| next | 16.2.1 | 16.2.4 | 16.2.4 ⚠️ |
| react | 19.2.4 | 19.2.5 | 19.2.5 ⚠️ |
| react-dom | 19.2.4 | 19.2.5 | 19.2.5 ⚠️ |
| @tanstack/react-query | ^5.95.1 | 5.100.5 | 5.100.5 ⚠️ |
| recharts | ^3.8.0 | 3.8.1 | 3.8.1 ✅ |

> `node_modules` not installed in the checkout — run `npm install` in `dashboard/` before building or auditing.

### 3. Code Quality — TODO / FIXME / HACK
```
Count: 0 across all .py, .ts, .js source files
```
✅ No technical debt markers found.

### 4. Test Status

| Suite | Command | Result |
|---|---|---|
| SDK | `cd sdk && python3 -m pytest -q` | ✅ **25 passed, 1 skipped** |
| Backend | `cd backend && python3 -m pytest -q` | ✅ **17 passed** |
| Dashboard | — | ⚠️ No test suite configured |

**Ongoing SDK warning (4th week):** An atexit `RuntimeError: Call agentlenz.init() before using AgentLenz` surfaces from `EventClient.flush` (`sdk/src/agentlenz/client.py:46`) during test teardown. Guard the flush handler against being called when `init()` was never invoked.

### 5. Git Hygiene

| Check | Status |
|---|---|
| Uncommitted changes | ✅ None |
| Stashes | ✅ None |
| Largest tracked file | ✅ `dashboard/package-lock.json` (244 KB — expected) |
| **Compiled bytecode tracked** | ⚠️ `__pycache__/` directories still committed — 4th week open |

**Action required (carry-over — 4th week):** Run `git rm -r --cached '**/__pycache__/'` to untrack existing bytecode, then commit. A root `.gitignore` was added (commit `7430592`) but `git rm --cached` was never run.

### Recent Activity
```
5631d0d standup: 2026-04-20
28e0715 standup: 2026-04-16
4355e16 standup: 2026-04-15
7430592 chore: add .gitignore to exclude __pycache__ and .pyc files
3a7bf06 health: weekly report 2026-04-13
```

Active standup cadence. No new feature commits this week.

---

## DockWright-MacOS-Agent — ⚠️ Warning

**Overall score: Warning** — no new commits since last report; structural issues (no automated tests, large binaries) remain open.

### 1. Stale Branches
No stale merged branches. Only `main` exists locally and on `origin`. ✅

### 2. Dependency Health
No standard package manifest (`Package.swift`, `package.json`, `requirements.txt`, `pyproject.toml`). Pure Xcode project — dependencies are managed through Xcode SPM integration.

⚠️ Cannot automatically check for outdated dependencies. Manually verify in Xcode → File → Packages → Update to Latest Package Versions.

### 3. Code Quality — TODO / FIXME / HACK
```
Count: 0 across 104 .swift source files
```
✅ No technical debt markers found.

### 4. Test Status
No `XCTest` target detected and no `swift test`-compatible `Package.swift`. `swift` CLI not available in this environment.

⚠️ **No tests can be run automatically.** Carry-over — no progress in 4 weeks.

**Recommendation:** Add a GitHub Actions workflow with:
```
xcodebuild test -scheme Dockwright -destination 'platform=macOS'
```

### 5. Git Hygiene

| Check | Status |
|---|---|
| Uncommitted changes | ✅ None |
| Stashes | ✅ None |
| Large binary files in git | ⚠️ ~6.7 MB tracked — see below |

**Large files tracked directly in git (unchanged for 4 weeks):**

| File | Size |
|---|---|
| `assets/demo.mov` | 1.5 MB |
| `Dockwright/Resources/Models/hey_jarvis_v0.1.onnx` | 1.3 MB |
| `Dockwright/Resources/Models/embedding_model.onnx` | 1.3 MB |
| `Dockwright/Resources/Models/melspectrogram.onnx` | 1.1 MB |
| `assets/screenshot-empty.png` | 664 KB |
| `assets/screenshot-chat.png` | 600 KB |
| `assets/demo.mp4` | 92 KB |

Total large binary payload: ~6.7 MB. Consider migrating ONNX models and media assets to Git LFS.

### Recent Activity
```
d6d3f3f chore: update UIAutomationTool
645d4ab fix: UI automation element search, Unicode typing, and threading
928f649 feat: whitelist safe sudo commands (pmset, systemsetup, defaults, etc.)
358b8d9 docs: simplify sudo instructions for non-devs
0837d7b docs: add optional sudo setup for system control
```

⚠️ No new commits since last week's health check.

---

## Action Items Summary

| Priority | Status | Repo | Action |
|---|---|---|---|
| High | ⚠️ Open (1st week) | agentlenz | `npm install && npm update` in `dashboard/` — patch updates for `next`, `react`, `react-dom`, `@tanstack/react-query` |
| Medium | 🔴 Open (4th week) | agentlenz | Run `git rm -r --cached '**/__pycache__/'` to untrack bytecode |
| Medium | 🟡 Ongoing | agentlenz | Fix `EventClient.flush` atexit guard in `sdk/src/agentlenz/client.py:46` |
| Medium | 🔴 Open (4th week) | DockWright-MacOS-Agent | Add `XCTest` target and CI test run via `xcodebuild test` |
| Low | 🔴 Open (4th week) | DockWright-MacOS-Agent | Migrate ONNX models + `demo.mov` to Git LFS |
| Low | 🔴 Open (3rd week) | agentlenz | Set up CI to run `pytest` per subproject on each push |
