import argparse
from sys import stdin, stdout

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description="Custom tail script.\n\n"
    "Print the last 10 lines of each FILE to standard output.\n"
    "With more than one FILE, precede each with a header giving the file name.\n"
    "With no FILE read standard input."
)
parser.add_argument(
    "FILE", nargs="*", default="stdin", help="name(s) of file(s) to read from"
)
args = parser.parse_args()

if args.FILE == 'stdin':
    for line in list(stdin)[-10:]:
        stdout.write(line)

else:
    for number, filename in enumerate(args.FILE):
        if len(args.FILE) > 1:
            stdout.write(f'==> {filename} <==\n')
        with open(filename, 'r') as file:
            lines = file.readlines()[-10:]
            for line in lines:
                stdout.write(line)
        if number < len(args.FILE) - 1:
            stdout.write('\n')
