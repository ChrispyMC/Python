import io, os, sys, hashlib
import tkinter as tk

try:
  import references
except ImportError:
  from hashgui import references

resources = references.Resources()
window = references.Window()

root = tk.Tk()
root.iconbitmap(os.path.dirname(os.path.abspath(__file__))+window.ICON)
root.geometry(window.GEOMETRY)
root.configure(bg=window.BACKGROUND)
root.resizable(False, False)

"""Options for hash functions."""
hashOptions = [
  "MD5",
  #SHA3
  "SHA3-224",
  "SHA3-256",
  "SHA3-384",
  "SHA3-512",
  "SHAKE128",
  "SHAKE512"
]

"""Options Menu."""
hashFunction = tk.StringVar(root)
changeFunction = tk.OptionMenu(root, hashFunction, *hashOptions)
changeFunction.config(font=("Helvetica", 12), fg=window.TEXT, bg=window.DROPDOWN)
changeFunction.grid(row=0, column=0, columnspan=2, sticky="we")

"""Change title on write."""
def functionCallback(*args):
  root.title(f"Hash GUI ({hashFunction.get()})")

hashFunction.trace("w", functionCallback)

"""File/Directory Select Frame."""
selectFrame = tk.LabelFrame(root, text="File/Directory Selection", font=("Calibri", 10), width=window.WIDTH/2, height=window.HEIGHT,
  labelanchor="n", relief="sunken", fg=window.TEXT, bg=window.BACKGROUND).grid(row=1, column=0)

"""Hashing Frame."""
hashFrame = tk.LabelFrame(root, text="Hasher", font=("Calibri", 10), width=window.WIDTH/2, height=window.HEIGHT,
  labelanchor="n", relief="raised", fg=window.TEXT, bg=window.BACKGROUND).grid(row=1, column=1)

"""Start function."""
def start(function="SHA3-256"):
  hashFunction.set(function.upper())
  root.title(f"Hash GUI ({function})")
  root.mainloop()

"""Start the tkinter main loop if __name__ == "__main__"."""
if __name__ == "__main__":
  start()