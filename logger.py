class Logger:
    def __init__(self, prefix='None'):
        self.prefix = prefix

    def log(self, data: str):
        if self.prefix:
            print(f"{self.prefix} {data}")
        else:
            print(data)

    def input(self, text: str):
        if self.prefix:
            return input(f"{self.prefix} {text}")
        else:
            return input(text)