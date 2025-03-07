# we want to generate a nxn maze using a png file that we can edit
# dfs algorithm for maze generation
# capture png
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.image as img 
import random
  
# reading png image file 

    
    
maze_cell = img.imread('maze_cell.png')
def maze_generation(n):
    maze = np.ones((n,n), dtype=int) # generates nxn maze for traversal
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] #right, down, left, up
    # utilizing dfs
    def dfs(x,y): # given a current cell as a  parameter
        maze[x][y] = 0 # marks cell as visited
        random.shuffle(directions) # randomize directions
        for dx, dy in directions: # while current cell has any unvisited neighbors
            nx, ny = x + dx * 2, y + dy * 2  # Move two steps in the chosen direction
            if 0 <= nx < n and 0 <= ny < n and maze[nx][ny] == 1:
                #visit random direction
                 maze[x + dx][y + dy] = 0 #remove wall
                 dfs(nx, ny) #recursively visit
    def iterative_maze_generation(x,y):
        stack = [] # stack to keep track of visited cells
        maze[x][y] = 0
        stack.append((x,y))
        
        while stack:
           
            x,y = stack.pop()
            # random.shuffle(directions)
            random.shuffle(directions)
            for dx, dy in directions:
                nx, ny = x + dx * 2, y + dy * 2
                if 0 <= nx < n and 0 <= ny < n and maze[nx, ny] == 1:
                    
                     maze[x + dx][y + dy] = 0 #remove wall
                     maze[nx][ny] = 0
                     stack.append((nx,ny))       
    #make a goal and start point
    
    def recursize_maze_gen(x,y):
        maze[x][y] = 0
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 <= nx < n and 0 <= ny < n and maze[nx, ny] == 1:
                maze[x + dx][y + dy] = 0
                recursize_maze_gen(nx,ny)
    
    dfs(0,0)  
    # iterative_maze_generation(0,0)
    recursize_maze_gen(0,0)
    
    return maze



#only input odd numbers for maze generation
n = 35
maze = maze_generation(n)   
# maze = recursive_maze_gen(n)
plt.imshow(maze) #maze representation
plt.show()

# # maze = iterative_maze_generation(0,0)
# print(maze)
    
    