import io, os, sys
import tkinter as tk

try:
  import hasher
  import references
  #import themes
except ImportError:
  from hashgui import hasher
  from hashgui import references
  #from hashgui import themes

resources = references.Resources()
window = references.Window()

root = tk.Tk()
root.iconbitmap(os.path.dirname(os.path.abspath(__file__))+window.ICON)
root.geometry(window.GEOMETRY)
root.configure(bg=window.BACKGROUND)
root.resizable(False, False)

####--Hash Function Options--####

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

####--Menu Bar--####

"""Menu commands."""
def test():
  print("test")

"""Menu."""
"""menuBar = tk.Menu(root)

fileMenu = tk.Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Open File...", command=hasher.whatever)
fileMenu.add_command(label="Open Directory...", command=test)
fileMenu.add_separator()
fileMenu.add_command(label="Quit", command=root.quit)
menuBar.add_cascade(label="File", menu=fileMenu)

hashMenu = tk.Menu(menuBar, tearoff=0)
hashMenu.add_command(label="Hash Files", command=hasher.whatever)
hashMenu.add_command(label="Hash Directories", command=test)
menuBar.add_cascade(label="Hash", menu=hashMenu)"""
#Add -> root.config(menu=menuBar) -> start()


"""File/Directory Selection Frames."""
####--First Column--####

####--First Frame--####
fileFrame = tk.Frame(root, width=window.WIDTH/2, height=window.HEIGHT/2, relief="sunken", bg=window.BACKGROUND).grid(row=0, column=0, rowspan=5)
fileLabel = tk.Label(fileFrame, text="File Selection", font=("Helvetica", window.LABELTEXTSIZE)).grid(row=0, column=0)

####--Second Frame--####
directoryFrame = tk.Frame(root, width=window.WIDTH/2, height=window.HEIGHT/2, relief="raised", bg=window.BACKGROUND).grid(row=4, column=0, rowspan=5)
directoryLabel = tk.Label(fileFrame, text="Directory Selection", font=("Helvetica", window.LABELTEXTSIZE)).grid(row=5, column=0)

"""Hashing Frames."""
####--Second Column--####

####--First Frame--####
hashFileFrame = tk.Frame(root, width=window.WIDTH/2, height=window.HEIGHT/2, relief="raised", bg=window.BACKGROUND).grid(row=0, column=1, rowspan=5)
hashFileLabel = tk.Label(hashFileFrame, text="File Hash Output", font=("Helvetica", window.LABELTEXTSIZE)).grid(row=0, column=1)

####--Second Frame--####
hashDirFrame = tk.Frame(root, width=window.WIDTH/2, height=window.HEIGHT/2, relief="raised", bg=window.BACKGROUND).grid(row=4, column=1, rowspan=5)
hashDirLabel = tk.Label(hashDirFrame, text="Directory Hash Output", font=("Helvetica", window.LABELTEXTSIZE)).grid(row=5, column=1)

"""Functions Menu."""
hashFunction = tk.StringVar()
changeFunction = tk.OptionMenu(hashFileFrame, hashFunction, *hashOptions)
changeFunction.config(font=("Helvetica", window.BUTTONTEXTSIZE), fg=window.TEXT, bg=window.DROPDOWN)
changeFunction.grid(row=4, column=1, sticky="sew")

"""Change title on write."""
def functionCallback(*args):
  root.title(f"Hash GUI ({hashFunction.get()})")

hashFunction.trace("w", functionCallback)

####--Start GUI Loop--####

"""Start function."""
def start(function="SHA3-256"):
  hashFunction.set(function.upper())
  root.title(f"Hash GUI ({function})")
  root.mainloop()

"""Start the tkinter main loop if __name__ == "__main__"."""
if __name__ == "__main__":
  print(root.grid_size())
  start()