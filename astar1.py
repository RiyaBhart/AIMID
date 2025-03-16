graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 4, 'E': 3},
    'C': {'F': 1, 'G': 5},
    'D': {'H': 2},
    'E': {},
    'F': {'I': 6},
    'G': {},
    'H': {},
    'I': {}  # Goal node
}
heuristic = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 4,
    'E': 7,
    'F': 3,
    'G': 6,
    'H': 2,
    'I': 0  # Goal node
}
def astar(graph,start,goal):
    frontier =[(start,heuristic[start])]
    visited = set()
    g_costs={start: 0}
    came_from = {start:None}
    while frontier:
        frontier.sort(key=lambda x:x[1])
        current_node,current_f = frontier.pop(0)
        
        if current_node in visited:
            continue
        
        print(current_node,end=" ")
        visited.add(current_node)
        
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node=came_from[current_node]
            path.reverse()
            print("\nGoal found with A*. Path : ",path)
            return
        for neighbour,cost in graph[current_node].items():
            new_g_cost = g_costs[current_node]+cost
            f_cost = new_g_cost+heuristic[neighbour]
            
            if neighbour not in g_costs or new_g_cost<g_costs[neighbour]:
                g_costs[neighbour]=new_g_cost 
                came_from[neighbour]=current_node
                frontier.append((neighbour,f_cost))
                
    print("\ngoal not found") 
    
print("\nFollowing is the A* Search:")
astar(graph, 'A', 'I')
 
        
    
