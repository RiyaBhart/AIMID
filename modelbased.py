class ModelBasedReflexAgent:
    def __init__(self, environment):
        self.environment = environment
        self.start = list(environment.keys())[0]
        self.visited = set()  # Memory

    def bfs(self, goal):
        queue = deque([self.start])
        while queue:
            node = queue.popleft()
            if node in self.visited:
                continue  # Skip revisited nodes
            print("Visiting:", node)
            self.visited.add(node)
            if node == goal:
                return f"Goal {goal} found!"
            queue.extend(self.environment[node])
        return "Goal not found"

    def dfs(self, goal):
        stack = [self.start]
        while stack:
            node = stack.pop()
            if node in self.visited:
                continue
            print("Visiting:", node)
            self.visited.add(node)
            if node == goal:
                return f"Goal {goal} found!"
            stack.extend(self.environment[node])
        return "Goal not found"

agent = ModelBasedReflexAgent(graph)
print(agent.bfs('G'))
print(agent.dfs('G'))
