from queue import PriorityQueue

graph = {
    'A': [('B', 5, 9), ('C', 8, 5)],  
    'B': [('D', 10, 4)],  
    'C': [('E', 3, 7)],  
    'D': [('F', 7, 5)],  
    'E': [('F', 2, 1)],  
    'F': []  
}

def astar(graph,start,goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((0,start,0))
    
    while not pq.empty():
        f_value,node,cost=pq.get()
        
        if node in visited:
            continue
        
        print(node,end=' ')
        visited.add(node)
        
        if node == goal:
            print("goal reached")
            return True
        
        for neighbor,edge_cost,heuristic in graph[node]:
            if neighbor not in visited:
                new_cost = cost+edge_cost
                f_new = new_cost +heuristic
                pq.put((f_new,neighbor,new_cost))
                
        print("\ngoal not found")
        return False
print("\nA start path:")
astar(graph,'A','F')
