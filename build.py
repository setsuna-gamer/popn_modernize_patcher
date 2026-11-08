#!/usr/bin/env python3
"""実行した OS 向けにビルドして release/ に配布用ファイルを作る。
PyInstaller はクロスコンパイル不可。各 OS 上で実行すること (CI: .github/workflows/build.yml)。

  python build.py
"""
import platform
import shutil
import subprocess
import sys
from pathlib import Path

NAME = "popn_patch_gui"
SRC = "popn_patch_gui.py"
ROOT = Path(__file__).resolve().parent
OUT = ROOT / "release"


def main():
    system = platform.system()  # Windows / Darwin / Linux
    arch = platform.machine().lower()
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    for d in ("build", "dist"):
        shutil.rmtree(ROOT / d, ignore_errors=True)
    OUT.mkdir(exist_ok=True)

    cmd = [sys.executable, "-m", "PyInstaller", "--noconfirm", "--clean",
           "--windowed", "--name", NAME]
    # macOS は .app バンドル (onedir)、他は単一ファイル
    cmd += ["--onedir"] if system == "Darwin" else ["--onefile"]
    subprocess.check_call(cmd + [SRC], cwd=ROOT)

    if system == "Windows":
        dest = OUT / f"{NAME}-windows-{arch}.exe"
        shutil.copy2(ROOT / "dist" / f"{NAME}.exe", dest)
    elif system == "Darwin":
        base = OUT / f"{NAME}-macos-{arch}"
        # ditto は .app のシンボリックリンク/属性を保持する
        subprocess.check_call(["ditto", "-c", "-k", "--keepParent",
                               str(ROOT / "dist" / f"{NAME}.app"), str(base) + ".zip"])
        dest = Path(str(base) + ".zip")
    else:
        dest = OUT / f"{NAME}-linux-{arch}"
        shutil.copy2(ROOT / "dist" / NAME, dest)
        dest.chmod(0o755)
    print("OK:", dest)


if __name__ == "__main__":
    main()
