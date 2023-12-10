import argparse
from sys import stdin, stdout

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description="Custom nl script.\n\n"
    "Write FILE to standard output, with line numbers added.\n"
    "With no FILE read standard input."
)
parser.add_argument(
    "FILE", nargs="?", default="stdin", help="name of file to read from"
)
args = parser.parse_args()

if args.FILE == 'stdin':
    for count, line in enumerate(stdin):
        stdout.write(f'{count + 1:>6}  {line}')

else:
    with open(args.FILE, 'r') as file:
        for count, line in enumerate(file):
            stdout.write(f'{count + 1:>6}  {line}')
