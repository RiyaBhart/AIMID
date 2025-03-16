import heapq

class UtilityBasedAgent:
    def __init__(self, environment, costs):
        self.environment = environment
        self.costs = costs
        self.start = list(environment.keys())[0]

    def bfs(self, goal):
        queue = [(0, self.start, [self.start])]  # (cost, node, path)
        while queue:
            cost, node, path = heapq.heappop(queue)
            print("Visiting:", node, "Cost:", cost)
            if node == goal:
                return f"Optimal Path: {' → '.join(path)} with cost {cost}"
            for neighbor in self.environment[node]:
                heapq.heappush(queue, (cost + self.costs[(node, neighbor)], neighbor, path + [neighbor]))
        return "Goal not found"

graph_weighted = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [], 'E': [], 'F': [], 'G': []
}

costs = {('A', 'B'): 2, ('A', 'C'): 3, ('B', 'D'): 4, ('B', 'E'): 1, ('C', 'F'): 5, ('C', 'G'): 2}

agent = UtilityBasedAgent(graph_weighted, costs)
print(agent.bfs('G'))
