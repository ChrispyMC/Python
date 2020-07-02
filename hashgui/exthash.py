#File Hash Toplevel window
import io, os, sys
import tkinter as tk
from tkinter import filedialog

try:
  import hasher
  import references
except ImportError:
  from hashgui import hasher
  from hashgui import references

resources = references.Resources()
window = references.Window()
wm = references.WindowMenu()

filenames, dirnames = [], []

class FileHash:
  def __init__(self):
    self.filenames = []

  def show_file_window(self):
    self.master = tk.Toplevel()
    self.master.geometry(wm.GEOMETRY)
    self.master.title("Select files to hash")
    self.master.iconbitmap(os.path.dirname(os.path.realpath(__file__)) + "/" + window.ICON)
    self.master.resizable(False, False)
    self.master.config(bg=window.BACKGROUND)

    self.label = tk.Label(self.master, text="No files selected.", fg=window.TEXT, bg=window.LABEL, 
      font=("Helvetica", window.LABELTEXTSIZE))
    self.label.pack(fill="x", side="top")
    self.button = tk.Button(self.master, text="Open files", fg=window.TEXT, bg=window.BUTTON, command=self.open_files)
    self.button.config(fg=window.TEXT, bg=window.BUTTON)
    self.button.pack()

  def open_files(self):
    self.filenames.append(filedialog.askopenfiles(initialdir="/", title="Select Files", filetypes=[("All Files", "*.*")]))
    self.label.config(text="%s files selected." % len(self.filenames))
    print(self.filenames)
    for f in self.filenames:
      print(f)


class DirHash:
  def __init__(self):
    self.dirnames = []

  def show_dir_window(self):
    self.master = tk.Toplevel()
    self.master.geometry(wm.GEOMETRY)
    self.master.title("Select directories to hash")
    self.master.iconbitmap(os.path.dirname(os.path.realpath(__file__)) + "/" + window.ICON)
    self.master.resizable(False, False)
    self.master.config(bg=window.BACKGROUND)

    self.label = tk.Label(self.master, text="No directories selected.", fg=window.TEXT, bg=window.LABEL, 
      font=("Helvetica", window.LABELTEXTSIZE))
    self.label.pack(fill="x", side="top")
    self.button = tk.Button(self.master, text="Open directory", fg=window.TEXT, bg=window.BUTTON, command=self.open_directory)
    self.button.config(fg=window.TEXT, bg=window.BUTTON)
    self.button.pack()
  
  def open_directory(self):
    self.dirnames.append(filedialog.askdirectory())
    self.label.config(text="%s directories selected." % len(self.dirnames))
    print(self.dirnames)
    for d in self.dirnames:
      print(d)