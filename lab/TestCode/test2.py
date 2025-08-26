import random 

class Enviornment:
    def __init__(self):
        self.rooms={
            'A':random.choice(['Dirty','Clean']),
            'B':random.choice(['Dirty','Clean'])
        }

        self.aget_location=random.choice(['A','B'])

    def is_dirty(self,location):
        return self.rooms[location]=='Dirty'
    def is_clean(self,location):
        return self.rooms[location]=='Clean'
    def move(self,new_location):
        self.aget_location=new_location


class RF:
    def __init__(self,env:Enviornment):
        pass