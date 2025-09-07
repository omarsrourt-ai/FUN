def request_input(grid, player):
    
    x = input(f'Player {player}, choose a column (1-7): ')

    if x.isdigit():
        column = int(x)
        if 1 <= column <= 7:
            for i in range(len(grid)-1, -1, -1):  
                if grid[i][column - 1] == '':
                    return (i + 1, column)
            return -2  
        else:
            return -1  
    else:
        return -1  


def make_move(grid, row, column, player):
    
    A = grid[row-1] 
    A[column-1] = player
    return grid
        

def check_row(grid, player):
     
    for i in grid:
        W = 0
        for j in range(len(i)-1):
            if i[j] == player:
                
                if i[j] == i[j+1]:
                    W += 1
                    
                    if W == 3: 
                        return True
                    
                else: W = 0
             
    return False
                   
def check_column(grid, player):

    for j in range(len(grid[0])):  
        W = 0
        for i, row in enumerate(grid):  
            if row[j] == player:
                W += 1
                if W == 4: 
                    return True
            else:
                W = 0  
    return False

def check_diag(grid, player):
       
    rows = len(grid)
    cols = len(grid[0])

    
    for i in range(rows - 3):
        for j in range(cols - 3):
            if (grid[i][j] == player and
                grid[i+1][j+1] == player and
                grid[i+2][j+2] == player and
                grid[i+3][j+3] == player):
                return True

    
    for i in range(3, rows):
        for j in range(cols - 3):
            if (grid[i][j] == player and
                grid[i-1][j+1] == player and
                grid[i-2][j+2] == player and
                grid[i-3][j+3] == player):
                return True

    return False

def is_draw(grid):
    
    for i in grid:
        if '' not in i:
            if check_row(grid, 'X') == False and check_diag(grid, 'X') == False and check_column(grid, 'X') == False:
                return True
            
            else: return False
            
        else: return False

def display_grid(grid):

    for row in grid:
        print('| ' + ' | '.join(row) + ' |')
        print('+' + '-' * 29 + '+')
        
    return None


def play_game(grid):

    current_player = 'X'
    game_over = False

    while not game_over:
        display_grid(grid)
        
        move = request_input(grid, current_player)

        if move == -1:
            print("Invalid Response")
            continue
        elif move == -2:
            print("Column you selected has no empty slots.")
            continue

        row, column = move
        grid = make_move(grid, row, column, current_player)

        if check_row(grid, current_player) or check_column(grid, current_player) or check_diag(grid, current_player):
            display_grid(grid)
            print(f"Congratulations! Player {current_player} won.")
            game_over = True
            
        elif is_draw(grid):
            display_grid(grid)
            print("Game is a draw")
            game_over = True
            
        else:
            current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    grid =   [['','','','','','',''],
              ['','','','','','',''],
              ['','','','','','',''],
              ['','','','','','',''],
              ['','','','','','',''],
              ['','','','','','','']]
    pass
 
# print(request_input(grid, 'X'))
# print(make_move(grid, 6, 1, 'X'))
# print(check_row(grid, 'X'))
# print(check_column(grid,'X'))
# print(check_diag(grid,'O'))
# print(is_draw(grid))
# display_grid(grid)
play_game(grid)
