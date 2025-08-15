import random

class Enviornment:
    def __init__(self):
        self.roooms={
            'A':random.choice(['Clean','Dirty']),
            'B':random.choice(['Clean','Dirty'])
        }

        self.agent_location=random.choice(['A','B'])

    def is_dirty(self,location):
        return self.roooms[location]=='Dirty'
    def is_clean(self,location):
        return self.roooms[location]=='Clean'
    def move(self,new_location):
        self.agent_location=new_location


    def randomly_dirty_rooms(self,probability=0.3):
        for room in self.roooms:
            if self.roooms[room]=='Clean' and random.random()<probability:
                self.roooms[room]='Dirty'
                print(f"Enviroment : room {room} got dirty agin !")