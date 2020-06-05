from prompt_toolkit import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.layout.containers import VSplit, Window, HSplit
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
from prompt_toolkit.input import Input
from prompt_toolkit.widgets import Box, Button

class UICardData:
    frontal = ''
    hidden = ''
    tag = ''
    def __init__(self, frontal, hidden, tag):
        self.frontal = frontal
        self.hidden = hidden
        self.tag = tag

class UICardState:
    buttons = None
    frontal_editable = False
    hidden_editable = False
    tag_editable = False

    def __init__(self, buttons, frontal_editable=False, hidden_editable=False, tag_editable=False):
        self.buttons = buttons
        self.frontal_editable = frontal_editable
        self.hidden_editable = hidden_editable
        self.tag_editable = tag_editable


class UICardButton:
    title = ''
    callback = None

    def __init__(self, title, callback=None):
        self.title = title
        self.callback = callback
        if callback is None: self.callback = self.clicked

    def clicked(event):
        pass




class UICardCallbacks:
    updated_fields = None

    def __init__(self, updated_fields):
        self.updated_fields = updated_fields



class UICard:
    uicard_data = None
    uicard_state = None
    uicard_callbacks = None

    frontal_buffer = None
    hidden_buffer = None
    tag_buffer = None
    buttons = []

    kb = None
    layout = None

    def __init__(self, uicard_data, uicard_state, uicard_callbacks):
        self.uicard_data = uicard_data
        self.uicard_state = uicard_state
        self.uicard_callbacks = uicard_callbacks
        self.buttons_box = None




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



        for b in self.uicard_state.buttons:
            button = Button(b.title, handler=b.callback)
            self.buttons.append(button)

            self.buttons_box = Box(body=VSplit(self.buttons, padding=4), height=4)




            left_panel = Window(content=BufferControl(buffer=self.frontal_buffer), wrap_lines=True)
            right_panel = Window(content=BufferControl(buffer=self.hidden_buffer), wrap_lines=True)
            bottom_panel = self.buttons_box

            vertical_container = VSplit([
            left_panel,
            Window(width=1, char='|'),
            right_panel,
            ])

            root_container = HSplit([ vertical_container, Window(height=1, char='-'), bottom_panel])

            self.layout = Layout(root_container)

    def bind_keyboard(self):

        self.kb = KeyBindings()
        self.kb.add("tab")(focus_next)
        self.kb.add("s-tab")(focus_previous)
        ##self.kb.add("c-qab")(exit






    def fire(self):
        pass

    def create_app(self):
        self.build_ui()
        self.bind_keyboard()
        app = Application(key_bindings=self.kb,layout=self.layout, full_screen=True)
        app.before_render = self
        return app