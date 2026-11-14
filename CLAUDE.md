# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

A Tkinter GUI tool that generates PCSX2 `.pnach` patches for the PS2 *pop'n music* games (7–14 FEVER! / BEST HITS). The user ticks features, enters numeric values, and the tool writes `patches/<serial>_<CRC>.pnach` (and optionally updates `gamesettings/<serial>.ini`). The whole app is a single file, `popn_modernize_patcher.py` (~15k lines, Python 3.8+, **standard library only**, needs tkinter). README.md / README.ja.md hold the user-facing feature list and supported titles; keep both in sync when features change. UI strings are bilingual via `T(ja, en)`; Japanese is the default.

## Commands

```
python popn_modernize_patcher.py             # launch GUI
python popn_modernize_patcher.py --selftest  # integrity tests (the only test suite; also run in CI)
python build.py                              # PyInstaller build -> release/ (must run on each target OS; no cross-compiling)
```

There is no linter and no way to run a single test: `selftest()` is one function of asserts at the end of the file. CI (`.github/workflows/build.yml`) runs selftest then build on Windows/macOS/Linux for `v*` tags and publishes a release.

## Architecture (popn_modernize_patcher.py)

- **`DATA`** (top of file, a giant embedded JSON string): `{ "<SERIAL>_<CRC>": {gametitle, sections:[{id, name, lines}]} }`. Each section is the verbatim pnach code (`patch=` / `//` lines) extracted from existing PCSX2 patches, per title. Section `id` links data to a Feature. `TITLES` maps display name -> `<SERIAL>_<CRC>` key. Adding a title or a patch means editing `DATA` (+ `TITLES`, README table).
- **`Feature` classes** (~line 14533+): a feature `id` matches section ids in `DATA`; `supported(serial)` is true only if the title's data has that section. `Verbatim` emits stored lines unchanged; `CoolWindow`, `KeyBeam`, `LaneBrightness`, `JudgeTiming`, `DefaultChara`, `Barline`, `P480` rewrite specific patch values (via `_sub_value`, which keeps hex width) from GUI parameters. `Verbatim(parent=...)` makes a feature a sub-option enabled only when its parent is on (e.g. `hslabel` under `hispeed`, `skiptitle` under `skipmode`). `FEATURES` is the ordered registry; `order` decides GUI group (`GROUPS`) and output order.
- **pnach/ini handling**: `build_pnach` merges generated sections into any existing pnach (unchecked features' existing sections are kept, others overwritten; section names are mapped back to feature ids by `classify`/`NAME_PREFIX`). Existing files are backed up as `<name>.bak_YYYYMMDDhhmmss` first. `update_ini` / `set_ini_value` edit PCSX2's `gamesettings/*.ini` (`[Patches] Enable = ...`) preserving line endings.
- **Settings/presets**: `popn_modernize_patcher_settings.json` in `APP_DIR` (exe folder when frozen; `~/Library/Application Support/...` for a macOS frozen app), validated by `sanitize_config`. Optional user files next to the program: `features_extra.json` (extra features, `ExtraFeature`) and `characters.json` (extends the built-in `CHARA_TABLES` default-character list).
- **GUI**: `run_gui` / `_run_gui_once` (large, builds the whole Tk UI, language switching restarts via `_run_gui_once`).

## Conventions / gotchas

- Selftest regenerates every supported section with default params and asserts it equals the stored original, so any edit to `DATA` or a Feature's `build` must keep defaults round-tripping (or update the corresponding assertions).
- Output order matters: `hslabel` must come after `hispeed`/`bpm` (asserted in selftest).
- Notes for `skipmode`/`skiptitle` use NBSP instead of spaces on purpose, to avoid ugly Tk wrapping around ASCII in Japanese text.
- Patch features that hook game init (BPM, hispeed label, skip, 480p) don't take effect from save-state loads; notes say the game must be cold-booted.

## Workflow notes (from repo history)

- **Patch data is synced from the maintainer's live PCSX2 `patches/*.pnach`.** Most commits are "Sync X patch with live PCSX2 patch": the `lines` of a `DATA` section are replaced by the updated live code, then the README / feature notes are adjusted. Treat the live pnach as the source of truth; don't invent patch addresses. The `author=` / `comment=` lines inside sections are part of the stored data.
- **Version**: `VERSION` near the top of the file (currently 1.3) is bumped in its own "Bump version to X.Y" commit when a batch of features is released; release tags are `v*` (triggers CI release).
- **Title order** is intentional: 7, BEST HITS, 8, 9, 10–14 (`TITLES`, and the character section order in `CHARA_TABLES`/`CHARA_PATCH` follows 7, BEST HITS, 8, 9).
- **Feature dependencies via `parent`**: sub-options are only selectable while the parent is enabled (hslabel->hispeed, skiptitle->skipmode). The hi-speed label is independent of the BPM display on BEST HITS (no shared hook); selftest asserts this.
- **Per-title differences are expressed as data, not code**: `supported(serial)` decides availability, so a feature that exists only for some titles (e.g. bar line OFF: 8 only; BPM: 7/BEST HITS; perfect: 10-12; freecool/jstep: 13/14; default character: 7/8/9/BEST HITS) just lacks the section for the others. Update the feature `note` and both READMEs when this changes.
- **Skip-to-FREE (`skipmode`)**: UI/notes call the destination "FREE" (not "FREE (TRAINING)"). On BEST HITS it does not skip character/line select, so the note tells users to set SKIP > CHARACTER SELECT and LINE SELECT to OFF in the game's OPTION. Only the UI notes say this; patch lines stay verbatim.
- **Backups**: every write backs up the existing file as `<name>.bak_YYYYMMDDhhmmss` (a new file each time; old ones are never auto-deleted). `backup_path` format is asserted in selftest.
- **Characters**: names are English in uppercase (version codes like `a1`/`c2` keep case); falls back to Japanese when no English name is known. The 2P colour checkbox is disabled for characters with no 2P colour in the ID table (2P = ID+1). Hex ID can be typed directly.
- **GUI text**: any new user-visible string needs both Japanese and English (`T(ja, en)`, or the `FEAT_EN` / `PARAM_EN` / `GROUP_EN` tables for feature names/params/groups). Select-all/clear-all for titles must refresh the preview.
- **Docs**: README.md (English) and README.ja.md (Japanese) mirror each other: feature list, supported-title table (serial / CRC), usage, backup behaviour, "cold boot, not save state" caveat. Update both together.
- Commit messages are short imperative English sentences; git commits in this repo end with the `Co-Authored-By` trailer given by the harness.
- Windows is the primary dev environment (PowerShell/Git Bash); `selftest` and the GUI both run with plain `python`.
