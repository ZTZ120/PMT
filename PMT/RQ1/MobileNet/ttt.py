import os
import re
import argparse
from pathlib import Path

def rename_files(folder: Path, start: int = 30, step: int = 2, pattern=r'(.*?)(\d+)$'):
    files = sorted([p for p in folder.iterdir() if p.is_file() and p.suffix == '.py' and p.name != Path(__file__).name])
    if not files:
        print("no .py files")
        return
    # prepare target numbers
    nums = [start + i * step for i in range(len(files))]
    tmp_names = []
    # phase 1: move to temp names to avoid conflicts
    for i, p in enumerate(files):
        tmp = folder / f"__tmp_rename_{i}__.py"
        p.rename(tmp)
        tmp_names.append((tmp, p))
    # phase 2: final names
    for (tmp, orig), num in zip(tmp_names, nums):
        stem = orig.stem
        m = re.match(pattern, stem)
        if m:
            base = m.group(1)
            # preserve digit width
            width = len(m.group(2))
            new_stem = f"{base}{str(num).zfill(width)}"
        else:
            new_stem = f"{stem}_{num}"
        new_name = folder / f"{new_stem}.py"
        # if target exists, append suffix
        if new_name.exists():
            new_name = folder / f"{new_stem}_renamed.py"
        tmp.rename(new_name)
        print(f"{orig.name} -> {new_name.name}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="将文件夹下的 .py 文件名末尾数字从 start 开始每个 -step")
    ap.add_argument("folder", nargs='?', default=".", help="目标文件夹")
    ap.add_argument("--start", type=int, default=30)
    ap.add_argument("--step", type=int, default=2)
    args = ap.parse_args()
    rename_files(Path(args.folder).expanduser().resolve(), start=args.start, step=args.step)