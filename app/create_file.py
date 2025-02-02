import sys, os
from datetime import datetime

def main():
    args = sys.argv[1:]
    dirs = []
    if '-d' in args:
        d_idx = args.index('-d')
        for item in args[d_idx+1:]:
            if item.startswith('-'):
                break
            dirs.append(item)
        if dirs:
            os.makedirs(os.path.join(*dirs), exist_ok=True)

    if '-f' not in args:
        return
    f_idx = args.index('-f')
    filename = None
    if f_idx + 1 < len(args) and not args[f_idx + 1].startswith('-'):
        filename = args[f_idx + 1]
    if not filename:
        return

    if dirs:
        file_path = os.path.join(*dirs, filename)
    else:
        file_path = filename

    lines = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)

    if not lines:
        return

    with open(file_path, "a", encoding="utf-8") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for i, txt in enumerate(lines, start=1):
            f.write(f"{i} {txt}\n")
        f.write("\n")

if __name__ == "__main__":
    main()
