import random
rows = 5
cols = 5
grid = [[random.randint(0, 1) for i in range(cols)] for i in range(rows)]

for row in grid:
    print(row)

def square():
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                print(f"Cleaning dirt at ({row}, {col})")
                grid[row][col] = 0
    print("Cleaning complete. Final grid:")
    for row in grid:
        print(row)

def triangle():
    for row in range(rows):
        col=row
        if grid[row][col]==1:
            print(f"Cleaning dirt at ({row}, {col})")
            grid[row][col]=0
    print("Cleaning complete. Final grid:")
    for row in grid:
        print(row)

def circle():
    for col in range(cols):
        if grid[0][col] == 1:
            print(f"Cleaning dirt at (0, {col})")
            grid[0][col] = 0

    for row in range(1, rows - 1):
        if grid[row][cols - 1] == 1:
            print(f"Cleaning dirt at ({row}, {cols - 1})")
            grid[row][cols - 1] = 0

    for col in range(cols):
        if grid[rows - 1][col] == 1:
            print(f"Cleaning dirt at ({rows - 1}, {col})")
            grid[rows - 1][col] = 0
    
    for row in range(1, rows - 1):
        if grid[row][0] == 1:
            print(f"Cleaning dirt at ({row}, 0)")
            grid[row][0] = 0

    

    print("Cleaning complete. Final grid:")
    for row in grid:
        print(row)

choice=input("Enter the vaccum shape you need: 1,Square 2,Triangle 3,Circle>>")
if choice == "1":
    square()
    
elif choice == "2":
    triangle()
    
elif choice == "3":
    circle()
else:
    print("Wrong Number there is no shape for that option")
