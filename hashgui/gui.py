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

    self.fileMenu = tk.Menu(self.menubar, tearoff=0)
    self.fileMenu.add_command(label="Open File...", command=self.test_command)
    self.fileMenu.add_command(label="Open Directory...", command=self.test_command)
    self.fileMenu.add_separator()
    self.fileMenu.add_command(label="Exit", command=self.master.quit)

    self.hashMenu = tk.Menu(self.menubar, tearoff=0)
    self.hashMenu.add_command(label="Hash Input Files", command=hasher.test)
    self.hashMenu.add_command(label="Hash Input Directories", command=hasher.test)
    self.hashMenu.add_separator()
    self.hashMenu.add_command(label="Hash File...", command=hasher.test)
    self.hashMenu.add_command(label="Hash Directory...", command=hasher.test)

    self.menubar.add_cascade(label="File", menu=self.fileMenu)
    self.menubar.add_cascade(label="Hash", menu=self.hashMenu)
  
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
    self.master.title(f"Hash GUI ({self.hashOption.get()})")
    print ("Set function to {0}.".format(self.hashOption.get()))


class HashGUI:
  def __init__(self, master, function="SHA3-256"):
    self.master = master
    self.master.geometry(window.GEOMETRY)
    self.master.title(f"Hash GUI ({function.upper()})")
    self.master.iconbitmap(os.path.dirname(os.path.realpath(__file__)) + "/" + window.ICON)
    self.master.resizable(False, False)
    self.master.config(bg=window.BACKGROUND)

    self.menubar = Menubar(self.master)
    self.master.config(menu=self.menubar.menubar)
    
    self.optionmenu = OptionMenu(self.master)
    self.optionmenu.hashOption.set(function)
    self.optionmenu.optionmenu.pack(side="top", fill="x")


def main(function="SHA3-256"):
  root = tk.Tk()
  gui = HashGUI(root)
  root.mainloop()

if __name__ == "__main__":
  main()