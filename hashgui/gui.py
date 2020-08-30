import os
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

try:
  """Program scripts/resources."""
  import hasher
  import references
  # import themes
  """External Tk windows."""
  import exthash
except ImportError:
  """Program scripts/resources."""
  from hashgui import hasher  # noqa: F401
  from hashgui import references
  # from hashgui import themes
  """External Toplevel windows."""
  from hashgui import exthash

resources = references.Resources()
window = references.Window()

if sys.platform == "linux" and os.environ.get("DISPLAY", "") == "":
  print("No display found. Using :0.0")
  os.environ.__setitem__("DISPLAY", ":0.0")

"""Options for hash functions can be found in references.py."""


class Menubar:
  def __init__(self, master):
    self.master = master
    self.menubar = tk.Menu(self.master)
    self.filehash = exthash.FileHash()
    self.dirhash = exthash.DirHash()

    self.fileMenu = tk.Menu(self.menubar, tearoff=0)
    self.fileMenu.add_command(label="Open File...", command=self.placeholder)
    self.fileMenu.add_command(label="Open Directory...", command=self.placeholder)
    self.fileMenu.add_separator()
    self.fileMenu.add_command(label="Exit", command=self.master.quit)

    self.editMenu = tk.Menu(self.menubar, tearoff=0)
    self.editMenu.add_command(label="Themes", command=self.placeholder)

    self.toolsMenu = tk.Menu(self.menubar, tearoff=0)
    self.toolsMenu.add_command(label="Hash File...", command=self.filehash.show_file_window)
    self.toolsMenu.add_command(label="Hash Directory...", command=self.dirhash.show_dir_window)
    self.toolsMenu.add_separator()
    self.toolsMenu.add_command(label="Hash Input Files", command=self.placeholder)
    self.toolsMenu.add_command(label="Hash Input Directories", command=self.placeholder)

    self.menubar.add_cascade(label="File", menu=self.fileMenu)
    self.menubar.add_cascade(label="Edit", menu=self.editMenu)
    self.menubar.add_cascade(label="Tools", menu=self.toolsMenu)

  def placeholder(self):
    """Used for menu items that will be updated in the HashGUI class."""
    print("Oi, Josuke! I deleted the menu command.")

  def update(self, menu, index, **options):
    """Update a menu (inheriting from self.menubar)."""
    menu.entryconfigure(index, **options)


class OptionMenu:
  def __init__(self, master):
    self.master = master
    self.hashOption = tk.StringVar()
    self.hashOption.trace("w", self.set_title)

    self.optionmenu = tk.OptionMenu(self.master, self.hashOption, *resources.HASH_OPTIONS)
    self.optionmenu.config(fg=window.TEXT, bg=window.BUTTON, activebackground=window.BUTTONLIGHT,
                           font=("Helvetica", window.BUTTONTEXTSIZE))

  def set_title(self, *args):
    self.master.title("Hash GUI (%s)" % self.hashOption.get())
    print("Set function to %s." % self.hashOption.get())


class HashTree:
  def __init__(self, master):
    self.master = master
    self.tree_frame = tk.Frame(bg=window.BACKGROUND, padx=10, pady=5)
    self.button_frame = tk.Frame(bg=window.BACKGROUND, padx=10, pady=10)
    self.dictionary = {}

    self.treeview = ttk.Treeview(self.tree_frame, selectmode="extended")
    self.scrollbar = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.treeview.yview)
    self.treeview.config(yscrollcommand=self.scrollbar.set)
    self.treeview.pack(fill="both", expand=True, anchor="n", pady=5)

    self.treeview["columns"] = ("1", "2", "3")
    self.treeview["show"] = "headings"

    self.treeview.heading("1", text="Name", command=lambda: self.sort_column(self.treeview, "1", False))
    self.treeview.column("1", width=int(window.WIDTH / 2), minwidth=int(window.WIDTH / 8), anchor='c')
    self.treeview.heading("2", text="Type", command=lambda: self.sort_column(self.treeview, "2", False))
    self.treeview.column("2", width=int(window.WIDTH / 8), minwidth=int(window.WIDTH / 8), anchor='c')
    self.treeview.heading("3", text="Size", command=lambda: self.sort_column(self.treeview, "3", False))
    self.treeview.column("3", width=int(window.WIDTH / 8), minwidth=int(window.WIDTH / 8), anchor='c')

    # <<TreeviewSelect>> bind is a part of the HashGUI class.

    self.add_files = tk.Button(self.button_frame, text="Add files", command=self.open_files)
    self.add_files.config(fg=window.TEXT, bg=window.BUTTON, font=("Helvetica", window.BUTTONTEXTSIZE), padx=5)
    self.add_files.pack(fill="x", anchor="n")

    self.remove_files = tk.Button(self.button_frame, text="Remove files", command=self.remove_files)
    self.remove_files.config(fg=window.TEXT, bg=window.BUTTON, font=("Helvetica", window.BUTTONTEXTSIZE), padx=5)
    self.remove_files.pack(fill="x", anchor="n")

  def test(self):
    """Placeholder command."""
    print("test")

  def open_files(self):
    """Add a list of files to the treeview widget."""
    files = filedialog.askopenfiles(initialdir="/", title="Select Files", filetypes=[("All Files", "*.*")])
    added = []
    for f in files:
      if f not in self.treeview.get_children() and f.name not in self.dictionary:
        filesize = os.path.getsize(os.path.realpath(f.name))
        self.treeview.insert("", "end", text=f.name, values=(f.name, "File", str(filesize) + " bytes"))
        self.dictionary[f.name] = f
        added.append(f)
    if added:
      print("Added %s to list." % ', '.join([f.name for f in added]))

  def remove_files(self):
    """Find & remove items selected from the treeview."""
    for i in self.treeview.selection():
      del self.dictionary[self.treeview.item(i, "values")[0]]
      self.treeview.delete(i)

  def sort_column(self, tree, col, reverse):
    """Sort column ascending/descending."""
    # Get items in the tree
    lst = [(tree.set(k, col), k) for k in tree.get_children('')]
    lst.sort(key=lambda t: t[0], reverse=reverse)

    # Rearrange items in sorted positions.
    for index, (val, k) in enumerate(lst):
      tree.move(k, "", index)

    # Reverse column sort next time.
    tree.heading(col, command=lambda: self.sort_column(tree, col, not reverse))

    # Print debug text.
    text = f"Sorted column {col} ascending." if not reverse else f"Sorted column {col} descending."
    print(text)

  def get_statistics(self):
    files, directories = 0, 0
    for i in self.treeview.get_children():
      if self.treeview.item(i, "values")[1] == "File":
        files += 1
      else:
        directories += 1
    return (files, directories)


class StatusBar:
  def __init__(self, master):
    self.master = master
    self.frame = tk.Frame(height=window.LABELTEXTSIZE * 2, bd=1, bg=window.BUTTONLIGHT, relief="sunken")

    self.selectionLabel = tk.Label(self.frame, text="Nothing selected.",
                                   font=("TkCaptionFont", window.LABELTEXTSIZE), fg=window.BACKGROUND)
    self.selectionLabel.pack(side="left")

    self.statisticsLabel = tk.Label(self.frame, text="0 files, 0 directories.",
                                    font=("TkCaptionFont", window.LABELTEXTSIZE), fg=window.BACKGROUND)
    self.statisticsLabel.pack(side="right")

  def set_left(self, text="Use StatusBar.set_left(text=\"Text.\") to modify this label."):
    """Set the selection (left) status bar label."""
    self.selectionLabel.config(text=text)

  def set_right(self, text="Use StatusBar.set_right(text=\"Text.\") to modify this label."):
    """Set the statistics (right) status bar label."""
    self.statisticsLabel.config(text=text)


class HashGUI:
  def __init__(self, master, function="MD5"):
    self.master = master
    self.master.geometry(window.GEOMETRY)
    self.master.title("Hash GUI (%s)" % function.upper())
    self.master.iconbitmap(os.path.dirname(os.path.realpath(__file__)) + "/" + window.ICON)
    self.master.resizable(False, False)
    self.master.config(bg=window.BACKGROUND)

    self.menubar = Menubar(self.master)
    self.master.config(menu=self.menubar.menubar)

    self.optionmenu = OptionMenu(self.master)
    self.optionmenu.hashOption.set(function)
    self.optionmenu.optionmenu.pack(side="top", fill="x")

    self.statusbar = StatusBar(self.master)
    self.statusbar.frame.pack(side="bottom", fill="x")

    self.hashtree = HashTree(self.master)
    self.hashtree.tree_frame.pack(side="top", fill="both", expand=True)
    self.hashtree.button_frame.pack(side="top", fill="both", expand=True)

    self.hashtree.treeview.bind("<<TreeviewSelect>>", self.treeview_select)

    self.menubar.update(menu=self.menubar.fileMenu, index=0, command=lambda: self.hashtree.open_files())

    # Add code to update the count of files and directories from treeview, sorted by type. ("file" or, "directory")

  def treeview_select(self, event):
    """Update the statusbar after a selection has been made."""
    # Get the selection and update the selection (left) bar.
    selected = event.widget.selection()
    items = []
    try:
      for i in selected:
        items.append(self.hashtree.treeview.item(i)["text"])
      self.statusbar.set_left("Selected " + ", ".join(items))
    except AttributeError:
      self.statusbar.set_left("Nothing selected.")

    # Get the treeview's item statistics and update the statistics (right) bar.
    statistics = self.hashtree.get_statistics()
    self.statusbar.set_right(text="{0} files, {1} directories.".format(statistics[0], statistics[1]))


def main(function="MD5"):
  root = tk.Tk()
  gui = HashGUI(root)  # noqa: F841
  root.mainloop()


if __name__ == "__main__":
  main()
