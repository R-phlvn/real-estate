class Manager:
    def __init__(self, _class=None):
        self._class = _class

    def search(self, **kwargs):
        result = list()
        for key, value in kwargs.items():
            if key.endswith('__min'):
                key = key[:-5]
                compare_key = 'min'
            elif key.endswith('__max'):
                key = key[:-5]
                compare_kay = 'max' 
            else:
                compare_key = 'equal'
            for obj in self._class.object_list:
                if hasattr(obj, key):
                    if compare_key == 'min':
                        status = bool(getattr(obj, key) >= value)
                    elif compare_key == 'max':
                        status = bool(getattr(obj, key) <= value)
                    else:
                        status = bool(getattr(obj, key) <= value)
                    if status:
                        result.append(obj)
        return result
    
    def get(self, **kwargs):
        for key, value in kwargs.items():
            for obj in self._class.object_list:
                if hasattr(obj, key) and getattr(obj, key) == value:
                    return obj
        return None