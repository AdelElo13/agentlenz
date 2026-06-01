# Weekly Health Report — 2026-06-01

> Generated automatically. Repos analysed: `agentlenz`, `DockWright-MacOS-Agent`.

---

## agentlenz — ⚠️ Warning

**Overall score: Warning** — all tests pass; dashboard dependency updates still unapplied (5th week); bytecode files still tracked in git (8th week open); no feature/fix commits in 6+ weeks.

### 1. Stale Branches
No stale merged branches. Only `main` exists locally and on `origin`. ✅

> **Note:** Local HEAD is detached and 1 commit ahead of `origin/main` (standup commit `0ec59e6` not yet pushed).

### 2. Dependency Health

| Ecosystem | File | Status |
|---|---|---|
| Python (sdk) | `sdk/pyproject.toml` | ✅ All minimum constraints satisfied — httpx 0.28.1, pydantic 2.13.4 |
| Python (backend) | `backend/pyproject.toml` | ✅ All constraints satisfied — fastapi 0.136.3, uvicorn 0.48.0, sqlalchemy 2.0.50, alembic 1.18.4 |
| Node / npm | `dashboard/package.json` | ⚠️ Patch/minor updates available — 5th week unapplied |

> SDK optional extras (`anthropic`, `openai`) are not installed in this CI environment — install with `pip install "agentlenz[anthropic,openai]"` locally.

**Dashboard pinned versions (carry-over wk 5):**

| Package | Pinned | Status |
|---------|--------|--------|
| next | 16.2.1 | ⚠️ patch updates available — unchanged since wk 1 |
| react | 19.2.4 | ⚠️ patch updates available — unchanged since wk 1 |
| react-dom | 19.2.4 | ⚠️ patch updates available — unchanged since wk 1 |
| @tanstack/react-query | ^5.95.1 | ⚠️ minor updates available |
| recharts | ^3.8.0 | ✅ satisfied |

> Run `npm install && npm update` inside `dashboard/` to apply.

### 3. Code Quality — TODO / FIXME / HACK
```
Count: 0 across all .py, .ts, .js, .tsx source files
```
✅ No technical debt markers found.

### 4. Test Status

| Suite | Command | Result |
|---|---|---|
| SDK | `cd sdk && python3 -m pytest -q` | ✅ **25 passed, 1 skipped** (0.09s) |
| Backend | `cd backend && python3 -m pytest -q` | ✅ **17 passed** (0.46s) |
| Dashboard | `npm run build` | ✅ **Build succeeded** — 6 static routes generated |
| Dashboard | `npm run lint` | ✅ **No ESLint errors** |
| Dashboard | unit tests | ⚠️ No test suite configured in `package.json` |

**Ongoing SDK atexit warning (8th week):** `RuntimeError: Call agentlenz.init() before using AgentLenz` fires from `EventClient.flush` at `sdk/src/agentlenz/client.py:46` during test teardown. Add an init-check guard before attempting flush.

### 5. Git Hygiene

| Check | Status |
|---|---|
| Uncommitted changes | ✅ None |
| Stashes | ✅ None |
| Large tracked files | ✅ Only `dashboard/package-lock.json` (240 KB) — expected |
| Compiled bytecode tracked | ⚠️ `__pycache__/*.pyc` files committed — 8th week open |
| Unpushed commits | ⚠️ 1 commit (`standup: 2026-06-01`) not yet on `origin/main` |

**Action required (carry-over — 8th week):** Remove committed `__pycache__` files:
```bash
git rm -r --cached '**/__pycache__/'
git commit -m "chore: untrack bytecode files"
```

### Recent Activity
```
0ec59e6 standup: 2026-06-01   ← HEAD (not yet pushed)
c03540d standup: 2026-05-29
d6f5b53 standup: 2026-05-26
d166d36 standup: 2026-05-25
16675e9 standup: 2026-05-22
```

Standup cadence is active but no feature or fix commits for 6+ weeks.

---

## DockWright-MacOS-Agent — ⚠️ Warning

**Overall score: Warning** — dormant for 8 weeks (last commit 2026-04-06); no automated tests runnable from CLI; large binaries tracked in git still unaddressed.

### 1. Stale Branches
No stale merged branches. Only `main` exists locally and on `origin`. ✅

> HEAD is detached at `refs/heads/main` — same commit as `origin/main` (`d6d3f3f`).

### 2. Dependency Health
No standard package manifest (`Package.swift`, `package.json`, `requirements.txt`, `pyproject.toml`) at repo root. Pure Xcode project (`.xcodeproj`) — dependencies managed through Xcode's SPM integration.

⚠️ Cannot audit from CLI. Manually verify in **Xcode → File → Packages → Update to Latest Package Versions**.

### 3. Code Quality — TODO / FIXME / HACK
```
Count: 0 across all 104 .swift source files
```
✅ No technical debt markers found.

### 4. Test Status
No `XCTest` target detectable from CLI. No `swift test`-compatible `Package.swift` present. `swift` / `xcodebuild` unavailable in this Linux environment.

⚠️ **No tests can be run automatically.** 8th week with no progress on this.

**Recommendation:** Add a GitHub Actions macOS workflow:
```yaml
- run: xcodebuild test -scheme Dockwright -destination 'platform=macOS'
```

### 5. Git Hygiene

| Check | Status |
|---|---|
| Uncommitted changes | ✅ None |
| Stashes | ✅ None |
| Large binary files in git | ⚠️ ~4.8 MB tracked — 8 weeks open |

**Large files tracked directly in git:**

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
928f649 feat: whitelist safe sudo commands
358b8d9 docs: simplify sudo instructions for non-devs
0837d7b docs: add optional sudo setup for system control
```

Last commit: **2026-04-06** — 8 weeks without activity. Consider archiving or planning a maintenance sprint.

---

## Action Items Summary

| Priority | Age | Repo | Action |
|---|---|---|---|
| High | wk 5 | agentlenz | `npm install && npm update` in `dashboard/` — bump next, react, react-dom, @tanstack/react-query |
| Medium | wk 8 | agentlenz | `git rm -r --cached '**/__pycache__/'` — untrack committed bytecode files |
| Medium | wk 8 | agentlenz | Fix `EventClient.flush` atexit guard — `sdk/src/agentlenz/client.py:46` |
| Medium | wk 8 | agentlenz | Add dashboard unit test suite (e.g. Vitest) |
| Medium | wk 8 | agentlenz | Push unpushed standup commit to `origin/main` |
| Medium | wk 8 | DockWright-MacOS-Agent | Add `XCTest` target + GitHub Actions macOS `xcodebuild test` workflow |
| Low | wk 8 | DockWright-MacOS-Agent | Migrate ONNX models + `demo.mov` to Git LFS (`git lfs track "*.onnx" "*.mov"`) |
