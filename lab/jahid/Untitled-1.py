from collections import deque

class MapEnvi:
    def __init__(self):
    self.graph = {
        'A': ('B': 2, 'C' : 4),
        'B': ('B': 2, 'C' : 4),
        'F': ('C': 6, 'E' : 1, )
        'G': ('F': 2)
    }

    def get_neighbors(self, city):
        return self.graph.get(city, ())
    def get_cost(self, from_city, to_city):
        return self.graph[from_city].get(to_city, float('inf'))
    
    class RouterFinding:
        def __init__(self, environment):
            