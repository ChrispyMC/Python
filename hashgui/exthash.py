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
    self.files = {}

  def show_file_window(self):
    self.master = tk.Toplevel()
    self.master.geometry(wm.GEOMETRY)
    self.master.title("Select files to hash")
    self.master.iconbitmap(os.path.dirname(os.path.realpath(__file__)) + "/" + window.ICON)
    self.master.resizable(False, False)
    self.master.config(bg=window.BACKGROUND)

    self.frame = tk.LabelFrame(self.master, text="No files selected.", fg=window.TEXT, bg=window.LABEL, 
      font=("Helvetica", window.LABELTEXTSIZE), labelanchor="n", padx=5, pady=5)
    self.frame.pack(side="top", fill="both", expand=True)

    self.scrollbar = tk.Scrollbar(self.frame, orient="vertical")

    self.listbox = tk.Listbox(self.frame, selectmode="extended", yscrollcommand=self.scrollbar.set)
    self.listbox.pack(fill="x")

    self.add = tk.Button(self.frame, text="Add files", command=self.open_files)
    self.add.config(fg=window.TEXT, bg=window.BUTTON, font=("Helvetica", window.BUTTONTEXTSIZE), padx=10)
    self.add.pack(side="left", padx=50)

    self.remove = tk.Button(self.frame, text="Remove files", command=self.remove_files)
    self.remove.config(fg=window.TEXT, bg=window.BUTTON, font=("Helvetica", window.BUTTONTEXTSIZE), padx=10)
    self.remove.pack(side="right", padx=50)

  def open_files(self):
    files = filedialog.askopenfiles(initialdir="/", title="Select Files", filetypes=[("All Files", "*.*")])
    for f in files:
      if f not in self.listbox.get(0, "end"):
        self.files[f.name] = f
        self.listbox.insert("end", f.name)
    print("Added %s to list." % ', '.join([f.name for f in files]))
    self.frame.config(text="%s opened." % len(self.files))

  def remove_files(self):
    for i in list(self.listbox.curselection()):
      try:
        del self.files[self.listbox.get(i)]
        self.listbox.delete(i)
      except: pass #_tkinter.TclError
    self.frame.config(text="%s opened." % self.listbox.size())
    if self.listbox.size() < 1:
      self.frame.config(text="No files opened.")

class DirHash:
  def show_dir_window(self):
    self.master = tk.Toplevel()
    self.master.geometry(wm.GEOMETRY)
    self.master.title("Select directories to hash")
    self.master.iconbitmap(os.path.dirname(os.path.realpath(__file__)) + "/" + window.ICON)
    self.master.resizable(False, False)
    self.master.config(bg=window.BACKGROUND)

    self.frame = tk.LabelFrame(self.master, text="No directories selected.", fg=window.TEXT, bg=window.LABEL, 
      font=("Helvetica", window.LABELTEXTSIZE), labelanchor="n", padx=5, pady=5)
    self.frame.pack(side="top", fill="both", expand=True)

    self.scrollbar = tk.Scrollbar(self.frame, orient="vertical")

    self.listbox = tk.Listbox(self.frame, selectmode="single", yscrollcommand=self.scrollbar.set)
    self.listbox.pack(fill="x")

    self.add = tk.Button(self.frame, text="Add directory", command=self.open_directory)
    self.add.config(fg=window.TEXT, bg=window.BUTTON, font=("Helvetica", window.BUTTONTEXTSIZE), padx=10)
    self.add.pack(side="left", padx=50)

    self.remove = tk.Button(self.frame, text="Remove directory", command=self.remove_directory)
    self.remove.config(fg=window.TEXT, bg=window.BUTTON, font=("Helvetica", window.BUTTONTEXTSIZE), padx=10)
    self.remove.pack(side="right", padx=50)
  
  def open_directory(self):
    directory = filedialog.askdirectory()
    if directory not in self.listbox.get(0, "end"):
      self.listbox.insert("end", directory)
      self.frame.config(text="%s selected." % self.listbox.size())
      print("Added %s to list." % directory)
    else:
      print("%s is already in list." % directory)
  
  def remove_directory(self):
    self.listbox.delete(tk.ANCHOR)
    self.frame.config(text="%s opened." % self.listbox.size())
    if self.listbox.size() < 1:
      self.frame.config(text="No directories opened.")