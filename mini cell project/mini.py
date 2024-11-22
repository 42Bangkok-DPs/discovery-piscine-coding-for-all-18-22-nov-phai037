def check_direction(r, c, dr, dc, board):
    while 0 <= r < len(board) and 0 <= c < len(board[0]):
        piece = board[r][c]
        if piece != '.':
            if piece == 'K': return True
            if piece in ('P', 'N', 'R', 'B', 'Q'):
                return True
            break
        r, c = r + dr, c + dc
    return False

def find_king(board):
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 'K':
                return r, c
    return -1, -1

def is_king_in_check(board):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    king_row, king_col = find_king(board)
    
    if king_row == -1: return False
    
    for dr, dc in directions:
        if check_direction(king_row + dr, king_col + dc, dr, dc, board):
            return True
    return False


board = [list(x) for x in """........
........
........
...K....
........
........
...N....
..Q.....
""".splitlines()]

print("success" if is_king_in_check(board) else "fail")
