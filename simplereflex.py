from collections import deque

class SimpleReflexAgent:
    def __init__(self, environment):
        self.environment = environment  # Graph structure
        self.start = list(environment.keys())[0]  # Pick first node as start

    def bfs(self, goal):
        queue = deque([self.start])
        while queue:
            node = queue.popleft()
            print("Visiting:", node)
            if node == goal:
                return f"Goal {goal} found!"
            queue.extend(self.environment[node])  # No memory, just reacts
        return "Goal not found"

    def dfs(self, goal):
        stack = [self.start]
        while stack:
            node = stack.pop()
            print("Visiting:", node)
            if node == goal:
                return f"Goal {goal} found!"
            stack.extend(self.environment[node])  # No memory
        return "Goal not found"

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [], 'E': [], 'F': [], 'G': []
}

agent = SimpleReflexAgent(graph)
print(agent.bfs('G'))
print(agent.dfs('G'))
