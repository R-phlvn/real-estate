class Manager:
    def __init__(self, _class=None):
        self._class = _class

    def search(self, **kwargs):
        result = list()
        for key, value in kwargs.items():
            for obj in self._class.object_list:
                if hasattr(obj, key) and getattr(obj, key) == value:
                    result.append(obj)
        return result