
def print_board(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---|---|---") 
    print(" " + board[3]+ " | " + board[4] + " | " + board[5])
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
  
    
def check_win(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]             
    ]
    for combo in winning_combinations:
        if board[combo[0]] == player and board[combo[1]] == player and board[combo[2]] == player:
            return True
    return False

def check_draw(board):
    return board.count(" ") == 0


def minimax(board, depth, maximizing):
    if check_win(board, "X"):
        return -1   
    elif check_win(board, "O"):
        return 1  
    elif check_draw(board):
        return 0  

    if maximizing:
        best_score = -1000
        for i in range(len(board)):
            if board[i] == " ":
                board[i] = "O"
              
                score = minimax(board, depth+1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for i in range(len(board)):
            if board[i] == " ":
                board[i] = "X"
                
                score = minimax(board, depth+1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score



def main():
    board= [" "," "," "," "," "," "," "," "," "]

    current_player = "X"  

    while True:
        if current_player == "X":
            print_board(board)
            move = int(input("Enter a move (1-9): "))
            while board[move-1] != " ":
                print("You cannot fool them, play correctly this time")
                move = int(input("Enter a move (1-9): "))
            board[move-1] = "X"
            current_player = "O"

        else:
            best_move = 0
            best_score = -1000
            for i in range(len(board)):
                if board[i] == " ":
                    board[i] = "O"
                    score = minimax(board, 0, False)
                    board[i] = " "
                    if score > best_score:
                        best_score = score
                        best_move = i
            board[best_move] = "O"
            current_player = "X"

        if check_win(board, "X"):
            print_board(board)
            print("You saved humanity from AI!!!")
            break
        if check_win(board, "O"):
            print_board(board)
            print("Ai terminated you")
            break
        if check_draw(board):
            print_board(board)
            print("we have reached coexistence")
            break


if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    