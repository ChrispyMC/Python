import argparse
try 
  from gui import main
except ImportError:
  from hashgui.gui import main

parser = argparse.ArgumentParser(description="Select files or directories to hash using a Tkinter GUI.")

parser.add_argument("-f" , "--function", help="Provide the hash function used.", default="SHA3-256")

args = parser.parse_args()

def run():
  main(function=args.function)

if __name__ == "__main__":
  run()