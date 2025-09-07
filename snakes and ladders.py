def request_input(grid,current_pos):
    
    x = input('Number ')
    if x == 'exit':
        print('Thank you for playing')
        print('Start a new game')
        
        return -1
    
    elif x.isalpha() or int(x) > 6 or int(x) < 1:
        print('good2')
        
        return 0
    
    elif int(x) >= 1 and int(x) <= 6:
        print('good')
        
        return int(x)
          
    pass
    # Implement your code here

def make_move(grid, current_pos, moves):
    m = current_pos + moves
    if m <= 6:
        g = grid[4]
        
    elif m <= 12:
        g = grid[3]
        
    elif m <= 18:
        g = grid[2]
        
    elif m <= 24:
        g = grid[1]
        
    elif m <= 30:
        g = grid[0]
        
    
    for i in g:
        
        if i[0] == m:
            if len(i) > 1:
                if i[1] == 'L':
                    current_pos = i[2]
                    print ('Hooray!')
                        
                    return i[2]
                          
                elif i[1] == 'S':
                    current_pos = i[2]
                    print ('Oops!')                
                
                    return i[2]
            
            else: return i[0]

    pass
    # Implement you code here
    
def display_grid(grid, pos):
    
    l = []
    
    for i in grid:
        for j in i:
            for k in j:
                if k not in l and isinstance(k, int):
                    l.append(k)
    l2 = sorted(l)
    
    
    for i in l2:
        if pos == i:
            l2[i-1] = '☆'
    
    
    h = 0
    a = []
    b = []
    c = []
    d = []
    e = []
    
    for i in l2:
        h +=1
        if h <= 6:
            a.append(i)
        elif h <= 12:
            b.append(i)
        elif h <= 18:
            c.append(i)
        elif h <= 24:
            d.append(i)
        elif h <= 30:
            e.append(i)
    d.reverse()
    b.reverse()
            
    
    print("|" + "|".join(str(x) for x in e) + "|")
    print("|" + "|".join(str(x) for x in d) + "|")
    print("|" + "|".join(str(x) for x in c) + "|")        
    print("|" + "|".join(str(x) for x in b) + "|")
    print("|" + "|".join(str(x) for x in a) + "|")

        
    
    
#     chr(ord('U')+2606)
    
    """
    Displays the current state of the game grid with the player's position highlighted.

    Formatting Rules:
    - Each row of the grid is displayed between '|' symbols.
    - Cells are separated by '|' with no spaces between characters.
    - The player's position is displayed using the Unicode star symbol ☆ (U+2606).
    - All other cells display their numeric value or content as-is.

    Parameters:
        grid (list[list]): A 2D list representing the game board.
        pos (int): The current position of the player represented as the square number.

    Returns:
        None: The function prints the formatted grid to the console.
    """
    pass
    # Implement you code here
    
def play_game(grid):
    """
    Executes the main game loop for the Snakes and Ladders game.

    The function uses the following sequence:
    1. Displays the grid with the player at the initial position (position 0).
    2. Prompts the player for input using request_input():
        - If the input is a valid move (1–6), it proceeds with the move.
        - If the input is 'exit', the game prints a thank-you message and ends.
        - If the input is invalid, it prints an error message and prompts again.
    3. Updates the player's position using make_move(), which accounts for snakes or ladders.
    4. Displays the updated grid using display_grid() with the new position.
    5. Checks if the player has reached the final cell:
        - If so, a winning message is printed and the game ends.
        - If not, the loop continues to the next turn.

    Parameters:
        grid (list[list]): A 2D list representing the game board. Cells may contain redirections for
                           snakes and ladders or simple integer values for standard positions.

    Returns:
        None: The function runs until the player exits or wins the game.
    """
    pass
    # Implement your code here
    
################## FOR TESTING ####################
if __name__ == '__main__':
    grid=   [[[25],[26],       [27,'S',1], [28],      [29],       [30]      ],
             [[24],[23],       [22],       [21,'S',9],[20,'L',29],[19,'S',7]],
             [[13],[14],       [15],       [16],      [17,'S',4], [18]      ],
             [[12],[11,'L',26],[10],       [9],       [8],        [7]       ],
             [[1], [2],        [3,'L',22], [4],       [5,'L',8],  [6]       ]]
    
    # Write your test cases below
    # Write test cases for individual functions and check whether
    # your implementation gives the correct answer


# request_input(grid,1)
# make_move(grid, 26, 1)
# display_grid(grid, 6)
