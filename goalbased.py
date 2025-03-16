class GoalBasedAgent:
    def __init__(self, environment):
        self.environment = environment
        self.start = list(environment.keys())[0]

    def bfs(self, goal):
        queue = deque([(self.start, [self.start])])  # Track paths
        while queue:
            node, path = queue.popleft()
            print("Visiting:", node)
            if node == goal:
                return f"Shortest Path: {' → '.join(path)}"
            for neighbor in self.environment[node]:
                queue.append((neighbor, path + [neighbor]))
        return "Goal not found"

    def dfs(self, goal):
        stack = [(self.start, [self.start])]
        while stack:
            node, path = stack.pop()
            print("Visiting:", node)
            if node == goal:
                return f"Path Found: {' → '.join(path)}"
            for neighbor in self.environment[node]:
                stack.append((neighbor, path + [neighbor]))
        return "Goal not found"

agent = GoalBasedAgent(graph)
print(agent.bfs('G'))
print(agent.dfs('G'))
