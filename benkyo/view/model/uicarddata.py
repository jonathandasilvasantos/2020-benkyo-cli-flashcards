class UICardData:
    id = -1
    frontal = ''
    hidden = ''
    tag = ''
    def __init__(self, id, frontal, hidden, tag):
        self.id = id
        self.frontal = frontal
        self.hidden = hidden
        self.tag = tag

        # Backup values to restore during an editing canceled process
        self._frontal = frontal
        self._hidden = hidden
        self._tag = tag
