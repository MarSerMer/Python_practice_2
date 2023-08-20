class Homework13Exception(Exception):
    pass

class SideException(Homework13Exception):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f'Side of the rectangle should be over zero. You entered {self.side}'

class HumanNameException(Homework13Exception):
    def __init__(self, name, min_l:int = 1, max_l:int = 40):
        self.name = name
        self.min_l = min_l
        self.max_l = max_l

    def __str__(self):
        return f'Wrong enter: "{self.name}"! It should be from {self.min_l} to {self.max_l} long.'