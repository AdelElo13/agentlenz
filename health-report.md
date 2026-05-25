# Weekly Health Report — 2026-05-25

> Generated automatically. Repos analysed: `agentlenz`, `DockWright-MacOS-Agent`.

---

## agentlenz — ⚠️ Warning

**Overall score: Warning** — all tests pass; dashboard patch updates still unapplied (4th week); 50 bytecode files still tracked in git (7th week open); no feature/fix commits in 5+ weeks.

### 1. Stale Branches
No stale merged branches. Only `main` exists locally and on `origin`. ✅

### 2. Dependency Health

| Ecosystem | File | Status |
|---|---|---|
| Python (sdk) | `sdk/pyproject.toml` | ✅ All deps satisfied — httpx 0.28.1, pydantic 2.13.4, anthropic 0.104.1, openai 2.38.0 |
| Python (backend) | `backend/pyproject.toml` | ✅ Installed and tests pass |
| Node / npm | `dashboard/package.json` | ⚠️ Patch/minor updates available — see below |

**Dashboard — npm outdated (`node_modules` not installed in this env; comparisons from registry):**

| Package | Pinned | Latest | Delta |
|---------|--------|--------|-------|
| next | 16.2.1 | 16.2.6 | ⚠️ patch (+5) — carry-over wk 4 |
| react | 19.2.4 | 19.2.6 | ⚠️ patch (+2) — carry-over wk 4 |
| react-dom | 19.2.4 | 19.2.6 | ⚠️ patch (+2) — carry-over wk 4 |
| @tanstack/react-query | ^5.95.1 | 5.100.14 | ⚠️ minor (was 5.100.10 last week) |
| recharts | ^3.8.0 | 3.8.1 | ✅ satisfied |

> Run `npm install && npm update` inside `dashboard/` to apply.

### 3. Code Quality — TODO / FIXME / HACK
```
Count: 0 across all .py, .ts, .js, .swift source files
```
✅ No technical debt markers found.

### 4. Test Status

| Suite | Command | Result |
|---|---|---|
| SDK | `cd sdk && python3 -m pytest -q` | ✅ **25 passed, 1 skipped** |
| Backend | `cd backend && python3 -m pytest -q` | ✅ **17 passed** |
| Dashboard | — | ⚠️ No test suite configured in `package.json` |

**Ongoing SDK atexit warning (7th week):** `RuntimeError: Call agentlenz.init() before using AgentLenz` fires from `EventClient.flush` at `sdk/src/agentlenz/client.py:46` during test teardown. Add a guard: check that config is initialized before attempting flush.

### 5. Git Hygiene

| Check | Status |
|---|---|
| Uncommitted changes | ✅ None |
| Stashes | ✅ None |
| Large tracked files | ✅ No single file above 1 MB |
| Compiled bytecode tracked | ⚠️ `__pycache__/*.pyc` files committed — 7th week open |

**Action required (carry-over — 7th week):** `.gitignore` already excludes `__pycache__`, but existing cached files were never removed from the index. Fix:
```bash
git rm -r --cached '**/__pycache__/'
git commit -m "chore: untrack bytecode files"
```

### Recent Activity
```
d166d36 standup: 2026-05-25
16675e9 standup: 2026-05-22
895c782 standup: 2026-05-21
6200426 standup: 2026-05-20
1432e3b standup: 2026-05-19
```

No feature or fix commits for 5+ weeks. Standup cadence is active but repo shows no forward progress.

---

## DockWright-MacOS-Agent — ⚠️ Warning

**Overall score: Warning** — dormant for 7 weeks (last commit 2026-04-06); no automated tests runnable from CLI; large binaries tracked in git remain unaddressed.

### 1. Stale Branches
No stale merged branches. Only `main` exists locally and on `origin`. ✅

### 2. Dependency Health
No standard package manifest (`Package.swift`, `package.json`, `requirements.txt`, `pyproject.toml`) present. Pure Xcode project (`.xcodeproj`) — dependencies managed through Xcode's SPM integration.

⚠️ Cannot audit from CLI. Manually verify in **Xcode → File → Packages → Update to Latest Package Versions**.

### 3. Code Quality — TODO / FIXME / HACK
```
Count: 0 across all 104 .swift source files
```
✅ No technical debt markers found.

### 4. Test Status
No `XCTest` target detectable from CLI. No `swift test`-compatible `Package.swift` present. `swift` / `xcodebuild` unavailable in this Linux environment.

⚠️ **No tests can be run automatically.** Carry-over — no progress in 7 weeks.

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

**Large files tracked directly in git (7 weeks open):**

| File | Size |
|---|---|
| `assets/demo.mov` | 1.5 MB |
| `Dockwright/Resources/Models/hey_jarvis_v0.1.onnx` | 1.3 MB |
| `Dockwright/Resources/Models/embedding_model.onnx` | 1.3 MB |
| `Dockwright/Resources/Models/melspectrogram.onnx` | 1.1 MB |
| `assets/screenshot-empty.png` | 664 KB |
| `assets/screenshot-chat.png` | 600 KB |

These inflate clone size and git history. Migrate to Git LFS: `git lfs track "*.onnx" "*.mov"`.

### Recent Activity
```
d6d3f3f chore: update UIAutomationTool
645d4ab fix: UI automation element search, Unicode typing, and threading
928f649 feat: whitelist safe sudo commands (pmset, systemsetup, defaults, etc.)
358b8d9 docs: simplify sudo instructions for non-devs
0837d7b docs: add optional sudo setup for system control
```

Last commit: **2026-04-06** — 7 weeks without activity. Consider archiving or picking back up.

---

## Action Items Summary

| Priority | Age | Repo | Action |
|---|---|---|---|
| High | wk 4 | agentlenz | `npm install && npm update` in `dashboard/` — bump next, react, react-dom, @tanstack/react-query |
| Medium | wk 7 | agentlenz | `git rm -r --cached '**/__pycache__/'` — untrack committed bytecode files |
| Medium | wk 7 | agentlenz | Fix `EventClient.flush` atexit guard — `sdk/src/agentlenz/client.py:46` |
| Medium | wk 7 | agentlenz | Set up CI to run `pytest` per subproject on each push |
| Medium | wk 7 | DockWright-MacOS-Agent | Add `XCTest` target + GitHub Actions macOS `xcodebuild test` workflow |
| Low | wk 7 | DockWright-MacOS-Agent | Migrate ONNX models + `demo.mov` to Git LFS (`git lfs track "*.onnx" "*.mov"`) |
