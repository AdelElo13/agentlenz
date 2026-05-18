# Weekly Health Report — 2026-05-18

> Generated automatically. Repos analysed: `agentlenz`, `DockWright-MacOS-Agent`.

---

## agentlenz — ⚠️ Warning

**Overall score: Warning** — backend tests restored this week (17 passed); SDK tests pass; dashboard patch updates still unapplied; 50 bytecode files still tracked in git (6th week open).

### 1. Stale Branches
No stale merged branches. Only `main` exists locally and on `origin`. ✅

### 2. Dependency Health

| Ecosystem | File | Status |
|---|---|---|
| Node / npm | `dashboard/package.json` | ⚠️ Patch updates available — see below |
| Python (backend) | `backend/pyproject.toml` | ⚠️ Cannot verify — deps not installed in env |
| Python (sdk) | `sdk/pyproject.toml` | ⚠️ Cannot verify — deps not installed in env |

**Dashboard — npm outdated (packages not installed locally; version comparisons from registry):**

| Package | Pinned | Latest | Delta |
|---------|--------|--------|-------|
| next | 16.2.1 | 16.2.6 | ⚠️ patch (+5) |
| react | 19.2.4 | 19.2.6 | ⚠️ patch (+2) |
| react-dom | 19.2.4 | 19.2.6 | ⚠️ patch (+2) |
| @tanstack/react-query | ^5.95.1 | 5.100.10 | ⚠️ minor |
| recharts | ^3.8.0 | 3.8.1 | ✅ satisfied |

> `node_modules` not installed — run `npm install` in `dashboard/` before building or auditing.

### 3. Code Quality — TODO / FIXME / HACK
```
Count: 0 across all .py, .ts, .js source files
```
✅ No technical debt markers found.

### 4. Test Status

| Suite | Command | Result |
|---|---|---|
| Backend | `cd backend && python3 -m pytest -q` | ✅ **17 passed** ← restored this week |
| SDK | `cd sdk && python3 -m pytest -q` | ✅ **25 passed, 1 skipped** |
| Dashboard | — | ⚠️ No test suite configured |

**Ongoing SDK warning (6th week):** An atexit `RuntimeError: Call agentlenz.init() before using AgentLenz` surfaces from `EventClient.flush` (`sdk/src/agentlenz/client.py:46`) during test teardown. Guard the flush handler against being called when `init()` was never invoked.

### 5. Git Hygiene

| Check | Status |
|---|---|
| Uncommitted changes | ✅ None |
| Stashes | ✅ None |
| Large tracked files | ✅ None above 1 MB |
| **Compiled bytecode tracked** | ⚠️ 50 `__pycache__/*.pyc` files still committed — 6th week open |

**Action required (carry-over — 6th week):** `.gitignore` already excludes `__pycache__`, but existing files were never untracked. Run:
```bash
git rm -r --cached '**/__pycache__/'
git commit -m "chore: untrack bytecode files"
```

### Recent Activity
```
f2ad0be standup: 2026-05-18
c14149e standup: 2026-05-15
5bfb346 health: weekly report 2026-05-04
6dfe816 health: weekly report 2026-04-27
d0f277c health: weekly report 2026-04-20
```

No feature or fix commits since 2026-04-20. Standup cadence remains active.

---

## DockWright-MacOS-Agent — ⚠️ Warning

**Overall score: Warning** — no new commits since last week; structural issues (no automated tests, large binaries in git) remain open; detached HEAD state in local clone.

### 1. Stale Branches
No stale merged branches. Only `main` exists locally and on `origin`. ✅

Note: local clone is in **detached HEAD** state (`HEAD detached at refs/heads/main`). Not blocking, but worth re-attaching: `git checkout main`.

### 2. Dependency Health
No standard package manifest (`Package.swift`, `package.json`, `requirements.txt`, `pyproject.toml`). Pure Xcode project — dependencies are managed through Xcode's built-in SPM integration.

⚠️ Cannot automatically check for outdated dependencies. Manually verify in **Xcode → File → Packages → Update to Latest Package Versions**.

### 3. Code Quality — TODO / FIXME / HACK
```
Count: 0 across all .swift source files
```
✅ No technical debt markers found.

### 4. Test Status
No `XCTest` target detected. No `swift test`-compatible `Package.swift` present. `swift` CLI unavailable in this Linux environment.

⚠️ **No tests can be run automatically.** Carry-over — no progress in 6 weeks.

**Recommendation:** Add a GitHub Actions macOS workflow:
```yaml
- run: xcodebuild test -scheme Dockwright -destination 'platform=macOS'
```

### 5. Git Hygiene

| Check | Status |
|---|---|
| Uncommitted changes | ✅ None |
| Stashes | ✅ None |
| Large binary files in git | ⚠️ ~4.8 MB tracked — unchanged since first report |

**Large files tracked directly in git (6 weeks open):**

| File | Size |
|---|---|
| `assets/demo.mov` | 1.5 MB |
| `Dockwright/Resources/Models/hey_jarvis_v0.1.onnx` | 1.3 MB |
| `Dockwright/Resources/Models/embedding_model.onnx` | 1.3 MB |
| `Dockwright/Resources/Models/melspectrogram.onnx` | 1.1 MB |
| `assets/screenshot-empty.png` | 664 KB |
| `assets/screenshot-chat.png` | 600 KB |

Consider migrating ONNX models and media assets to Git LFS.

### Recent Activity
```
d6d3f3f chore: update UIAutomationTool
645d4ab fix: UI automation element search, Unicode typing, and threading
928f649 feat: whitelist safe sudo commands (pmset, systemsetup, defaults, etc.)
358b8d9 docs: simplify sudo instructions for non-devs
0837d7b docs: add optional sudo setup for system control
```

⚠️ No new commits since at least 2026-05-04 (last health report). Development appears paused.

---

## Action Items Summary

| Priority | Status | Repo | Action |
|---|---|---|---|
| High | ⚠️ Open (3rd week) | agentlenz | `npm install && npm update` in `dashboard/` — patch updates for `next`, `react`, `react-dom` and minor for `@tanstack/react-query` |
| Medium | 🔴 Open (6th week) | agentlenz | Run `git rm -r --cached '**/__pycache__/'` to untrack 50 bytecode files |
| Medium | 🟡 Ongoing (6th week) | agentlenz | Fix `EventClient.flush` atexit guard in `sdk/src/agentlenz/client.py:46` |
| Medium | 🔴 Open (6th week) | DockWright-MacOS-Agent | Add `XCTest` target and CI test run via `xcodebuild test` |
| Low | 🔴 Open (6th week) | DockWright-MacOS-Agent | Migrate ONNX models + `demo.mov` to Git LFS |
| Low | New | DockWright-MacOS-Agent | Reattach HEAD: `git checkout main` |
| Low | 🔴 Open (4th week) | agentlenz | Set up CI to run `pytest` per subproject on each push |
