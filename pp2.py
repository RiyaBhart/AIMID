from queue import PriorityQueue

grid = [
    [1, 2, 3, '#', 4],
    [1, '#', 1, 2, 2],
    [2, 3, 1, '#', 1],
    ['#', '#', 2, 1, 1],
    [1, 1, 2, 2, 1]
]

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan Distance

def astar(grid, start, goal):
    N, M = len(grid), len(grid[0])
    pq = PriorityQueue()
    pq.put((0 + heuristic(start, goal), 0, start, [start]))  # (f, g, node, path)
    visited = set()

    while not pq.empty():
        _, g, (r, c), path = pq.get()

        if (r, c) in visited:
            continue
        visited.add((r, c))

        if (r, c) == goal:
            return path, g  

        for dr, dc in MOVES:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] != '#':
                new_cost = g + grid[nr][nc]
                f = new_cost + heuristic((nr, nc), goal)
                pq.put((f, new_cost, (nr, nc), path + [(nr, nc)]))

    return None, float('inf')

start = (0, 0)
goal = (len(grid) - 1, len(grid[0]) - 1)

path, cost = astar(grid, start, goal)

if path:
    print("\nOptimal Path:", path)
    print("Minimum Cost:", cost)
else:
    print("No path found!")
