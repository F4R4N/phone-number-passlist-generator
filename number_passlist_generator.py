import os
import sys
from datetime import timedelta
import time
import argparse
from tqdm import trange

EPILOG = 'Download : python number_passlist_generator.py -n 0916 -p /path/to/dist/'

def human_readable_filesize(num, suffix="B"):
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"

def main(prenumber, path):
    os.chdir(path)
    start_time = time.time()
    print("waiting . . .")
    filename = 'passlist-' + prenumber + '-py.txt'
    with open(filename, "a", encoding="utf-8") as file:
        for i in trange(0, 10000000):
            i = str(i).zfill(7)  # exclude pre-number phone number have 7 digits
            res = prenumber + i
            file.write(res + '\n')
    file_size = human_readable_filesize(os.path.getsize(filename))

    end_time = time.time()
    res_time = timedelta(seconds=int(end_time - start_time))
    print(f"Phone numbers saved to '{filename}'\nFilesize: '{file_size}'\nDuration: '{res_time}s'")

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(prog='python number_passlist_generator.py',
                                        epilog=EPILOG, add_help=False)
        parser.add_argument('-n', '--pre', help='Specify your desired pre-number.', required=True)
        parser.add_argument('-p', '--path', help='Path to save output file.', required=True)
        parser.add_argument('-h', '--help', action='help',
                            default=argparse.SUPPRESS, help='Show this help message and exit.')
        args = parser.parse_args()
        main(args.pre, args.path)
    except KeyboardInterrupt:
        print("you used Ctrl+C\nexiting . . . ")
        sys.exit(0)
