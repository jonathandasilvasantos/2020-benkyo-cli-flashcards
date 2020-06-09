from view.model.uicardshortcut import UICardShortcut

class UICardState:
    toolbars = []
    frontal_editable = False
    hidden_editable = False
    tag_editable = False
    show_hidden = False
    mode = ''
    shortcuts = []

    def __init__(self, toolbars, frontal_editable=False, hidden_editable=False, tag_editable=False, show_hidden=False, mode='custom', shortcuts=[]):
        self.mode = mode
        self.toolbars = toolbars
        self.frontal_editable = frontal_editable
        self.hidden_editable = hidden_editable
        self.tag_editable = tag_editable
        self.show_hidden = show_hidden
        self.shortcuts = shortcuts
