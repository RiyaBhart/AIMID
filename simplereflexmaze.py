from collections import deque

class Environment:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.columns = len(maze[0])

    def get_neighbors(self, position):
        r, c = position
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []

        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.columns:
                if self.maze[nr][nc] in {'.', 'G'}:
                    neighbors.append((nr, nc))
        return neighbors

    def is_goal(self, position):
        r, c = position
        return self.maze[r][c] == 'G'

    def get_start_goal(self):
        start, goal = None, None
        for r in range(self.rows):
            for c in range(self.columns):
                if self.maze[r][c] == 'S':
                    start = (r, c)
                if self.maze[r][c] == 'G':
                    goal = (r, c)
        return start, goal


class SimpleReflexAgent:
    def __init__(self, environment):
        self.environment = environment
        self.start, self.goal = environment.get_start_goal()

    def bfs(self):
        queue = deque([(self.start, [self.start])])
        visited = set([self.start])

        while queue:
            (r, c), path = queue.popleft()
            print(f"Visiting: {r, c}")

            if self.environment.is_goal((r, c)):
                return path  

            for neighbor in self.environment.get_neighbors((r, c)):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))  
        return None

    def dfs(self):
        stack = [(self.start, [self.start])]
        visited = set([self.start])

        while stack:
            (r, c), path = stack.pop()
            print(f"Visiting: {r, c}")

            if self.environment.is_goal((r, c)):
                return path  

            for neighbor in self.environment.get_neighbors((r, c)):
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append((neighbor, path + [neighbor]))  
        return None


maze = [
    ['S', '.', '.', '#'],
    ['#', '#', '.', '.'],
    ['.', '.', '.', 'G']
]

env = Environment(maze)
agent = SimpleReflexAgent(env)

bfs_path = agent.bfs()
dfs_path = agent.dfs()

print("\nBFS Path:", bfs_path)
print("DFS Path:", dfs_path)
