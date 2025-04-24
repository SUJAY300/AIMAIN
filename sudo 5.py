import random

SIZE, SUB = 9, 3

def print_board(b):
    for r in b:
        print(*r)

def is_valid(b, r, c, n):
    block_r, block_c = r // SUB * SUB, c // SUB * SUB
    return all(n != b[r][i] and n != b[i][c] for i in range(SIZE)) and \
           all(n != b[i][j] for i in range(block_r, block_r + SUB) for j in range(block_c, block_c + SUB))

def find_cell(b):
    best = (None, None, list(range(1, SIZE+1)))
    for r in range(SIZE):
        for c in range(SIZE):
            if b[r][c] == 0:
                opts = [n for n in range(1, SIZE+1) if is_valid(b, r, c, n)]
                if len(opts) < len(best[2]):
                    best = (r, c, opts)
    return best if best[0] is not None else None

def solve(b):
    cell = find_cell(b)
    if not cell: return True
    r, c, opts = cell
    for n in opts:
        b[r][c] = n
        if solve(b): return True
        b[r][c] = 0
    return False

def generate_board():
    b = [[0]*SIZE for _ in range(SIZE)]
    for i in range(0, SIZE, SUB):
        nums = random.sample(range(1, SIZE+1), SIZE)
        for r in range(SUB):
            for c in range(SUB):
                b[i+r][i+c] = nums[r*SUB + c]
    solve(b)
    for _ in range(random.randint(30, 40)):
        b[random.randint(0, SIZE-1)][random.randint(0, SIZE-1)] = 0
    return b

if __name__ == "__main__":
    print("Generated Sudoku Board:")
    board = generate_board()
    print_board(board)
    if solve(board):
        print("\nSolved Sudoku Board:")
        print_board(board)
    else:
        print("\nNo solution exists!")
