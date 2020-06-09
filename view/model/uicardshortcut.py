class UICardShortcut:
    title = ''
    shortcut = ''
    callback = None
    def __init__(self, title, shortcut, callback):
        self.title = title
        self.shortcut = shortcut
        self.callback = callback
