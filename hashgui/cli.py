import argparse
from hashgui.gui import start

parser = argparse.ArgumentParser(description="Select files or directories to hash using a Tkinter GUI.")

parser.add_argument("-f" , "--function", help="Provide the hash function used.", default="sha3-256")

args = parser.parse_args()

def run():
  start(function=args.function)

if __name__ == "__main__":
  run()
