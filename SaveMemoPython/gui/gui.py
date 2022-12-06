from enum import Enum
from SaveMemoPython.db.db import get_remembers, save_text

import PySimpleGUI as pg

pg.theme('DarkAmber')


class GUIEnum(Enum):
    GET = 0
    POST = 1


class GUI:
    layout = [
        [pg.Button('Store texts'),
         pg.Multiline(size=(50, 300), expand_y=True, expand_x=True)],
        [pg.Button('Ok'), pg.Button('Cancel')]]
    window = pg.Window('Remember', layout, auto_size_text=True, auto_size_buttons=True, resizable=True)

    gui_types: GUIEnum = GUIEnum.GET
    get_texts: [str] = []

    def __init__(self):
        pass

    def save_text(self, text):
        save_text(text)

    def handle_inputs(self):
        if self.gui_types == GUIEnum.GET:
            pass
        elif self.gui_types == GUIEnum.POST:
            pass

    def start(self):
        while True:
            event, values = self.window.read()
            if event == pg.WIN_CLOSED or event == 'Cancel':
                break
            if event == 'Store texts':
                print("Storing..")
                self.save_text(values[0])
