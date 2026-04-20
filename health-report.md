# Weekly Health Report — 2026-04-20

> Generated automatically. Repos analysed: `agentlenz`, `DockWright-MacOS-Agent`.

---

## agentlenz — ⚠️ Warning

**Overall score: Warning** — both Python test suites pass; dashboard has 2 HIGH npm vulnerabilities and 50 `.pyc` files remain tracked in git.

### 1. Stale Branches
No stale merged branches. Only `main` exists locally and on `origin`. ✅

### 2. Dependency Health

| Ecosystem | File | Status |
|---|---|---|
| Node / npm | `dashboard/package.json` | ⚠️ 3 vulnerabilities — see below |
| Python (backend) | `backend/pyproject.toml` | ✅ Min-pinned ranges; 17 tests pass |
| Python (sdk) | `sdk/pyproject.toml` | ✅ Min-pinned ranges; 25 tests pass, 1 skipped |

**Dashboard — npm audit results:**

| Severity | Package | Notes |
|---|---|---|
| 🔴 HIGH | `next` | Upgrade to latest patch release |
| 🔴 HIGH | `picomatch` | Transitive dep; `npm audit fix` should resolve |
| 🟡 MODERATE | `brace-expansion` | Transitive dep; `npm audit fix` should resolve |

Run `npm audit fix` in `dashboard/` to address. Review if `--force` is needed for the `next` upgrade.

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

**Minor SDK warning (3rd week):** An atexit `RuntimeError: Call agentlenz.init() before using AgentLenz` surfaces from `EventClient.flush` (`sdk/src/agentlenz/client.py:46`) during test teardown. Guard the flush handler against being called when `init()` was never invoked.

### 5. Git Hygiene

| Check | Status |
|---|---|
| Uncommitted changes | ✅ None |
| Stashes | ✅ None |
| Largest tracked file | ✅ `dashboard/package-lock.json` (242 KB — expected) |
| **Compiled bytecode tracked** | ⚠️ **50 `.pyc` files** still committed — 3rd week open |
| HEAD state | ⚠️ Detached at `refs/heads/main` (checkout artifact) |

**Action required (carry-over — 3rd week):** Run `git rm -r --cached '**/__pycache__/'` to untrack existing bytecode, then commit. A root `.gitignore` was added (commit `7430592`) but `git rm --cached` was never run.

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

**Overall score: Warning** — no new commits since last report; structural issues (no tests, large binaries) remain open.

### 1. Stale Branches
No stale merged branches. Only `main` exists locally and on `origin`. ✅

⚠️ **HEAD is in a detached state** (`HEAD detached at refs/heads/main`) — carry-over from last week.

### 2. Dependency Health
No standard package manifest (`Package.swift`, `package.json`, `requirements.txt`, `pyproject.toml`). Pure Xcode project — dependencies, if any, are managed through Xcode SPM integration.

⚠️ Cannot automatically check for outdated dependencies. Manually verify in Xcode → File → Packages → Update to Latest Package Versions.

### 3. Code Quality — TODO / FIXME / HACK
```
Count: 0 across 104 .swift source files
```
✅ No technical debt markers found.

### 4. Test Status
No `XCTest` target detected and no `swift test`-compatible `Package.swift`. `swift` CLI is not available in this environment.

⚠️ **No tests exist or can be run.** Carry-over — no progress in 3 weeks.

**Recommendation:** Add an `XCTest` target or a GitHub Actions workflow with:
```
xcodebuild test -scheme Dockwright -destination 'platform=macOS'
```

### 5. Git Hygiene

| Check | Status |
|---|---|
| Uncommitted changes | ✅ None |
| Stashes | ✅ None |
| Large binary files in git | ⚠️ ~6.5 MB tracked — see below |

**Large files tracked directly in git (unchanged for 3 weeks):**

| File | Size |
|---|---|
| `assets/demo.mov` | 1.5 MB |
| `Dockwright/Resources/Models/hey_jarvis_v0.1.onnx` | 1.3 MB |
| `Dockwright/Resources/Models/embedding_model.onnx` | 1.3 MB |
| `Dockwright/Resources/Models/melspectrogram.onnx` | 1.1 MB |
| `assets/screenshot-empty.png` | 661 KB |
| `assets/screenshot-chat.png` | 600 KB |
| `assets/demo.mp4` | 89 KB |

Total large binary payload: ~6.5 MB. Consider migrating ONNX models and media assets to Git LFS.

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
| High | 🔴 New | agentlenz | `npm audit fix` in `dashboard/` — 2 HIGH vulns (`next`, `picomatch`) |
| Medium | 🔴 Open (3rd week) | agentlenz | Run `git rm -r --cached '**/__pycache__/'` to untrack 50 `.pyc` files |
| Medium | 🟡 Ongoing | agentlenz | Fix `EventClient.flush` atexit guard in `sdk/src/agentlenz/client.py:46` |
| Medium | 🔴 Open (3rd week) | DockWright-MacOS-Agent | Investigate and fix detached HEAD state |
| Medium | 🔴 Open (3rd week) | DockWright-MacOS-Agent | Add `XCTest` target and CI test run |
| Low | 🔴 Open (3rd week) | DockWright-MacOS-Agent | Migrate ONNX models + `demo.mov` to Git LFS |
| Low | 🔴 Open (2nd week) | agentlenz | Set up CI to run `pytest` per subproject on each push |
