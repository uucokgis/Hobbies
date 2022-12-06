import PySimpleGUI as pg

from SaveMemoPython.db.db import save_text, get_remembers

pg.theme('DarkAmber')


class GUI:
    get_date_option = False
    layout = [
        [pg.Button('Store texts'),
         pg.Checkbox('Show dates', key='-DATECB-'),
         pg.Multiline(size=(50, 25), expand_y=True, expand_x=True, key='-STORE-'),
         # todo: put filter search box
         pg.Listbox(values=get_remembers(get_date_option), size=(50, 25), enable_events=True, key='-RLIST-')]
    ]
    window = pg.Window('Remember', layout, auto_size_text=True, auto_size_buttons=True,
                       resizable=True, finalize=True)
    window['-STORE-'].bind("<Return>", "CTRL-Enter")

    def refresh_texts(self):
        datas = get_remembers(self.get_date_option)
        self.window['-RLIST-'].update(datas)

    def clean_texts(self):
        self.window['-STORE-'].update("")

    def save_texts(self, data):
        save_text(data)
        self.refresh_texts()
        self.clean_texts()

    def start(self):
        while True:
            event, values = self.window.read()
            if event == pg.WIN_CLOSED or event == 'Cancel':
                break
            if event == 'Store texts':
                self.save_texts(values['-STORE-'])

            if values['-DATECB-']:
                self.get_date_option = values['-DATECB-']

            if event == "-STORE-" + "CTRL-Enter":
                self.save_texts(values['-STORE-'])
