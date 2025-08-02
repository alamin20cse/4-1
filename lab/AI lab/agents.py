import random 
class Enviroment:
    def __init__(self):
        self.rooms={'A':random.choice(['Clean','Dirty']),
                    'B':random.choice(['Clean','Dirty']),
                    
                    }
        self.agent_location=random.choice(['A','B'])
    def is_dirty(self,location):
        return self.rooms[location]=='Dirty'
    def is_clean(self,location):
        return self.rooms[location]=='Clean'
    def move (self,new_location):
        self.agent_location=new_location
    
    def randomly_dirty_rooms(self,probability=0.3):
        for room in self.rooms:
            if self.rooms[room]=='Clean' and random.random()<probability:
                self.rooms[room]='Dirty'
                print(f"Enviroment : room {room} got dirty agin !")
        
    def display(self):
        print(f"Adnt is in room {self.agent_location}")
        print(f"Room A: {self.rooms['A']}, Room B :{self.rooms['B']}")
    
    
    
class ReflexVacuumAgent:
    def act(self,env:Enviroment):
        location=env.agent_location
        if env.is_dirty(location):
            print(f"Action : Suck dirty room ")
            env.is_clean(location)
        elif location=='A':
            print(f'Action : Mov right to room  B ')
            env.move("B")
        
        elif location=='B':
            print(f'Action : Mov right to room  A ')
            env.move("A")
env=Enviroment()
agent=ReflexVacuumAgent()

for step in range(10):
    print(f'\nstep {step+1}')
    env.display()
    agent.act(env)
    env.randomly_dirty_rooms(probability=0.3)           
        