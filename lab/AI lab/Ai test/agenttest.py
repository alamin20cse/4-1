from collections import deque
class EnvMap:
    def __init__(self):
        self.graph={
             'A':{'B':2,'C':4},
            'B':{'A':2,'D':3,'E':5},
            'C':{'A':4,'F':6},
            'D':{'B':3},
            'E':{'B':5,'F':1},
            'F':{'C':6,'E':1,'G':2},
            'G':{'F':2}

        }
    def getNighbar(self,city):
        return self.graph.get(city,{})
    def getCost(self,formcity,tocity):
        return self.graph[formcity].get(tocity,float('inf'))
class RouteFinding:
    def __init__(self,enviornment):
        self.env=enviornment
    def bfs(self,start,goal):
        queue=deque()
        queue.append((start,[start]))
        visited=set()
        while queue:
            current,path=queue.popleft()
            if current==goal:
                return path
            if current in visited:
                continue
            visited.add(current)

            for neighbar in self.env.getNighbar(current):
                if neighbar not in visited:
                    queue.append((neighbar,path+[neighbar]))
        return None
    

    def  calculate_cost(self,path):
        if not path or len(path)<2:
            return 0
        total_cost=0
        for i in range(len(path)-1):
            fromCity=path[i]
            toCity=path[i+1]
            cost=self.env.getCost(fromCity,toCity)
            total_cost+=cost
        return total_cost


    


env=EnvMap()
agent=RouteFinding(env)

startcity='A'
goalcity='G'
path=agent.bfs(startcity,goalcity)
cost=agent.calculate_cost(path)

print(f"Path from {startcity} to {goalcity} : {path}")
print(f"Total path cost :{cost}")
