class UICardButton:
    title = ''
    callback = None

    def __init__(self, title, callback=None):
        self.title = title
        self.callback = callback
        if callback is None: self.callback = self.clicked

    def clicked(event):
        pass
