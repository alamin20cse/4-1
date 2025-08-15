import random 
class Enviroment:
    def __init__(self):
        self.rooms={'A':random.choice(['Clean','Dirty']),
                    'B':random.choice(['Clean','Dirty']),
                    
                    }
        self.agent_location=random.choice(['A','B'])