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

NAME = "popn_modernize_patcher"
SRC = "popn_modernize_patcher.py"
ROOT = Path(__file__).resolve().parent
OUT = ROOT / "release"
DOCS = ["LICENSE", "README.md", "README.ja.md"]


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

    # 配布物は <NAME>-<os>-<arch>/ フォルダにバイナリ + LICENSE + README をまとめて圧縮する
    plat = {"Windows": "windows", "Darwin": "macos"}.get(system, "linux")
    base = f"{NAME}-{plat}-{arch}"
    stage = ROOT / "build" / "stage" / base
    shutil.rmtree(stage.parent, ignore_errors=True)
    stage.mkdir(parents=True)
    if system == "Windows":
        shutil.copy2(ROOT / "dist" / f"{NAME}.exe", stage)
    elif system == "Darwin":
        # .app のシンボリックリンク/属性を保持するため copytree(symlinks=True)
        shutil.copytree(ROOT / "dist" / f"{NAME}.app", stage / f"{NAME}.app", symlinks=True)
    else:
        shutil.copy2(ROOT / "dist" / NAME, stage / NAME)
        (stage / NAME).chmod(0o755)
    for doc in DOCS:
        shutil.copy2(ROOT / doc, stage)

    if system == "Darwin":
        # ditto は .app のシンボリックリンク/属性を保持する
        dest = OUT / f"{base}.zip"
        subprocess.check_call(["ditto", "-c", "-k", "--keepParent", str(stage), str(dest)])
    elif system == "Windows":
        dest = Path(shutil.make_archive(str(OUT / base), "zip", stage.parent, base))
    else:
        # tar.gz は実行権限を保持する
        dest = Path(shutil.make_archive(str(OUT / base), "gztar", stage.parent, base))
    print("OK:", dest)


if __name__ == "__main__":
    main()
