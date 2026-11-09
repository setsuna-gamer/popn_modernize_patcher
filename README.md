# popn_modernize_patcher

**English** | [日本語](README.ja.md)

A GUI tool that generates PCSX2 `.pnach` patch files for the PS2 *pop'n music* series
(pop'n music 7–14 FEVER! and BEST HITS). Tick the features you want, set the numeric
values, and the tool writes a `.pnach` file into your PCSX2 `patches` folder.

## Disclaimer (please read)

- **Use at your own risk.** This software is provided "as is", without warranty of any kind.
  The author takes no responsibility for any damage, data loss, save-data corruption,
  emulator trouble, or any other problem resulting from its use.
- **This project is unofficial and has no affiliation with KONAMI or Sony Interactive
  Entertainment in any way.** Do **not** contact them (or their support) about this
  tool. All trademarks and game titles belong to their respective owners.
- **Distribution may end suddenly and without notice.** The repository, releases, and
  download links may be changed or removed at any time.
- This tool does not include any game data, ROM, or ISO. You must own the games and
  provide your own legitimate copies. Do not ask for or share game images.

## Features

Available features depend on the title (some are only offered for certain games):

- HiSpeed extension (x2–x8 / x10 in .5 steps; LOW on some titles)
- Judge timing adjustment
- COOL judge in all modes
- Score formula (current pop'n style)
- No FEVER at gauge MAX
- PERFECT = GOOD 0 and BAD 0
- Key beam length
- Lane brightness
- COOL window 25 ms
- Bar lines OFF
- BPM display on the option screen (7 / BEST HITS)
- 480p test (experimental)
- Default character on the character select screen (7 / 8 / 9 / BEST HITS; pick from a built-in table or type a hex ID; 2P colour optional)

The built-in patch data is based on existing pnach files from the PCSX2 patches folder.
The UI supports Japanese and English, and settings can be saved as presets.

## Supported titles

| Title | Serial / CRC |
|---|---|
| pop'n music 7 | SLPM-65208 / 459970FC |
| pop'n music 8 | SLPM-65316 / 18B64A1A |
| pop'n music 9 | SLPM-65508 / DFBAFDE3 |
| pop'n music 10 | SLPM-65770 / 088871A6 |
| pop'n music 11 | SLPM-66065 / 47F66D02 |
| pop'n music 12 Iroha | SLPM-66314 / 35E0596E |
| pop'n music 13 Carnival | SLPM-66533 / 4BD5C7E6 |
| pop'n music 14 FEVER! | SLPM-66742 / 632DB211 |
| pop'n music BEST HITS | SLPM-62288 / 098E1539 |

## Usage

1. Download the executable for your OS from the Releases page (Windows / macOS / Linux),
   or run from source (Python 3.8+, standard library only, tkinter required):

   ```
   python popn_modernize_patcher.py
   ```

2. Select your PCSX2 data folder (the parent of `patches` and `gamesettings`).
3. Choose the title, tick the features, and enter any numeric values.
4. Press the generate/write button. `patches/<serial>_<CRC>.pnach` is created.
5. In PCSX2, enable patches (Settings → Emulation → Enable Cheats / Patches).

Self-test of the built-in data:

```
python popn_modernize_patcher.py --selftest
```

Optional: `features_extra.json` placed next to the program is loaded as extra feature
definitions.
`characters.json` next to the program adds/overrides the character table:
`{"SLPM-65316_18B64A1A": [{"id": "0x1B", "name": "BAMBOO"}]}`

## Build

PyInstaller cannot cross-compile; run on each target OS (CI: `.github/workflows/build.yml`).

```
python build.py
```

Output goes to `release/`.

## License

Released under the [MIT License](LICENSE). You are free to use, copy, modify, and
redistribute it for any purpose, provided the copyright and license notice are kept.
