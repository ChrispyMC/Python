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

class Menubar:
  def __init__(self, master):
    self.master = master
    self.menubar = tk.Menu(self.master)

    self.fileMenu = tk.Menu(self.menubar, tearoff=0)
    self.fileMenu.add_command(label="Open File", command=self.test_command)
    self.fileMenu.add_command(label="Open Directory", command=self.test_command)
    self.fileMenu.add_separator()
    self.fileMenu.add_command(label="Exit", command=self.master.quit)

    self.hashMenu = tk.Menu(self.menubar, tearoff=0)
    self.hashMenu.add_command(label="Hash Input", command=hasher.test)

    self.menubar.add_cascade(label="File", menu=self.fileMenu)
    self.menubar.add_cascade(label="Hash", menu=self.hashMenu)
  
  def test_command(self):
    print("oi, josuke?")


class HashGUI:
  def __init__(self, master, function="SHA3-256"):
    self.master = master
    self.master.geometry(window.GEOMETRY)
    self.master.title(f"Hash GUI ({function.upper()})")
    self.master.iconbitmap(os.path.dirname(os.path.realpath(__file__)) + "/" + window.ICON)
    self.master.resizable()
    self.master.config(bg=window.BACKGROUND)

    self.menubar = Menubar(self.master)
    self.master.config(menu=self.menubar.menubar)
    
def main(function="SHA3-256"):
  root = tk.Tk()
  gui = HashGUI(root)
  root.mainloop()

if __name__ == "__main__":
  main()