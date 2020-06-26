import tkinter as tk

class OptionMenu(tk.Frame): # <-- with Frame

  def __init__(self, master, status, *options):

    super().__init__(master) # <-- with super()

    self.status = tk.StringVar()
    self.status.set(status)

    # use `self` as parent for widgets inside

    self.dropdown = tk.OptionMenu(self, self.status, *options)
    self.dropdown.pack()


def main():

  editionMap = {1:"English", 2:"German", 3:"Russian"}
  langMap = {1:"English", 2:"German", 3:"Russian"}
  topicMap = {1:"English", 2:"German", 3:"Russian"}

  root = tk.Tk()

  Edition_Filter = OptionMenu(root, "Edition", *editionMap.keys())
  Edition_Filter.grid(row=0, column=0)

  Language_Filter = OptionMenu(root, "Language", *langMap.keys())
  Language_Filter.grid(row=0, column=1)

  Topic_Filter = OptionMenu(root, "Topic", *topicMap.keys())
  Topic_Filter.grid(row=0, column=2)

  root.mainloop()

if __name__ == '__main__':
    main()