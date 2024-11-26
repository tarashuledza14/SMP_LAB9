class MenuItem:
    def __init__(self, key: str, description: str, func: callable, args: list = ()):
        self.key = key
        self.description = description
        self.func = func
        self.args = args