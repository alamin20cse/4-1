from collections import deque
class MapEnv:
    def __init__(self):
         self.graph ={
            'A':{'B':2,'C':4},
            'B':{'A':2,'D':3,'E':5},
            'C':{'A':4,'F':6},
            'D':{'B':3},
            'E':{'B':5,'F':1},
            'F':{'C':6,'E':1,'G':2},
            'G':{'F':2}
        }
    def getNeigbar(self,city):
         return self.graph.get(city,{})
    def getCost(self,fromcity,tocity):
         return self.graph[fromcity].get(tocity,float('inf'))
    
class Routefind:
    def __init__(self,enviornment):
        self.env=enviornment
    def bfs(self,start,goal):
        queuee=deque()
        queuee.append(start,[start])
        visited=set()
        while queuee:
            current,path=queuee.popleft()
            if current==goal:
                return path
            if current in visited:
                continue
            for neighbar in self.env.getNeigbar:
                if neighbar is not visited:
                    queuee.append(neighbar,path+[neighbar])



env=MapEnv()
agent=Routefind(env)