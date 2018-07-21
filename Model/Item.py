class Item:
    def __init__(self, id, name):
        self.id = id
        self._name = name

    @property
    def name(self):
        return self._name