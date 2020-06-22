from prompt_toolkit.widgets import Button
from prompt_toolkit.layout.containers import VSplit
class UICardToolbar:

    title = ''
    id = ''
    buttons = []
    prompt_buttons = []

    def __init__(self, id, title, buttons):
        self.id = id
        self.title = title
        self.buttons = buttons
        self.prompt_buttons = []
        for button in buttons:
            prompt_button = Button(button.title, handler=button.callback)
            self.prompt_buttons.append(prompt_button)

        self.toolbar_panel = VSplit(self.prompt_buttons, padding=4)

def get_toolbar(toolbars, id):
    for toolbar in toolbars:
        if toolbar.id == id:
            return toolbar
    return None
