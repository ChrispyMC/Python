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
  print("what")

"""Menu."""
menuBar = tk.Menu(root)

fileMenu = tk.Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Open File...", command=hasher.test)
fileMenu.add_command(label="Open Directory...", command=test)
fileMenu.add_separator()
fileMenu.add_command(label="Quit", command=root.quit)
menuBar.add_cascade(label="File", menu=fileMenu)

hashMenu = tk.Menu(menuBar, tearoff=0)
hashMenu.add_command(label="Hash Files", command=hasher.test)
hashMenu.add_command(label="Hash Directories", command=test)
menuBar.add_cascade(label="Hash", menu=hashMenu)

"""Functions Menu."""
hashFunction = tk.StringVar()
changeFunction = tk.OptionMenu(root, hashFunction, *hashOptions)
changeFunction.config(font=("Helvetica", window.BUTTONTEXTSIZE), fg=window.TEXT, bg=window.DROPDOWN)
changeFunction.pack(side="top", fill="x")

"""Change title on write."""
def functionCallback(*args):
  root.title(f"Hash GUI ({hashFunction.get()})")
  print(f"Switched hash function to {hashFunction.get()}.")

hashFunction.trace("w", functionCallback)

####--Status Bar--####
statusBar = tk.Label(root, text="No items selected.", relief="sunken", anchor="w", font=("Helvetica", window.LABELTEXTSIZE), bd=1, 
  fg=window.TEXT, bg=window.LABEL).pack(side="bottom", fill="x")

####--Input List Frame--####
"""Left Frame."""
inputFrame = tk.LabelFrame(root, fg=window.TEXT, bg=window.BACKGROUND, 
  labelanchor="n", text="File/Directory Selection")

#Add to Listbox Buttons
inputDirButton = tk.Button(inputFrame, text="Open Directory", font=("Helvetica", window.BUTTONTEXTSIZE), 
  bg=window.BUTTONLIGHT, command=hasher.test)
inputDirButton.pack(side="top", fill="x")

inputFileButton = tk.Button(inputFrame, text="Open Files", font=("Helvetica", window.BUTTONTEXTSIZE), bg=window.BUTTONLIGHT, command=hasher.test)
inputFileButton.pack(side="top", fill="x")

#Listbox widget
inputListbox = tk.Listbox(inputFrame, fg=window.TEXT, bg=window.BACKGROUND)
inputListbox.pack(side="top", fill="both", expand=True)

#Remove from Listbox Buttons
removeFileButton = tk.Button(inputFrame, text="Remove File", font=("Helvetica", window.BUTTONTEXTSIZE), 
  fg=window.TEXT, bg=window.BUTTON, command=lambda inputListbox=inputListbox: inputListbox.delete(tk.ANCHOR))
removeFileButton.pack(side="bottom", fill="x")

removeDirButton = tk.Button(inputFrame, text="Remove Directory", font=("Helvetica", window.BUTTONTEXTSIZE), 
  fg=window.TEXT, bg=window.BUTTON, command=hasher.test)
removeDirButton.pack(side="bottom", fill="x")

inputFrame.pack_propagate(False)
inputFrame.pack(side="left", fill="both", expand=True)

####--Output List Frame--####
"""Right Frame."""
outputFrame = tk.LabelFrame(root, fg=window.TEXT, bg=window.BACKGROUND, 
  labelanchor="n", text="Hasher")

outputFrame.pack(side="right", fill="both", expand=True)

####--Start GUI Loop--####

"""Start function."""
def start(function="SHA3-256"):
  hashFunction.set(function.upper())
  root.title(f"Hash GUI ({function})")
  root.config(menu=menuBar)
  root.mainloop()

"""Start the tkinter main loop if __name__ == "__main__"."""
if __name__ == "__main__":
  print(root.grid_size())
  start()