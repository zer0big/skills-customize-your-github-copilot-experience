"""Starter code for Python Text Processing assignment.

Usage examples:
    python assignments/python-text-processing/starter-code.py sample.txt --top 5
    python assignments/python-text-processing/starter-code.py sample.txt --replace old new --out replaced.txt

"""

import sys
from collections import Counter
from pathlib import Path
import argparse
import re


def read_text_file(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return path.read_text(encoding='utf-8')


def count_lines(text: str) -> int:
    return text.count('\n') + (0 if text.endswith('\n') or text == '' else 1)


def tokenize(text: str):
    # lower-case, remove punctuation
    words = re.findall(r"\b[\w']+\b", text.lower())
    return words


def top_n_words(text: str, n: int = 10):
    words = tokenize(text)
    return Counter(words).most_common(n)


def replace_word(text: str, old: str, new: str) -> str:
    # simple whole-word replace (case-sensitive behavior noted)
    pattern = re.compile(rf"\b{re.escape(old)}\b")
    return pattern.sub(new, text)


def write_text_file(path: Path, text: str):
    path.write_text(text, encoding='utf-8')


def main(argv=None):
    parser = argparse.ArgumentParser(description='Python Text Processing starter')
    parser.add_argument('file', help='Path to text file')
    parser.add_argument('--top', type=int, default=10, help='Show top N words')
    parser.add_argument('--replace', nargs=2, metavar=('OLD', 'NEW'), help='Replace OLD with NEW')
    parser.add_argument('--out', help='Output file for replace result')
    args = parser.parse_args(argv)

    path = Path(args.file)
    try:
        text = read_text_file(path)
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        return 1

    lines = count_lines(text)
    words = tokenize(text)
    print(f"Lines: {lines}")
    print(f"Words: {len(words)}")

    print(f"Top {args.top} words:")
    for word, cnt in top_n_words(text, args.top):
        print(f"  {word}: {cnt}")

    if args.replace:
        old, new = args.replace
        replaced = replace_word(text, old, new)
        out_path = Path(args.out) if args.out else path.with_name(path.stem + "_replaced" + path.suffix)
        write_text_file(out_path, replaced)
        print(f"Replaced and wrote output to: {out_path}")

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
