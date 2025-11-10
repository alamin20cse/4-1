import random
class Environment:
    def __init__(self):
        self.rooms={'A':random.choice(['Dirty','Clean'])}
        print(self.rooms)