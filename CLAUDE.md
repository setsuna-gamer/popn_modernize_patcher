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
