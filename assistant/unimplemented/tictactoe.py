from colorama import Fore, Back, Style, init

init()

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def draw_board(b):
    print(Fore.MAGENTA, end="")
    print("╔═══╦═══╦═══╗")
    for i in range(3):
        print("║", board[0 + i * 3], "║", board[1 + i * 3], "║", board[2 + i * 3], "║")
        if i < 2:
            print("╠═══╬═══╬═══╣")
        else:
            print("╚═══╩═══╩═══╝")
    print(Style.RESET_ALL, end="")


def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input(f"Which slot will be taken by {player_token}? (1-9): ")
        try:
            player_answer = int(player_answer)
        except ValueError:
            print("Invalid answer...")
            continue
        if 1 <= player_answer <= 9:
            if str(board[player_answer - 1]) not in "XO":
                board[player_answer - 1] = player_token
                valid = True
            else:
                print("Cell is occupied...")
        else:
            print("Incorrect input...")


def check_win(b):
    win_coord = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    )
    for e in win_coord:
        if board[e[0]] == board[e[1]] == board[e[2]]:
            return board[e[0]]
    return False


def main(b):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)


main(board)
