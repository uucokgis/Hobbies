import tkinter as tk
from SaveMemoPython.db.db import get_remembers
from enum import Enum


class GUIEnum(Enum):
    GET = 0
    POST = 1


class GUI:
    root = tk.Tk()
    root.title('Remember')
    root.geometry("1000x400")

    gui_types: GUIEnum = GUIEnum.GET
    stored_texts: [str] = []

    def __init__(self):
        self.handle_inputs()

    def add_entry_text(self):
        # store text
        ent = tk.Text(self.root, width=400, font='Arial 24')
        ent.grid(row=1, column=0)

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
