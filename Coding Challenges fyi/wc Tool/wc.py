from argparse import ArgumentParser


def wc(filepath, c=False, l=False, w=False, m=False):
    with open(filepath, mode="rb") as f:
        contents_bin = f.read()
    contents = contents_bin.decode()
    print(
        len(contents_bin) if c else "",
        len(contents.split("\n")) - 1 if l else "",
        len(contents.split()) if w else "",
        len(contents) if m else "",
        filepath,
    )


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("input_file")
    parser.add_argument("--count", "-c", action="store_true")
    parser.add_argument("--lines", "-l", action="store_true")
    parser.add_argument("--words", "-w", action="store_true")
    parser.add_argument("--chars", "-m", action="store_true")
    args = parser.parse_args()
    if all([args.count, args.lines, args.words, args.chars]):
        args.count, args.lines, args.words = True, True, True
    wc(args.input_file, args.count, args.lines, args.words, args.chars)
