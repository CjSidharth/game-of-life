from random import random
from time import sleep
from blessed import Terminal
term = Terminal()

def dead_state(width,height):
    return [[ 0 for _ in range(width)] for _ in range(height)]

def random_state(width,height):
    grid = dead_state(width,height)
    for i in range(height):
        for j in range(width):
            if random() >= 0.3:
                grid[i][j] = 1
            else:
                grid[i][j] = 0
    return grid


def render_bless(grid):
    print(term.home + term.seagreen2_on_black + term.clear,end='')
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                print("█"*2,end='')
            else:
                print(" "*2,end='')
        print("")
    sleep(0.09)



def render(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                print("#"*2,end='')
            else:
                print("‧"*2,end='')
        print("")
    sleep(0.09)

def rules(grid,i,j,sum):
    if grid[i][j] == 1:
        if sum == 0 or sum == 1 or sum > 3:
            return 0
        else:
            return 1
    else:
        if sum == 3:
            return 1
        else:
            return 0

def next_board_state(grid):
    temp_grid = dead_state(len(grid[0]),len(grid))
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0 and j == 0:
                sum = grid[i+1][j] + grid[i+1][j+1] + grid[i][j+1]
                temp_grid[i][j] = rules(grid,i,j,sum)
            elif i == len(grid)-1 and j == len(grid[0])-1:
                sum = grid[i-1][j-1] + grid[i][j-1] + grid[i-1][j]
                temp_grid[i][j] = rules(grid,i,j,sum)
            elif i == len(grid)-1 and j == 0:
                sum = grid[i][j+1] + grid[i-1][j] + grid[i-1][j+1]
                temp_grid[i][j] = rules(grid,i,j,sum)
            elif i == 0 and j == len(grid[0])-1:
                sum = grid[i+1][j] + grid[i+1][j-1] + grid[i][j-1]
                temp_grid[i][j] = rules(grid,i,j,sum)
            elif i == 0:
                sum = grid[i][j-1] + grid[i][j+1] + grid[i+1][j] + grid[i+1][j-1] + grid[i+1][j+1]
                temp_grid[i][j] = rules(grid,i,j,sum)
            elif i == len(grid)-1:
                sum = grid[i][j-1] + grid[i][j+1] + grid[i-1][j] + grid[i-1][j-1] + grid[i-1][j+1]
                temp_grid[i][j] = rules(grid,i,j,sum)
            elif j == 0:
                sum = grid[i-1][j] + grid[i+1][j] + grid[i-1][j+1] + grid[i][j+1] + grid[i+1][j+1]
                temp_grid[i][j] = rules(grid,i,j,sum)
            elif j == len(grid[0])-1:
                sum = grid[i-1][j] + grid[i+1][j] + grid[i-1][j-1] + grid[i][j-1] + grid[i+1][j-1]
                temp_grid[i][j] = rules(grid,i,j,sum)
            else:    
                sum = grid[i+1][j] + grid[i-1][j] + grid[i][j-1] + grid[i][j+1] + grid[i-1][j-1] + grid[i-1][j+1] + grid[i+1][j-1] + grid[i+1][j+1]
                temp_grid[i][j] = rules(grid,i,j,sum)
    return temp_grid
    
def load_board_state(path):
    grid = []
    with open(path,"r") as file:
        return [[ord(i)-ord('0') for i in line if i != '\n'] for line in file]    

def main():
    choice = int(input("Enter 1 for random input and 2 for custom input in text: "))
    if choice == 1:
        try:
            height = int(input("Enter height: "))
            width = int(input("Enter width: "))
            x = random_state(width,height)
            render_bless(x)
            while True:
                x = next_board_state(x)
                render_bless(x)
        except ValueError:
            print("Enter in proper integer")
    else:
        try:
            path = input("Enter file name: ")
            y = load_board_state(path)
            render_bless(y)
            while True:
                y = next_board_state(y)
                render_bless(y)
        except FileNotFoundError:
            print("File was not found at the given path.")
        
       
if __name__ == "__main__":
    main()




