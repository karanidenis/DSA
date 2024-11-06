#  Memory Puzzle
# Create a Memory Puzzle game with the following requirements:
# Display a grid of hidden pairs of symbols (e.g., letters or numbers).
# Allow the player to input the coordinates of two tiles to flip them over.
# If the two tiles match, they remain revealed; if not, they flip back.
# Keep track of the player's moves and how many pairs they’ve matched.
# End the game when all pairs are matched.
# Display a congratulatory message when the game is complete.


# build puzzle ✔
# add numbers on puzzle randomly ✔
# players input - rows and columns, number is reveled, ✔
# toggle visibility - show board with visible values 
# check if numbers match ✔
# change players ✔
# check for gameover - if all values are visible 
# record everytime a player succesfully flips to determine winner
import random


def printPuzzle(puzzle):
    for row in puzzle:
        print(" | ".join(str(item) for item in row))
        print("-------------")

def playGame():
    puzzle = [[" " for _ in range(4)] for _ in range(3)]
    # print(puzzle)
    
    numbers = [0,0,0,0, 1,1,1,1, 2,2,2,2]
    for row in range(len(puzzle)):
        for col in range(len(puzzle[row])):
            number = random.choice(numbers)
            numbers.remove(number)
            if puzzle[row][col] == " ":
                puzzle[row][col] = number
    # printPuzzle(puzzle)
    
    gameOver = False
    player = 0
    while True:
        printPuzzle(puzzle)
        print(f"player {player} turn!")
        
        try:
            # Take the row and column inputs from the user as comma-separated values
            val1 = input("Enter a number 0, 1, or 2 as row and column (e.g., 0,1): ").split(',')
            val2 = input("Enter another number 0, 1, or 2 as row and column (e.g., 1,2): ").split(',')
            
            # Convert the split values into integers
            val1 = [int(v) for v in val1]
            val2 = [int(v) for v in val2]
        
        except ValueError:
            print("Invalid input! Please enter numbers in the format 'row,column' (e.g., 0,1).")
            continue
        
        # Check if the input values are within the range 0-2 for both rows and columns
        if (val1[0] not in range(3) or val1[1] not in range(4) or
            val2[0] not in range(3) or val2[1] not in range(4)):
            print("Please enter numbers between 0 and 2!")
            continue
        
        # Assign the row and column values
        row_1, column_1 = val1[0], val1[1]
        row_2, column_2 = val2[0], val2[1]
            
        played = puzzle[row_1][column_1], puzzle[row_2][column_2]
        print(f"Player {player} played {played}") 
        
        
        if played[0] == played[1]:
            print(f"player {player} won!")
            break
        player = 1 if player == 0 else 0
        
        continue   
        
            
        

if __name__=='__main__':
    playGame()