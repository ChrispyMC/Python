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
    self.button = tk.Button(self.master, text="Add files", fg=window.TEXT, bg=window.BUTTON, command=self.open_files)
    self.button.config(fg=window.TEXT, bg=window.BUTTON)
    self.button.pack()

  def open_files(self):
    self.filenames.append(filedialog.askopenfiles(initialdir="/", title="Select Files", filetypes=[("All Files", "*.*")]))
    self.label.config(text="%s files selected." % len(self.filenames))
    print(self.filenames)
    for f in self.filenames:
      print(f)


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

    self.listbox = tk.Listbox(self.frame, yscrollcommand=self.scrollbar.set)
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
    self.frame.config(text="%s selected." % self.listbox.size())
    if self.listbox.size() < 1:
      self.frame.config(text="No directories selected.")