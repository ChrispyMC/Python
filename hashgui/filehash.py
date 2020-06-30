#File Hash Toplevel window
import io, os, sys
import tkinter as tk

try:
  import hasher
  import references
except ImportError:
  from hashgui import hasher
  from hashgui import references

resources = references.Resources()
window = references.Window()
wm = references.WindowMenu()

def show():
  toplevel = tk.Toplevel()
  toplevel.geometry(wm.GEOMETRY)
  toplevel.title("Hash File")
  toplevel.iconbitmap(os.path.dirname(os.path.realpath(__file__)) + "/" + window.ICON)
