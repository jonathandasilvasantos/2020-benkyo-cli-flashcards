from prompt_toolkit import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.layout.containers import VSplit, Window, HSplit
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
from prompt_toolkit.input import Input
from prompt_toolkit.widgets import Box, Button
from utils.singleton import Singleton
from view.widgets.uicardtoolbar import UICardToolbar, get_toolbar
from view.model.uicardstate import UICardState
from view.model.uicarddata import UICardData



class UICard(metaclass=Singleton):
    uicard_data = None
    uicard_state = None
    uicard_callbacks = None

    frontal_buffer = None
    hidden_buffer = None
    tag_buffer = None
    buttons = []
    edit_buttons = []

    kb = None
    layout = None

    def __init__(self, uicard_data, uicard_state, uicard_callbacks):
        self.uicard_data = uicard_data
        self.uicard_state = uicard_state
        self.uicard_callbacks = uicard_callbacks
        self.buttons_box = None

        self.build_ui()
        self.bind_keyboard()




    def build_ui(self):

        self.frontal_buffer = Buffer()
        self.frontal_buffer.wrap_lines = True
        self.frontal_buffer.dont_extend_width = True

        self.hidden_buffer = Buffer()
        self.hidden_buffer.wrap_lines = True
        self.hidden_buffer.dont_extend_width = True

        self.tag_buffer = Buffer()
        self.tag_buffer.wrap_lines = True
        self.tag_buffer.dont_extend_width = True
        self.tag_buffer.dont_extend_height = True

        empty_buttons = [
            Button('Empy', handler=self.exit_),
            Button('Empy', handler=self.exit_),
        ]

        self.toolbar = VSplit(empty_buttons, height=1)

        left_panel = Window(content=BufferControl(buffer=self.frontal_buffer), wrap_lines=True)
        right_panel = Window(content=BufferControl(buffer=self.hidden_buffer), wrap_lines=True)
        self.bottom_panel = Box(self.toolbar, height=4)
        tag_panel = VSplit([
        Window(content=FormattedTextControl(text='TAG: '), width=5),
        Window(content=BufferControl(buffer=self.tag_buffer))
        ], height=1)




        vertical_container = VSplit([
        Window(width=2, char='| '),
        left_panel,
        Window(width=3, char=' | '),
        right_panel,
        Window(width=2, char=' |'),
        ])

        title_panel = VSplit([
        Window(width=2, char='| '),
        Window(content=FormattedTextControl(text='Frontal Face')),
        Window(width=3, char=' | '),
        Window(content=FormattedTextControl(text='Hidden Face')),
        Window(width=2, char=' |')
        ], height=1)

        footer_panel = VSplit([
        Window(width=2, char='| '),
        Window(content=FormattedTextControl(text='Status bar')),
        Window(width=3, char=' | '),
        tag_panel,
        Window(width=2, char=' |'),
        ], height=1)

        root_container = HSplit([
        Window(height=1, char='='),
        title_panel,
        Window(height=1, char='-'),
        vertical_container,
        Window(height=1, char='-'),
        footer_panel,
        Window(height=1, char='-'),
        self.bottom_panel
        ])

        self.layout = Layout(root_container)
        self.show_toolbar('pratice')


    def show_toolbar(self, id):
        toolbar = get_toolbar(self.uicard_state.toolbars, id)
        self.toolbar.children = toolbar.toolbar_panel.children
        self.layout.focus(toolbar.prompt_buttons[0])



    def change_mode(self, mode):
        self.uicard_state.mode = mode
        if get_toolbar(self.uicard_state.toolbars, mode) is not None:
            self.show_toolbar(mode)



    def exit_():
        exit(0)
    def restore():
        pass
    def save():
        pass
    def cancel(self):
        pass


    def bind_keyboard(self):


        kb = KeyBindings()
        self.kb = kb
        kb.add("tab")(focus_next)
        kb.add("s-tab")(focus_previous)
        for shortcut in self.uicard_state.shortcuts:
            kb.add(shortcut.shortcut)(shortcut.callback)
        kb.add("c-q")(quit_app)

    def edit_mode(self, event):
        self.uicard_state.mode = 'edit'
        self.custom_buttons_vsplit.children = self.edit_buttons_vsplit.children
        self.layout.focus(self.edit_buttons[0])



    def fire(self):
        if self.uicard_state.frontal_editable == False:
            self.frontal_buffer.text = self.uicard_data.frontal
        if self.uicard_state.hidden_editable == False:
            if self.uicard_state.show_hidden:
                self.hidden_buffer.text = self.uicard_data.hidden
            else:
                self.hidden_buffer.text = ''
        if self.uicard_state.tag_editable == False:
            self.tag_buffer.text = self.uicard_data.tag



    def create_app(self):
        app = Application(key_bindings=self.kb,layout=self.layout, full_screen=True)
        app.before_render = self

        return app


def quit_app(event):
    exit(0)
