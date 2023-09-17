import sys
import random

ALPHA = "ABCDEFGHIABCDEFGHJKLMNOPQRSTYVWYZ"
MIN_SIZE = 3
MAX_SIZE = 19
DEFAULT_SIZE = 5
DEFAULT_KOMI = 6.5
komi = DEFAULT_KOMI
board_size = DEFAULT_SIZE
board = [['.' for i in range(board_size)] for j in range(board_size)]
white_captured_stones = 0
black_captured_stones = 0
total_moves = 0

def protocol_version(cmd):
    print("2\n\n")
    
def name(cmd):
    print("KevinGo\n\n")
    
def version(cmd):
    print("0.0.1\n\n")

def known_command(cmd):
    try:
        clean_cmd = cmd.split(' ')[1].strip()
        if clean_cmd in cmd_dict:
            print("true")
            return
    except:
        pass
    print("false")

def list_commands(cmd):
    for key in cmd_dict.keys():
        print(key.replace('\n',''))

def quit(cmd):
    sys.exit()

def boardsize(cmd):
    global board_size, board
    try:
        board_size = int(cmd.split(' ')[1].strip())
        if board_size <= MAX_SIZE and board_size >= MIN_SIZE:
            print("creating board with size " + str(type(board_size)))
            board = [['.' for i in range(board_size)] for j in range(board_size)]
        else:
            print("size must be between " + str(MIN_SIZE) + " and " + str(MAX_SIZE))
    except:
        print("failed to create board with size " + str(board_size))

def showboard(cmd):
    global board
    print("  " + "A B C D E F G H J K L M N O P Q R S T Y V W Y Z"[:len(board)*2])
    for i in range(len(board)) : 
        print(str(len(board)-i) + " ", end='')    
        for j in range(len(board[i])) : 
            print(board[i][j], end=" ")
        print()    

def clear_board(cmd):
    global board_size, white_captured_stones, black_captured_stones, total_moves
    white_captured_stones = 0
    black_captured_stones = 0
    total_moves = 0

    boardsize("boardsize " + str(board_size))

def komi(cmd):
    try:
        global komi
        komi = float(cmd.split(' ')[1])
    except:
        print("failed to set komi to " + cmd)

def play(cmd):
    global board, total_moves
    color = cmd.split(' ')[1][0]
    move = cmd.split(' ')[2]
    col = ALPHA.find(move[0])
    row = board_size - int(move[1:])
    
    print("move " + str(total_moves))
    if total_moves >= board_size * board_size:
        print("board is full")
        return True

    if row >= 0 and row < board_size and col >= 0 and col < board_size:
        if color == 'B' or color == 'W':
            if board[row][col] == '.':
                board[row][col] = color
                total_moves += 1
                return True
    print("illegal move")
    return False

def genmove(cmd):
    color = cmd.split(' ')[1][0]
    print("generating move for " + color)

    while True:
        row = random.randint(1, board_size)
        col = random.randint(0, board_size-1)

        move = str(ALPHA[col]) + str(row)
        if play("play " + color + " " + move):
            break
    print (move)
    

cmd_dict =  {
            "protocol_version": protocol_version,
            "name": name,
            "version": version,
            "known_command": known_command,
            "list_commands": list_commands,
            "quit": quit,
            "boardsize": boardsize,
            "showboard": showboard,
            "clear_board": clear_board,
            "komi": komi,
            "play": play,
            "genmove": genmove
            }

# Loop over commands
for cmd in sys.stdin:
    clean_cmd = cmd.split(' ')[0].strip()
    if clean_cmd in cmd_dict:
        cmd_dict[clean_cmd](cmd)
    else:
        print("\n'" + cmd.replace("\n",'') + "' IS NOT SUPPORTED. Try one of these: ")
        list_commands(cmd)