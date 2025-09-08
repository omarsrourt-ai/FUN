# snakes and ladders.py

def request_input(grid, current_pos):

    x = input('Enter a number (1–6) or type "exit": ').strip().lower()

    if x == 'exit':
        print('Thank you for playing')
        print('Start a new game')
        return -1

    # validate strictly numeric and within 1..6
    if not x.isdigit():
        print('Invalid input. Please enter a number from 1 to 6.')
        return 0

    v = int(x)
    if v < 1 or v > 6:
        print('Invalid input. Please enter a number from 1 to 6.')
        return 0

    return v


def _build_board_map(grid):

    mapping = {}
    for row in grid:
        for cell in row:
            n = cell[0]
            if len(cell) >= 3 and cell[1] in ('L', 'S'):
                mapping[n] = (cell[1], cell[2])
            else:
                mapping[n] = ('N', n)
    return mapping


def make_move(grid, current_pos, moves):

    target = current_pos + moves
    if target >= 30:
        # Reaching or passing the last square means win on 30
        return 30

    board = _build_board_map(grid)

    # Apply snake or ladder if present
    if target in board:
        kind, dest = board[target]
        if kind == 'L':
            print('Hooray! You climbed a ladder!')
            return dest
        elif kind == 'S':
            print('Oops! You got bitten by a snake!')
            return dest
        else:
            return target

    # Fallback (shouldn’t happen with a valid board)
    return target


def display_grid(grid, pos):

    # Collect numbers in board order by rows
    numbers = []
    for row in grid:
        row_nums = [cell[0] for cell in row]
        numbers.append(row_nums)



    # Build a flat sorted list 1..30
    all_nums = sorted({cell[0] for row in grid for cell in row})

    # Place a star on current position (only for 1..30)
    cells = [str(n) for n in all_nums]
    if 1 <= pos <= 30:
        cells[pos - 1] = '☆'

    # Re-slice into rows of 6
    rows = [cells[i:i+6] for i in range(0, 30, 6)]


    rows[1] = list(reversed(rows[1]))
    rows[3] = list(reversed(rows[3]))

    # Print from top to bottom
    print("|" + "|".join(rows[4]) + "|")
    print("|" + "|".join(rows[3]) + "|")
    print("|" + "|".join(rows[2]) + "|")
    print("|" + "|".join(rows[1]) + "|")
    print("|" + "|".join(rows[0]) + "|")


def play_game(grid):

    current_pos = 0
    print("\nWelcome to Snakes & Ladders!")
    display_grid(grid, current_pos)

    while True:
        roll = request_input(grid, current_pos)
        if roll == -1:
            # user typed 'exit'
            break
        if roll == 0:
            # invalid input; prompt again
            continue

        # valid roll
        new_pos = make_move(grid, current_pos, roll)
        print(f'You rolled a {roll} and moved from {current_pos} to {new_pos}.')
        current_pos = new_pos
        display_grid(grid, current_pos)

        if current_pos == 30:
            print("🎉 You win! Reached 30. Game over.")
            break


################## FOR TESTING ####################
if __name__ == '__main__':
    grid = [
        [[25], [26],        [27, 'S', 1],  [28],       [29],        [30]],
        [[24], [23],        [22],          [21, 'S', 9],[20, 'L', 29],[19, 'S', 7]],
        [[13], [14],        [15],          [16],       [17, 'S', 4], [18]],
        [[12], [11, 'L', 26],[10],          [9],        [8],         [7]],
        [[1],  [2],         [3, 'L', 22],  [4],        [5, 'L', 8],  [6]],
    ]

    play_game(grid)
