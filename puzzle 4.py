import heapq

class PuzzleState:
    def __init__(self, board, moves=0, prev=None):
        self.board = board
        self.moves = moves
        self.prev = prev
        self.priority = moves + self.heuristic()

    def __lt__(self, other):
        return self.priority < other.priority

    def heuristic(self):
        goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        return sum(abs((b % 3) - (g % 3)) + abs((b // 3) - (g // 3)) for b, g in [(i, goal.index(self.board[i])) for i in range(9) if self.board[i] != 0])

    def neighbors(self):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        zero_pos = self.board.index(0)
        x, y = divmod(zero_pos, 3)
        neighbors = []

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_board = self.board[:]
                new_board[zero_pos], new_board[nx * 3 + ny] = new_board[nx * 3 + ny], new_board[zero_pos]
                neighbors.append(PuzzleState(new_board, self.moves + 1, self))
        return neighbors

    def is_goal(self):
        return self.board == list(range(1, 9)) + [0]

    def path(self):
        state, steps = self, []
        while state:
            steps.append(state.board)
            state = state.prev
        return steps[::-1]

def a_star(start_board):
    start = PuzzleState(start_board)
    frontier = [start]
    heapq.heapify(frontier)
    explored = set()

    while frontier:
        current = heapq.heappop(frontier)
        if current.is_goal():
            return current.path()

        explored.add(tuple(current.board))
        for neighbor in current.neighbors():
            if tuple(neighbor.board) not in explored:
                heapq.heappush(frontier, neighbor)

    return None

start_state = [1, 2, 8, 3, 0, 5, 6, 7, 4]
solution = a_star(start_state)

if solution:
    for step in solution:
        print(f'{step[:3]}\n{step[3:6]}\n{step[6:]}\n')
else:
    print("No solution found.")
