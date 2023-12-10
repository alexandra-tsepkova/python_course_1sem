import argparse
from sys import stdin, stdout


def wc_stdin():
    total = []
    for line in stdin:
        total.append([1, len(line.split()), len(line.encode('utf-8'))])
    total = tuple(sum(x) for x in zip(*total))

    stdout.write(f'{total[0]:>7} {total[1]:>7} {total[2]:>7}\n')


def wc_files(args):
    total = []
    offset = 1
    for filename in args.FILE:
        file_stats = []
        with open(filename, 'r') as file:
            for line in file:
                file_stats.append([1, len(line.split()), len(line.encode('utf-8'))])
        file_stats = tuple(sum(x) for x in zip(*file_stats))
        total.append(file_stats)
        offset = max(len(str(file_stats[1])), len(str(file_stats[2])), offset)
    for number, stat in enumerate(total):
        stdout.write(f'{stat[0]:>{offset}} {stat[1]:>{offset}} {stat[2]:>{offset}} {args.FILE[number]}\n')
    if len(args.FILE) > 1:
        total = tuple(sum(x) for x in zip(*total))
        stdout.write(f'{total[0]:>{offset}} {total[1]:>{offset}} {total[2]:>{offset}} total\n')


def main(args):
    if args.FILE == 'stdin':
        wc_stdin()
    else:
        wc_files(args)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Custom wc script.\n\n"
        "Print newline, word, and byte counts for each FILE, and a total line if\n"
        "more than one FILE is specified.  A word is a non-zero-length sequence of\n"
        "characters delimited by white space.\n"
        "With no FILE read standard input.\n"
    )
    parser.add_argument(
        "FILE", nargs="*", default="stdin", help="name(s) of file(s) to read from"
    )

    main(parser.parse_args())
