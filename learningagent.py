class LearningAgent:
    def __init__(self, environment):
        self.environment = environment
        self.start = list(environment.keys())[0]
        self.knowledge = {}  # Stores learned paths

    def learn(self, goal):
        self.knowledge[goal] = self.bfs(goal)  # Learn BFS path

    def bfs(self, goal):
        queue = deque([(self.start, [self.start])])
        while queue:
            node, path = queue.popleft()
            if node == goal:
                return path
            for neighbor in self.environment[node]:
                queue.append((neighbor, path + [neighbor]))
        return []

    def act(self, goal):
        if goal in self.knowledge:
            return f"Using learned path: {' → '.join(self.knowledge[goal])}"
        return "Path not learned yet."

agent = LearningAgent(graph)
agent.learn('G')
print(agent.act('G'))
