from collections import deque

# Define the grid
grid = [
    ['O', 'O', 'X', 'O', 'T'],
    ['O', 'X', 'O', 'O', 'X'],
    ['P', 'O', 'O', 'X', 'O'],
    ['X', 'X', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'X', 'O']
]

# Define possible movements (Up, Down, Right)
MOVES = [(-1, 0), (1, 0), (0, 1)]  # (row_offset, col_offset)

def find_positions(grid):
    start, target = None, None
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'P':
                start = (r, c)
            if grid[r][c] == 'T':
                target = (r, c)
    return start, target

def get_neighbors(grid, position):
    r, c = position
    neighbors = []
    for dr, dc in MOVES:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != 'X':
            neighbors.append((nr, nc))
    return neighbors

def bfs(grid, start, goal):
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        (r, c), path = queue.popleft()
        if (r, c) == goal:
            return path
        
        for neighbor in get_neighbors(grid, (r, c)):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None

def dfs(grid, start, goal):
    stack = [(start, [start])]
    visited = set([start])

    while stack:
        (r, c), path = stack.pop()
        if (r, c) == goal:
            return path
        
        for neighbor in get_neighbors(grid, (r, c)):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, path + [neighbor]))

    return None

start, goal = find_positions(grid)

if start and goal:
    bfs_path = bfs(grid, start, goal)
    dfs_path = dfs(grid, start, goal)

    print("\nBFS Path:", bfs_path)
    print("DFS Path:", dfs_path)
else:
    print("Start or Target not found in the grid!")
