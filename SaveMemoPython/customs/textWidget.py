import tkinter as tk


class Text(tk.Text):
    def __init__(self, parent, *args, **kwargs):
        if kwargs.get('textvariable'):
            self.textvariable = kwargs.pop('textvariable')
            # self.textvariable.bind('<KeyRelease>', lambda *args: )
        super().__init__(parent, *args, **kwargs)
