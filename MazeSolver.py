from MazeGenerator import *
import matplotlib.pyplot as plt
import random
#we should keep track of the amount of steps and the end points
#for this case we will set the end points to be the top left and top right


n = 35
maze = maze_generation(n)
maze[0][0] = 2
maze[n-1][n-1] = 3

x,y = 0,0
def solve_maze_randomly(maze_arr, x=0, y=0, steps=0):
     directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] #right, down, left, up
     #first we will implement random mouse
     #we should start at the start point
     maze[0][0] = 2
     random.shuffle(directions)
     if maze_arr[x][y] == 3:
            print("Maze Solved")
            print(steps)
            return True
     maze_arr[x][y] = 4
     
     for dx, dy in directions: 
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and maze_arr[nx][ny] in [0, 3]:
            # maze_arr[0][0] = 4 #mark start location as visited
            
            if solve_maze_randomly(maze_arr, nx, ny, steps + 1):
                return True
def hand_on_wall_rule(maze_arr, x=0, y=0, steps=0):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] #right, down, left, up
    maze[0][0] = 2
    #in this case we would not randomize location but prioritize the right hand rule
    # a wall is designated as 1 in the maze_arr
    if maze_arr[x][y] == 3:
            print("Maze Solved")
            print(steps)
            return True
    maze_arr[x][y] = 4 #mark location as visited for recursive steps
    for i in range(4):
        new_dir = (i + 1) % 4
        print(new_dir)
        dx, dy = directions[new_dir]
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and maze_arr[nx][ny] in [0, 3]:
            if hand_on_wall_rule(maze_arr, nx, ny, steps + 1):
                return True
    return False
        
        
# def Tremauxs_algorithm(maze_arr, x=0, y=0, steps=0):
#     directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] #right, down, left, up
#     maze[0][0] = 2
#     if maze_arr[x][y] == 3:
#             print("Maze Solved")
#             print(steps)
#             return True
#     maze_arr[x][y] = 4 #mark location as visited for recursive steps
    #there should be a method to keep track of the amount of times a cell has been visited
        
    
            
            
        
        
            
    
         
solve_maze_randomly(maze)
hand_on_wall_rule(maze)
print(maze)

# solve_maze_randomly(maze)

# start_location = maze[0][0]
# end_location = maze[n-1][n-1]
plt.imshow(maze) #maze representation
plt.show()

