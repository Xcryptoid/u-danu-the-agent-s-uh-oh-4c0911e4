# The entry is one finished word, written ahead of time in entry.txt.
# This file only moves that finished word into the output folder the
# grader points at, so what gets judged is exactly the word on disk.
import os
import shutil


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    shutil.copyfile(src, os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
