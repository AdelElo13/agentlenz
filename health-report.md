# Weekly Health Report — 2026-06-22

> Generated automatically. Repos analysed: `agentlenz`, `DockWright-MacOS-Agent`.

---

## agentlenz — ⚠️ Warning

**Overall score: Warning** — no stale branches this week; dashboard dependencies not installed (npm packages all MISSING); 50 compiled bytecode files still tracked in git (10th week carry-over); test suite cannot run (pytest not installed in environment); no test suite for dashboard.

### 1. Stale Branches

| Branch | Status |
|---|---|
| None found | ✅ |

`git branch -a --merged main` returns only `main` and `remotes/origin/main`. Previous week's stale branch (`standup-2026-05-27`) appears to have been removed. ✅

> ⚠️ HEAD is detached from `refs/heads/main` — same commit as `origin/main`. Not a blocker but unusual for a cloned repo.

### 2. Dependency Health

| Ecosystem | File | Status |
|---|---|---|
| Python (sdk) | `sdk/pyproject.toml` | ⚠️ Cannot verify — `pip`/packages not installed in environment |
| Python (backend) | `backend/pyproject.toml` | ⚠️ Cannot verify — `pip`/packages not installed in environment |
| Node / npm | `dashboard/package.json` | ⚠️ All packages MISSING (node_modules not installed) — outdated versions confirmed |

**Dashboard pinned versions (carry-over — 7th week unapplied):**

| Package | Pinned | Latest | Status |
|---------|--------|--------|--------|
| `next` | 16.2.1 | 16.2.9 | ⚠️ patch update available |
| `react` | 19.2.4 | 19.2.7 | ⚠️ patch update available |
| `react-dom` | 19.2.4 | 19.2.7 | ⚠️ patch update available |
| `@tanstack/react-query` | ^5.95.1 | 5.101.0 | ⚠️ minor update available |
| `recharts` | ^3.8.0 | 3.8.1 | ✅ satisfied |
| `npm` itself | 10.9.7 | 11.17.0 | ⚠️ major update available |

> Run `cd dashboard && npm install && npm update` to apply. Also consider `npm install -g npm@11.17.0`.

**SDK declared dependencies** (versions unverified, packages not installed):
- `httpx>=0.27`, `pydantic>=2.0`
- Optional: `anthropic>=0.40`, `openai>=1.50`

**Backend declared dependencies** (versions unverified):
- `fastapi>=0.115`, `uvicorn[standard]>=0.32`, `sqlalchemy[asyncio]>=2.0`, `asyncpg>=0.30`, `alembic>=1.14`, `pydantic>=2.0`, `pydantic-settings>=2.0`, `psycopg2-binary>=2.9`

### 3. Code Quality — TODO / FIXME / HACK

```
Count: 0 across all .py, .ts, .js, .tsx source files
```
✅ No technical debt markers found.

### 4. Test Status

| Suite | Command | Result |
|---|---|---|
| SDK | `cd sdk && python3 -m pytest -q` | ❌ Cannot run — `No module named pytest` |
| Backend | `cd backend && python3 -m pytest -q` | ❌ Cannot run — `No module named pytest` |
| Dashboard | — | ⚠️ No `test` script in `package.json` (10th week) |

> Packages need to be installed before tests can run. Recommend adding a CI step that runs `pip install -e sdk[dev] && pytest` and `pip install -e backend[dev] && pytest`.

### 5. Git Hygiene

| Check | Status |
|---|---|
| Uncommitted changes | ✅ None |
| Stashes | ✅ None |
| Large tracked files | ✅ Only `dashboard/package-lock.json` (240 KB) — expected |
| Compiled bytecode tracked | ⚠️ 50 `__pycache__/*.pyc` files committed — **10th week open** |
| Unpushed commits | ✅ None |

> `.gitignore` already contains `**/__pycache__/` and `**/*.pyc` — these files were committed before the rule was added and must be explicitly removed from the index.

**Action required (carry-over — 10th week):**
```bash
git rm -r --cached '**/__pycache__/' '**/*.pyc'
git commit -m "chore: untrack committed bytecode files"
```

### Recent Activity
```
d756937 standup: 2026-06-19   ← HEAD (3 days ago)
7ad8ad6 standup: 2026-06-18
00b76c5 standup: 2026-06-12
dd240c5 standup: 2026-06-11
47c7389 standup: 2026-06-10
f6a4009 standup: 2026-06-09
f3085ce health: weekly report 2026-06-08
b915563 standup: 2026-06-08
```

Standup cadence is active. No feature/fix commits visible in recent history.

---

## DockWright-MacOS-Agent — ⚠️ Warning

**Overall score: Warning** — dormant for ~11 weeks (last commit 2026-04-06); large binary assets committed to git (~5 MB); no automated tests; no SPM dependency manifest to audit.

### 1. Stale Branches

No stale merged branches. Only `main` exists locally and on `origin`. ✅

> ⚠️ HEAD is detached at `refs/heads/main` — same commit as `origin/main` (`d6d3f3f`). Not a blocker.

### 2. Dependency Health

No standard package manifest (`Package.swift`, `package.json`, `requirements.txt`, `pyproject.toml`) found. Pure Xcode project — Swift Package Manager dependencies managed inside `.xcodeproj`.

**104 Swift source files** across the project.

⚠️ Cannot audit from CLI. Manually verify in **Xcode → File → Packages → Update to Latest Package Versions**.

### 3. Code Quality — TODO / FIXME / HACK

```
Count: 0 across all 104 .swift source files
```
✅ No technical debt markers found.

### 4. Test Status

No `XCTest` target detectable from CLI. No `swift test`-compatible `Package.swift`. `xcodebuild` unavailable in this Linux container.

⚠️ **No tests can be run automatically** — 10th week with no CI coverage.

**Recommendation:** Add a GitHub Actions macOS workflow:
```yaml
- uses: actions/checkout@v4
- run: xcodebuild test -scheme Dockwright -destination 'platform=macOS'
```

### 5. Git Hygiene

| Check | Status |
|---|---|
| Uncommitted changes | ✅ None |
| Stashes | ✅ None |
| Large binary files in git | ⚠️ ~5 MB tracked — **10th week open** |

**Large files tracked directly in git:**

| File | Size |
|---|---|
| `assets/demo.mov` | 1.5 MB |
| `Dockwright/Resources/Models/hey_jarvis_v0.1.onnx` | 1.3 MB |
| `Dockwright/Resources/Models/embedding_model.onnx` | 1.3 MB |
| `Dockwright/Resources/Models/melspectrogram.onnx` | 1.1 MB |
| `assets/screenshot-empty.png` | 664 KB |
| `assets/screenshot-chat.png` | 600 KB |
| `assets/demo.mp4` | 92 KB |

Total tracked binary bloat: ~6.6 MB. Migrate to Git LFS:
```bash
git lfs install
git lfs track "*.onnx" "*.mov" "*.mp4"
git add .gitattributes
```

### Recent Activity
```
d6d3f3f chore: update UIAutomationTool   ← HEAD (~11 weeks ago)
645d4ab fix: UI automation element search, Unicode typing, and threading
928f649 feat: whitelist safe sudo commands
358b8d9 docs: simplify sudo instructions for non-devs
0837d7b docs: add optional sudo setup for system control
```

Last commit: **2026-04-06** — 11 weeks without activity. Consider planning a maintenance sprint or archiving if no longer active.

---

## Action Items Summary

| Priority | Age | Repo | Action |
|---|---|---|---|
| **High** | wk 7 | agentlenz | `cd dashboard && npm install && npm update` — bump next (→16.2.9), react/react-dom (→19.2.7), @tanstack/react-query (→5.101.0) |
| **High** | wk 10 | agentlenz | `git rm -r --cached '**/__pycache__/'` — untrack 50 committed bytecode files |
| Medium | — | agentlenz | Install dev dependencies in CI (`pip install -e sdk[dev] && pytest`) so tests can run |
| Medium | wk 10 | agentlenz | Add dashboard unit test suite (e.g. Vitest or Jest) |
| Medium | wk 10 | DockWright-MacOS-Agent | Add `XCTest` target + GitHub Actions macOS `xcodebuild test` workflow |
| Low | wk 10 | DockWright-MacOS-Agent | Migrate ONNX models + video assets to Git LFS (saves ~6 MB clone weight) |
| Low | — | DockWright-MacOS-Agent | Consider maintenance sprint or archival — 11 weeks dormant |
