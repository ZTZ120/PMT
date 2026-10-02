import argparse
from pathlib import Path

def find_matches(dirpath, suffix='169.xls', recursive=False):
    p = Path(dirpath)
    if not p.exists():
        print(f"目录不存在: {p}")
        return []
    if recursive:
        return sorted([f for f in p.rglob(f"*{suffix}") if f.is_file()])
    else:
        return sorted([f for f in p.iterdir() if f.is_file() and f.name.endswith(suffix)])

def main():
    ap = argparse.ArgumentParser(description="删除目录下以 169.xls 结尾的文件（默认 dry-run）")
    ap.add_argument("dir", nargs="?", default=".", help="目标目录（默认当前目录）")
    ap.add_argument("--suffix", default="169.xls", help="文件后缀/结尾字符串（默认 169.xls）")
    ap.add_argument("--recursive", action="store_true", help="递归查找子目录")
    ap.add_argument("--apply", action="store_true", help="执行删除（默认仅列出）")
    args = ap.parse_args()

    files = find_matches(args.dir, args.suffix, args.recursive)
    if not files:
        print("未找到匹配文件")
        return
    for f in files:
        print(f)
    print("count:", len(files))

    if not args.apply:
        print("dry-run：确认无误后加 --apply 执行删除")
        return

    for f in files:
        try:
            f.unlink()
            print("已删除:", f)
        except Exception as e:
            print("删除失败:", f, e)

if __name__ == "__main__":
    main()