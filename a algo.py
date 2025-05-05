def print_board(board):
    for row in range(0, 9, 3):
        row_visual = ""
        for tile in board[row:row + 3]:
            if tile == 0:
                row_visual += "   "
            else:
                row_visual += f"{tile:>2} "
        print(row_visual.strip())

def heuristic(board, goal_state):
    distance = 0
    for i in range(9):
        if board[i] != 0:
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal_state.index(board[i]), 3)
            distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

def move_tile(board, move, blank_pos):
    new_board = board[:]
    new_blank_pos = blank_pos + move
    new_board[blank_pos], new_board[new_blank_pos] = new_board[new_blank_pos], new_board[blank_pos]
    return new_board

def a_star(start_state, goal_state):
    open_list = [(start_state, 0, heuristic(start_state, goal_state))]
    closed_list = set()

    while open_list:
        current_state, depth, _ = open_list.pop(0)
        print(f"Step {depth + 1}:")  
        print_board(current_state)  
        print() 
        
        if current_state == goal_state:
            return current_state, depth
        
        closed_list.add(tuple(current_state))
        blank_pos = current_state.index(0)
        moves = [(-3, 'U'), (3, 'D'), (-1, 'L'), (1, 'R')]  
        
        for move, _ in moves:
            if move == -3 and blank_pos < 3: continue 
            if move == 3 and blank_pos > 5: continue   
            if move == -1 and blank_pos % 3 == 0: continue  
            if move == 1 and blank_pos % 3 == 2: continue  
            
            new_board = move_tile(current_state, move, blank_pos)
            if tuple(new_board) in closed_list:
                continue
            
            open_list.append((new_board, depth + 1, depth + 1 + heuristic(new_board, goal_state)))
        
        open_list.sort(key=lambda x: x[2])  
    
    return None, None


def print_solution(solution):
    print("Solution path:")
    print_board(solution)


initial_state = list(map(int, input("Enter initial state (9 numbers separated by space): ").split()))
goal_state = list(map(int, input("Enter goal state (9 numbers separated by space): ").split()))

solution, steps = a_star(initial_state, goal_state)


if solution:
    print(f"Solution found in {steps} steps:")
    print_solution(solution)
else:
    print("No solution exists.")