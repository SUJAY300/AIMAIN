moves = ['rock', 'paper', 'scissors']
win = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

def utility(ai, user):
    return 1 if win[ai] == user else -1 if win[user] == ai else 0

def minimax(user_move):
    best_score, best_move = -2, None
    for move in moves:
        score = utility(move, user_move)
        if score > best_score:
            best_score, best_move = score, move
    return best_move

user = input("Enter your move (rock/paper/scissors): ").lower()
if user not in moves:
    print("Invalid input!")
else:
    ai = minimax(user)
    print(f"AI chose: {ai}")
    if ai == user: print("Result: Draw")
    elif win[ai] == user: print("Result: AI Wins!")
    else: print("Result: You Win!")
