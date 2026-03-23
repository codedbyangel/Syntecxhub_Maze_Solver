import heapq

maze = [
    [0, 0, 0, 1],
    [0, 1, 0, 0],
    [0, 1, 0, 0]
]

start = (0, 0)
goal = (2, 3)

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    came_from = {}
    g_cost = {start: 0}
    
    while open_list:
        _, current = heapq.heappop(open_list)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        
        x, y = current
        
        neighbors = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
        
        for nx, ny in neighbors:
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0:
                new_cost = g_cost[current] + 1
                
                if (nx, ny) not in g_cost or new_cost < g_cost[(nx, ny)]:
                    g_cost[(nx, ny)] = new_cost
                    f_cost = new_cost + heuristic((nx, ny), goal)
                    heapq.heappush(open_list, (f_cost, (nx, ny)))
                    came_from[(nx, ny)] = current
    
    return "No Path Found"

path = astar(maze, start, goal)
path = astar(maze, start, goal)

for i in range(len(maze)):
    for j in range(len(maze[0])):
        if (i, j) == start:
            print("S", end=" ")
        elif (i, j) == goal:
            print("G", end=" ")
        elif (i, j) in path:
            print("*", end=" ")
        elif maze[i][j] == 1:
            print("#", end=" ")
        else:
            print(".", end=" ")
    print()