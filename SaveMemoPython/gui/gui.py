import tkinter as tk
from SaveMemoPython.customs.textWidget import Text
from SaveMemoPython.db.db import get_remembers
from enum import Enum


class GUIEnum(Enum):
    GET = 0
    POST = 1


class GUI:
    root = tk.Tk()
    root.title('Remember')
    root.geometry("600x400")

    gui_types: GUIEnum = GUIEnum.GET
    stored_texts: [str] = []
    typing_text = tk.StringVar()

    def __init__(self):
        self.frame = tk.Frame(self.root, bg='red')
        self.frame.pack()
        self.handle_inputs()

    def add_entry_text(self):
        # store text
        entLabel = tk.Label(self.frame, text='Entry Text', justify=tk.CENTER)
        entLabel.grid(row=1, column=1)
        ent = Text(self.frame, font='Arial 24', textvariable=self.typing_text)
        ent.grid(row=2, column=1)

    def fill_stored_texts(self):
        data = get_remembers()
        self.stored_texts = data

    def add_get_text(self):
        listBox = tk.Listbox(self.root, listvariable=self.stored_texts, selectmode=tk.MULTIPLE)

    def handle_inputs(self):
        if self.gui_types == GUIEnum.GET:
            self.add_entry_text()
        elif self.gui_types == GUIEnum.POST:
            self.add_get_text()

    def start(self):
        self.root.mainloop()
