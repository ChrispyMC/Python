import io, os, sys
import tkinter as tk

try:
  """Program scripts/resources."""
  import hasher
  import references
  #import themes
  """External Tk windows."""
  import exthash
except ImportError:
  """Program scripts/resources."""
  from hashgui import hasher
  from hashgui import references
  #from hashgui import themes
  """External Toplevel windows."""
  from hashgui import exthash

resources = references.Resources()
window = references.Window()

if sys.platform == "linux" and os.environ.get("DISPLAY", "") == "":
  print("No display found. Using :0.0")
  os.environ.__setitem__("DISPLAY", ":0.0")

"""Options for hash functions."""
HASH_OPTIONS = [
  #MD5
  "MD5",
  #SHA-3
  "SHA3-224",
  "SHA3-256",
  "SHA3-384",
  "SHA3-512",
  #SHA-2
  "SHA-224",
  "SHA-256",
  "SHA-384",
  "SHA-512",
  #SHA-1
  "SHA1",
  #SHAKE
  "SHAKE-128",
  "SHAKE-256",
  #BLAKE
  "BLAKE2B",
  "BLAKE2S"
]

class Menubar:
  def __init__(self, master):
    self.master = master
    self.menubar = tk.Menu(self.master)
    self.filehash = exthash.FileHash()
    self.dirhash = exthash.DirHash()

    self.fileMenu = tk.Menu(self.menubar, tearoff=0)
    self.fileMenu.add_command(label="Open File...", command=self.test_command)
    self.fileMenu.add_command(label="Open Directory...", command=self.test_command)
    self.fileMenu.add_separator()
    self.fileMenu.add_command(label="Exit", command=self.master.quit)

    self.editMenu = tk.Menu(self.menubar, tearoff=0)
    self.editMenu.add_command(label="Themes", command=self.test_command)

    self.toolsMenu = tk.Menu(self.menubar, tearoff=0)
    self.toolsMenu.add_command(label="Hash File...", command=self.filehash.show_file_window)
    self.toolsMenu.add_command(label="Hash Directory...", command=self.dirhash.show_dir_window)
    self.toolsMenu.add_separator()
    self.toolsMenu.add_command(label="Hash Input Files", command=hasher.test)
    self.toolsMenu.add_command(label="Hash Input Directories", command=hasher.test)

    self.menubar.add_cascade(label="File", menu=self.fileMenu)
    self.menubar.add_cascade(label="Edit", menu=self.editMenu)
    self.menubar.add_cascade(label="Tools", menu=self.toolsMenu)
  
  def test_command(self):
    print("oi, josuke?")


class OptionMenu:
  def __init__(self, master):
    self.master = master
    self.hashOption = tk.StringVar()
    self.hashOption.trace("w", self.set_title)

    self.optionmenu = tk.OptionMenu(self.master, self.hashOption, *HASH_OPTIONS)
    self.optionmenu.config(fg=window.TEXT, bg=window.BUTTON, activebackground=window.BUTTONLIGHT, font=("Helvetica", window.BUTTONTEXTSIZE))

  def set_title(self, *args):
    self.master.title("Hash GUI (%s)" % self.hashOption.get())
    print ("Set function to %s." % self.hashOption.get())


class HashList:
  def __init__(self, master):
    self.master = master
    self.frame = tk.Frame(bg=window.BACKGROUND, padx=10, pady=5)
    self.dictionary = {}
    
    """
    * Individual files should be added to the base dictionary.
    * Directories make a new key (Directory Path) with a dictionary value
      * This dictionary will hold the file key-value pairs (Display name-IOWrapper Object) in the directory
      * Users should be able to add/remove files to hash from the directory.
    """

    self.scrollbar = tk.Scrollbar(self.frame, orient="vertical")

    self.listbox = tk.Listbox(self.frame, selectmode="extended", yscrollcommand=self.scrollbar.set)
    self.listbox.pack(fill="both", anchor="n", pady=5)

    self.add = tk.Button(self.frame, text="Add files", command=self.open_files)
    self.add.config(fg=window.TEXT, bg=window.BUTTON, font=("Helvetica", window.BUTTONTEXTSIZE), padx=5)
    self.add.pack(fill="x", anchor="s")

    self.remove = tk.Button(self.frame, text="Remove files", command=self.remove_files)
    self.remove.config(fg=window.TEXT, bg=window.BUTTON, font=("Helvetica", window.BUTTONTEXTSIZE), padx=5)
    self.remove.pack(fill="x", anchor="s")
  
  def open_files(self):
    files = filedialog.askopenfiles(initialdir="/", title="Select Files", filetypes=[("All Files", "*.*")])
    for f in files:
      if f not in self.listbox.get(0, "end"):
        self.dictionary[f.name] = f
        self.listbox.insert("end", f.name)
    print("Added %s to list." % ', '.join([f.name for f in files]))
    #self.frame.config(text="%s opened." % len(self.files))

  def remove_files(self):
    for i in list(self.listbox.curselection()):
      try:
        del self.files[self.listbox.get(i)]
        self.listbox.delete(i)
      except: pass #_tkinter.TclError
    #self.frame.config(text="%s opened." % len(self.files))
    #if self.listbox.size() < 1:
    #  self.frame.config(text="No files opened.")
    
  #Add code to set status bar to tk.ANCHOR text.


class StatusBar:
  def __init__(self, master):
    self.master = master
    self.frame = tk.Frame(height=window.LABELTEXTSIZE * 2, bd=1, bg=window.BUTTONLIGHT, relief="sunken")

    self.selectionLabel = tk.Label(self.frame, text="Nothing selected.", 
      font=("TkCaptionFont", window.LABELTEXTSIZE),  fg=window.BACKGROUND)
    self.selectionLabel.pack(side="left")
    
    self.statisticsLabel = tk.Label(self.frame, text="0 files, 0 directories", 
      font=("TkCaptionFont", window.LABELTEXTSIZE), fg=window.BACKGROUND)
    self.statisticsLabel.pack(side="right")
  
  #Add code to update the count of files and directories from len(FileList.files) & DirectoryList.dirlist.size()
    
    
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

    self.filelist = FileList(self.master)
    self.filelist.frame.pack(side="top", fill="x")


def main(function="MD5"):
  root = tk.Tk()
  gui = HashGUI(root)
  root.mainloop()

if __name__ == "__main__":
  main()