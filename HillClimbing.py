import random

def create_board():
    return [random.randint(0, 3) for _ in range(4)]

def calculate_conflicts(board):
    conflicts = 0
    for i in range(4):
        for j in range(i + 1, 4):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                conflicts += 1
    return conflicts

def hill_climbing():
    board = create_board()
    while True:
        current_conflicts = calculate_conflicts(board)
        if current_conflicts == 0:
            return board
        next_board = None
        next_conflicts = float('inf')
        for i in range(4):
            temp_board = board[:]
            for j in range(4):
                if temp_board[i] != j:
                    temp_board[i] = j
                    temp_conflicts = calculate_conflicts(temp_board)
                    if temp_conflicts < next_conflicts:
                        next_conflicts = temp_conflicts
                        next_board = temp_board[:]
        if next_conflicts >= current_conflicts:
            return board
        board = next_board

solution = hill_climbing()
print("Solution:", solution)
