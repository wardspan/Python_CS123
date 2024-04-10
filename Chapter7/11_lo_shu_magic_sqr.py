# This program will ask the user for a two-dimensional list. A function accepts a two-dimensional list 
# from the user as an argument and determines whether the list is a Lo Shu Magic Square. 
# A Lo Shu Magic Square, is a grid with 3 rows and 3 columns that has the following properties:
# - The grid contains the numbers 1 through 9 exactly.
# - The sum of each row, each column, and each diagonal all add up to the same number.

def is_loshu_magic_square(grid):
    # Check if the grid contains the numbers 1 through 9 exactly
    numbers = set()
    for row in grid:
        for num in row:
            numbers.add(num)
    if numbers != set(range(1, 10)):
        return False
    
    # Calculate the sum of the first row
    target_sum = sum(grid[0])
    
    # Check if the sum of each row is equal to the target sum
    for row in grid:
        if sum(row) != target_sum:
            return False
    
    # Check if the sum of each column is equal to the target sum
    for col in range(len(grid[0])):
        col_sum = sum(row[col] for row in grid)
        if col_sum != target_sum:
            return False
    
    # Check if the sum of the main diagonal is equal to the target sum
    diagonal_sum = sum(grid[i][i] for i in range(len(grid)))
    if diagonal_sum != target_sum:
        return False
    
    # Check if the sum of the secondary diagonal is equal to the target sum
    secondary_diagonal_sum = sum(grid[i][len(grid)-1-i] for i in range(len(grid)))
    if secondary_diagonal_sum != target_sum:
        return False
    
    # If all checks pass, the grid is a Lo Shu Magic Square
    return True

def main():
    # Prompt the user to enter a 3x3 grid
    grid = []
    for i in range(3):
        row = input(f"Enter row {i+1}: Use a space between numbers ").split()
        row = [int(num) for num in row]
        grid.append(row)

    # Call the function to check if the grid is a Lo Shu Magic Square
    if is_loshu_magic_square(grid):
        print("The grid is a Lo Shu Magic Square.")
    else:
        print("The grid is not a Lo Shu Magic Square.")
        
if __name__ == '__main__':
    main()
    