import common

lines = common.get_lines(__file__)

def get_numbers():
    return [int(_) for _ in lines[0].split(',')]

def get_boards():
    boards = []
    for i in range(1, len(lines)):
        if lines[i] == '':
            boards.append([])
        else:
            boards[-1].append([ int(_) for _ in lines[i].split()])
    return boards
      
def sum_unmarked(board):
    result = 0
    for row in board:
        result += sum([row[_] for _ in range(N) if row[_] >= 0])
    return result

def has_won_on_num(board, num):
    def get_coordinate():
        for x in range(N):
            for y in range(N):
                if board[x][y] == num:
                    return (x, y)
        return (-1, -1)

    x, y = get_coordinate()
    if x < 0: return False
    
    board[x][y] = -1  # mark as -1
    # search corresponding col and row
    row = sum([board[x][_] for _ in range(N)]) == N * (-1)
    col = sum([board[_][y] for _ in range(N)]) == N * (-1)
    return row | col 


numbers = get_numbers()
boards = get_boards()
N = len(boards[0])

def part_one():
    for num in numbers:
        for board in boards:
            if has_won_on_num(board, num):
                return sum_unmarked(board) * num

def part_two():
    boards_wins = [False] * len(boards)
    for num in numbers:
        for i, board in enumerate(boards):
            if boards_wins[i]: continue
            if has_won_on_num(board, num):
                boards_wins[i] = True
                if all(boards_wins):
                    return sum_unmarked(board) * num

print(part_two())





