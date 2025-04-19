class Node:
    
    def __init__(self, value):
        self.value = value
        self.outbound = []
        self.inbound = []
        
    def point_to(self, other):
        self.outbound.append(other)
        other.inbound.append(self)
        
    def __str__(self):
        return f'Node({self.value})'
    
class Graph:
    def __init__(self, root):
        self._root = root
        
    def dfs(self):
        visited = [] #пройденые вершины
        stack = [self._root] # стек для вершин соседей
        
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.append(current)
                
                for neighbor in reversed(current.outbound):
                    if neighbor not in visited:
                        stack.append(neighbor)
                        
        return [node.value for node in visited] 
  
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)

g = Graph(a)

print(g.dfs())