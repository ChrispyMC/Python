import sys
import argparse

try:
  from gui import main
  from hasher import hash_file
except ImportError:
  from hashgui.gui import main
  from hashgui.hasher import hash_file

available = [
    "MD5",
    "SHA1",
    "SHA-224",
    "SHA-256",
    "SHA-384",
    "SHA-512",
    "SHA3-224",
    "SHA3-256",
    "SHA3-384",
    "SHA3-512",
    "SHAKE-128",
    "SHAKE-256",
    "BLAKE2B",
    "BLAKE2S"]

parser = argparse.ArgumentParser(description="Select files or directories to hash using a Tkinter GUI.",
                                 prog="hashgui", epilog=", ".join(available))

parser.add_argument("--version", action="version", version="Hash GUI 1.0")
parser.add_argument("-f", "--function", help="Provide the hash function used.", default="MD5")
parser.add_argument("--file", help="Pass in an input file to the hasher.", action="append", default=None)
parser.add_argument("--directory", help="Pass in a (relative) directory to the hasher.", default=None)

args = parser.parse_args()


def run():
  if args.file is not None:
    print(args.function)
    for f in args.file:
      print(f + " | " + hash_file(filename=f, function=args.function))
    sys.exit(0)
  main(function=args.function)


if __name__ == "__main__":
  run()
