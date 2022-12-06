from enum import Enum

import PySimpleGUI as pg

from SaveMemoPython.db.db import save_text

pg.theme('DarkAmber')


class GUIEnum(Enum):
    GET = 0
    POST = 1


class GUI:

    gui_types: GUIEnum = GUIEnum.GET
    get_texts: [str] = []

    def __init__(self):
        self.window = pg.Window('Remember', self.handle_layouts(), auto_size_text=True, auto_size_buttons=True, resizable=True)

    def handle_layouts(self):
        if self.gui_types == GUIEnum.GET:
            layout = [
                [pg.Button('Store texts'),
                 pg.Multiline(size=(50, 150), expand_y=True, expand_x=True)]]
        elif self.gui_types == GUIEnum.POST:
            layout = []

        else:
            layout = []

        return layout

    def start(self):
        while True:
            event, values = self.window.read()
            if event == pg.WIN_CLOSED or event == 'Cancel':
                break
            if event == 'Store texts':
                print("Storing..")
                save_text(values[0])
