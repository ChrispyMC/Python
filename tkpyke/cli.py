import argparse
"""
try:
  from gui import main
except ImportError:
  from _template.gui import main
"""

parser = argparse.ArgumentParser(description="A template for command-line interface & Tkinter GUI projects.")

parser.add_argument("-c" , "--command", help="Command Description.", default="Default value.")

args = parser.parse_args()

def run():
  #> Code for checking arguments goes here.
  main()

if __name__ == "__main__":
  run()