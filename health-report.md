# Weekly Health Report — 2026-04-13

> Generated automatically. Repos analysed: `agentlenz`, `DockWright-MacOS-Agent`.

---

## agentlenz — ⚠️ Warning

**Overall score: Warning** — tests confirmed passing for the first time this week; dashboard deps are stale and pyc tracking remains unresolved.

### 1. Stale Branches
No stale merged branches. Only `main` exists locally and on `origin`. ✅

### 2. Dependency Health

| Ecosystem | File | Status |
|---|---|---|
| Node / npm | `dashboard/package.json` | ⚠️ See below |
| Python (backend) | `backend/pyproject.toml` | ✅ Semver ranges current; 17 tests pass |
| Python (sdk) | `sdk/pyproject.toml` | ✅ Semver ranges current; 25 tests pass |

**Dashboard — outdated / missing packages** (`npm outdated`):

| Package | Installed | Latest |
|---|---|---|
| `@tanstack/react-query` | **MISSING** | 5.99.0 |
| `next` | 16.2.1 | **16.2.3** |
| `react` | 19.2.4 | **19.2.5** |
| `react-dom` | 19.2.4 | **19.2.5** |
| `recharts` | 3.8.0 | **3.8.1** |

`node_modules` is not fully installed — `@tanstack/react-query` and several `@types/*` packages are missing. Run `npm install` in `dashboard/` to restore.

### 3. Code Quality — TODO / FIXME / HACK
```
Count: 0 across all .py, .ts, .js source files
```
✅ No technical debt markers found.

### 4. Test Status
Tests were executed this week:

| Suite | Command | Result |
|---|---|---|
| SDK | `cd sdk && python3 -m pytest -q` | ✅ **25 passed, 1 skipped** |
| Backend | `cd backend && python3 -m pytest -q` | ✅ **17 passed** |
| Dashboard | — | ⚠️ No test suite configured |

**Minor SDK warning:** An atexit `RuntimeError: Call agentlenz.init() before using AgentLenz` surfaces from `EventClient.flush` (`sdk/src/agentlenz/client.py:46`) during test teardown. Tests still pass, but the flush handler should guard against being called when `init()` was never invoked.

### 5. Git Hygiene

| Check | Status |
|---|---|
| Uncommitted changes | ✅ None |
| Stashes | ✅ None |
| Largest tracked file | ✅ `dashboard/package-lock.json` (242 KB — expected) |
| Compiled bytecode tracked | ⚠️ `.pyc` files still committed in `sdk/tests/__pycache__/` and `backend/` |
| Root `.gitignore` | ⚠️ Does not exist — carry-over from 2026-04-06 |
| HEAD state | ⚠️ Detached at `refs/heads/main` (checkout artifact) |

**Action required (carry-over):** Create a root `.gitignore` with at minimum:
```
**/__pycache__/
**/*.pyc
```
Then run `git rm -r --cached '**/__pycache__/'` to untrack existing bytecode.

### Recent Activity
```
7f93346 health: weekly report 2026-04-06
1a3adbb standup: 2026-04-03
be6e65e standup: 2026-04-01
ea2b54d standup: 2026-03-27
011256f fix(backend): use ssl=disable query param for asyncpg on Fly
```

No new code commits since last week's health report. Recent activity is standup notes only.

---

## DockWright-MacOS-Agent — ⚠️ Warning

**Overall score: Warning** — no new commits since last report; structural issues (no tests, large binaries) remain open.

### 1. Stale Branches
No stale merged branches. Only `main` exists locally and on `origin`. ✅

⚠️ **HEAD is in a detached state** (`HEAD detached at refs/heads/main`) — carry-over from last week.

### 2. Dependency Health
No standard package manifest (`Package.swift`, `Package.resolved`, `package.json`, `requirements.txt`). Pure Xcode project — no Swift Package Manager dependencies declared.

| Setting | Value |
|---|---|
| Swift version | 5.0 |
| Deployment target | macOS 14.0 (Sonoma) |
| SPM packages | None |
| Third-party deps | Embedded via system Python (`websocket`, `asyncio`, `subprocess`) |

⚠️ Cannot automatically check for outdated dependencies. Manually verify in Xcode → File → Packages → Update to Latest Package Versions.

### 3. Code Quality — TODO / FIXME / HACK
```
Count: 0 across 104 .swift source files
```
✅ No technical debt markers found.

### 4. Test Status
No `XCTest` target detected and no test scheme found in `Dockwright.xcodeproj`. `swift` CLI is not available in this environment.

⚠️ **No tests exist or can be run.** Carry-over from last week — no progress.

**Recommendation:** Add an `XCTest` target or a GitHub Actions workflow with:
```
xcodebuild test -scheme Dockwright -destination 'platform=macOS'
```

### 5. Git Hygiene

| Check | Status |
|---|---|
| Uncommitted changes | ✅ None |
| Stashes | ✅ None |
| Large binary files in git | ⚠️ See below |

**Large files tracked directly in git (unchanged from last week):**

| File | Size |
|---|---|
| `assets/demo.mov` | 1.5 MB |
| `Dockwright/Resources/Models/embedding_model.onnx` | 1.3 MB |
| `Dockwright/Resources/Models/hey_jarvis_v0.1.onnx` | 1.2 MB |
| `Dockwright/Resources/Models/melspectrogram.onnx` | 1.0 MB |
| `assets/screenshot-empty.png` | 661 KB |
| `assets/screenshot-chat.png` | 600 KB |

Total large binary payload: ~6.3 MB. Consider migrating ONNX models and media assets to Git LFS.

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
| High | 🔴 New | agentlenz | Run `npm install` in `dashboard/` — `@tanstack/react-query` and others are missing |
| Medium | 🟡 New | agentlenz | Update dashboard packages: `npm update` (`next` → 16.2.3, `react` → 19.2.5, etc.) |
| Medium | 🟡 New | agentlenz | Fix `EventClient.flush` atexit guard in `sdk/src/agentlenz/client.py:46` |
| Medium | 🔴 Open (2nd week) | agentlenz | Add root `.gitignore` and untrack `__pycache__` / `.pyc` files |
| Medium | 🔴 Open (2nd week) | DockWright-MacOS-Agent | Verify / fix detached HEAD state |
| Medium | 🔴 Open (2nd week) | DockWright-MacOS-Agent | Add `XCTest` target and CI test run |
| Low | 🔴 Open (2nd week) | DockWright-MacOS-Agent | Migrate ONNX models + `demo.mov` to Git LFS |
| Low | 🔴 Open (2nd week) | agentlenz | Set up CI to run `pytest` per subproject on each push |
