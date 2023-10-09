def print_row(values):
    print('     |     |     ')
    print(' ' ,values[0] ,' | ' ,values[1] ,' |  ' ,values[2] )
    print('_____|_____|_____')

def board():
    print('\n\n\tTic Tac Toe\n\n')
    print('Player 1 (X)  -  Player 2 (O)\n' ) 

    print_row(square[1:4])
    print_row(square[4:7])
    print('     |     |     ')
    print(' ' ,square[7] ,' | ' ,square[8] ,' |  ' ,square[9] )
    print('     |     |     ')
def check_win():
    # Define the winning combinations
    winning_combinations = [
        [square[1], square[2], square[3]],  # first row
        [square[4], square[5], square[6]],  # second row
        [square[7], square[8], square[9]],
        [square[1], square[4], square[7]],
        [square[2], square[5], square[8]],
        [square[3], square[6], square[9]],
        [square[1], square[5], square[9]],
        [square[3], square[5], square[7]],
    ]

    # Check each combination
    for combination in winning_combinations:
        if combination[0] == combination[1] == combination[2] != ' ':
            if combination[0] == 'X':
                return "Player 1 wins"
            elif combination[0] == 'O':
                return "Player 2 wins"
    return "No winner"  # If no winning combination is found
print_row([1, 2, 3]) 
square = [' '] + list(range(1, 10))
board()
turn = 1
while True:
    print(f"Player {turn}")
    player = int(input("Enter a number: "))
    if player < 1 or player > 9:
        break
    if square[player] != ' ':
        print("Invalid move")
    else:
        square[player] = mark
    mark = 'X' if turn == 1 else 'O'
    square[player] = mark
    board()
    result = check_win()
    if result != "No winner":
        print("RESULT:")
        print(result)
        break
    turn = 1 if turn == 2 else 2


