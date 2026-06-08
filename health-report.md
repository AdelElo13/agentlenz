# Weekly Health Report — 2026-06-08

> Generated automatically. Repos analysed: `agentlenz`, `DockWright-MacOS-Agent`.

---

## agentlenz — ⚠️ Warning

**Overall score: Warning** — all tests pass; new stale remote branch detected; dashboard dependency updates still unapplied (6th week); bytecode files still tracked in git (9th week open); atexit warning persists (9th week).

### 1. Stale Branches

| Branch | Status |
|---|---|
| `standup-2026-05-27` (remote only) | ⚠️ **New this week** — remote branch not present locally, appears to be an unmerged standup divergence |

**Action:** Delete the stale remote branch:
```bash
git push origin --delete standup-2026-05-27
```

### 2. Dependency Health

| Ecosystem | File | Status |
|---|---|---|
| Python (sdk) | `sdk/pyproject.toml` | ⚠️ `pydantic_core 2.46.4` → latest `2.47.0` (patch update available) |
| Python (backend) | `backend/pyproject.toml` | ✅ All constraints satisfied — fastapi, uvicorn, sqlalchemy, alembic all current |
| Node / npm | `dashboard/package.json` | ⚠️ Patch/minor updates available — 6th week unapplied |

**Dashboard pinned versions (carry-over wk 6):**

| Package | Pinned | Latest | Status |
|---------|--------|--------|--------|
| `next` | 16.2.1 | 16.2.7 | ⚠️ patch update — unchanged since wk 1 |
| `react` | 19.2.4 | 19.2.7 | ⚠️ patch update — unchanged since wk 1 |
| `react-dom` | 19.2.4 | 19.2.7 | ⚠️ patch update — unchanged since wk 1 |
| `@tanstack/react-query` | ^5.95.1 | 5.101.0 | ⚠️ minor update available |
| `recharts` | ^3.8.0 | 3.8.1 | ✅ satisfied |

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
| Backend | `cd backend && python3 -m pytest -q` | ✅ **17 passed** (0.44s) |
| Dashboard | unit tests | ⚠️ No test suite configured in `package.json` (9th week) |

**Ongoing SDK atexit warning (9th week):** `RuntimeError: Call agentlenz.init() before using AgentLenz` fires from `EventClient.flush` at `sdk/src/agentlenz/client.py:46` during test teardown. Add an init-check guard before attempting flush.

### 5. Git Hygiene

| Check | Status |
|---|---|
| Uncommitted changes | ✅ None |
| Stashes | ✅ None |
| Large tracked files | ✅ Only `dashboard/package-lock.json` (240 KB) — expected |
| Compiled bytecode tracked | ⚠️ `__pycache__/*.pyc` files committed — **9th week open** |
| Unpushed commits | ✅ None — HEAD is current with `origin/main` |

**Action required (carry-over — 9th week):** Remove committed `__pycache__` files:
```bash
git rm -r --cached '**/__pycache__/'
git commit -m "chore: untrack bytecode files"
```

### Recent Activity
```
b915563 standup: 2026-06-08   ← HEAD
14aee97 standup: 2026-06-05
f96429f standup: 2026-06-04
c6a512c standup: 2026-06-03
a959f60 standup: 2026-06-02
```

Standup cadence is active. No feature or fix commits in 7+ weeks.

---

## DockWright-MacOS-Agent — ⚠️ Warning

**Overall score: Warning** — dormant for 9 weeks (last commit ~2026-04-06); no automated tests runnable from CLI; large binaries tracked in git still unaddressed (9th week).

### 1. Stale Branches

No stale merged branches. Only `main` exists locally and on `origin`. ✅

> HEAD is detached at `refs/heads/main` — same commit as `origin/main` (`d6d3f3f`).

### 2. Dependency Health

No standard package manifest (`Package.swift`, `package.json`, `requirements.txt`, `pyproject.toml`) at repo root. Pure Xcode project (`.xcodeproj`) — dependencies managed through Xcode's SPM integration.

⚠️ Cannot audit from CLI. Manually verify in **Xcode → File → Packages → Update to Latest Package Versions**.

### 3. Code Quality — TODO / FIXME / HACK

```
Count: 0 across all .swift source files
```
✅ No technical debt markers found.

### 4. Test Status

No `XCTest` target detectable from CLI. No `swift test`-compatible `Package.swift` present. `xcodebuild` unavailable in this Linux environment.

⚠️ **No tests can be run automatically** — 9th week with no progress on this.

**Recommendation:** Add a GitHub Actions macOS workflow:
```yaml
- run: xcodebuild test -scheme Dockwright -destination 'platform=macOS'
```

### 5. Git Hygiene

| Check | Status |
|---|---|
| Uncommitted changes | ✅ None |
| Stashes | ✅ None |
| Large binary files in git | ⚠️ ~4.8 MB tracked — **9th week open** |

**Large files tracked directly in git:**

| File | Size |
|---|---|
| `assets/demo.mov` | 1.5 MB |
| `Dockwright/Resources/Models/hey_jarvis_v0.1.onnx` | 1.3 MB |
| `Dockwright/Resources/Models/embedding_model.onnx` | 1.3 MB |
| `Dockwright/Resources/Models/melspectrogram.onnx` | 1.1 MB |
| `assets/screenshot-empty.png` | 659 KB |
| `assets/screenshot-chat.png` | 599 KB |

These inflate clone size and git history. Migrate to Git LFS: `git lfs track "*.onnx" "*.mov"`.

### Recent Activity
```
d6d3f3f chore: update UIAutomationTool
645d4ab fix: UI automation element search, Unicode typing, and threading
928f649 feat: whitelist safe sudo commands
358b8d9 docs: simplify sudo instructions for non-devs
0837d7b docs: add optional sudo setup for system control
```

Last commit: **~2026-04-06** — 9 weeks without activity. Consider archiving or planning a maintenance sprint.

---

## Action Items Summary

| Priority | Age | Repo | Action |
|---|---|---|---|
| **High** | new | agentlenz | Delete stale remote branch: `git push origin --delete standup-2026-05-27` |
| **High** | wk 6 | agentlenz | `npm install && npm update` in `dashboard/` — bump next, react, react-dom, @tanstack/react-query |
| Medium | wk 9 | agentlenz | `git rm -r --cached '**/__pycache__/'` — untrack committed bytecode files |
| Medium | wk 9 | agentlenz | Fix `EventClient.flush` atexit guard — `sdk/src/agentlenz/client.py:46` |
| Medium | wk 9 | agentlenz | Add dashboard unit test suite (e.g. Vitest) |
| Medium | wk 9 | DockWright-MacOS-Agent | Add `XCTest` target + GitHub Actions macOS `xcodebuild test` workflow |
| Low | wk 9 | DockWright-MacOS-Agent | Migrate ONNX models + `demo.mov` to Git LFS (`git lfs track "*.onnx" "*.mov"`) |
