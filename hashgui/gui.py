import io, os, sys, hashlib
from hashgui import references
from tkinter import Tk

resources = references.Resources()
window = references.Window()

root = Tk()
root.geometry(window.GEOMETRY)

def start(function="sha3-256"):
  root.title(f"Hash GUI ({function})")
  root.mainloop()

if __name__ == "__main__":
  start()