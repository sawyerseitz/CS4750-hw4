from time import clock
from copy import deepcopy
from random import randint
from heuristic import *

#this takes the board and evaluates the heuristic to return to the minimax tree
def minimax_exec(board, player, x_list, o_list, action_list):
    player_win = []
    opp_win = []
    opponent_symbol = 'E'
    player_symbol = 'E'
    if player == 'p1':
        player_symbol = 'X'
        opponent_symbol = 'O'
    else:
        player_symbol = 'O'
        opponent_symbol = 'X'
    #initialize return vars
    winner = None

    h_value_list = []
    temp_board = deepcopy(board)
    # print_board(board)
    # print_board(temp_board)
    #returns the max of the min value and the correct move
    choice, total_nodes = max_value(action_list, temp_board, player_symbol, player_win, opp_win, opponent_symbol, 0)
    # if player_win:
    #     winner = player
    val = choice[0]
    move = choice[1]
    # print_board(board)

    # print(choice)
    action_list.remove(move)
    if not action_list:
        winner = 'tie'
    if player_symbol == 'X':
        x_list.append(move)
    else:
        o_list.append(move)
    #move is a coordinate pair tuple
    return winner, move, total_nodes

# ************************************
#
#END OF EXECUTION FUNCTION
#
# ************************************

def min_value(action_list, board, player_char, player_win, opp_win, opp_char, increment):
    temp_board = deepcopy(board)
    total_nodes = 0
    value_list = []
    if player_char == 'X':
        player = 'p1'
        if increment == 1:
            value_list = []
            for action in action_list:
                # print('hey, im in the min_value but p1')
                value, nodes = heuristic(action[0], action[1], update_board(temp_board, player, action), player_char, opp_char, player_win, opp_win)
                value_list.append(tuple((value, action)))
                total_nodes += nodes
            return min(value_list), total_nodes
        else:
            value_list = []
            for action in action_list:
                mval, n = max_value(action_list, update_board(temp_board, player, action), player_char, player_win, opp_win, opp_char, increment+1)
                value_list.append(tuple((mval, action)))
                total_nodes += n
            return min(value_list), total_nodes
    else:
        player = 'p2'
        if increment == 3:
            value_list = []
            for action in action_list:
                value, nodes = heuristic(action[0], action[1], update_board(temp_board, player, action), player_char, opp_char, player_win, opp_win)
                value_list.append(tuple((value, action)))
                total_nodes += nodes
            return min(value_list), total_nodes
        else:
            value_list = []
            for action in action_list:
                mval, n = max_value(action_list, update_board(temp_board, player, action), player_char, player_win, opp_win, opp_char, increment+1)
                value_list.append(tuple((mval, action)))
                total_nodes += n
            return min(value_list), total_nodes



def max_value(action_list, board, player_char, player_win, opp_win, opp_char, increment):
    temp_board = deepcopy(board)
    total_nodes = 0
    value_list = []
    if player_char == 'X':
        player = 'p1'
        if increment == 1:
            value_list = []
            for action in action_list:
                value, nodes = heuristic(action[0], action[1], update_board(temp_board, player, action), player_char, opp_char, player_win, opp_win)
                value_list.append(tuple((value, action)))
                total_nodes += nodes
            return max(value_list), total_nodes
        else:
            value_list = []
            for action in action_list:
                mval, n = min_value(action_list, update_board(temp_board, player, action), player_char, player_win, opp_win, opp_char, increment+1)
                value_list.append(tuple((mval, action)))
                total_nodes += n
            return max(value_list), total_nodes
    else:
        player = 'p2'
        if increment == 3:
            value_list = []
            for action in action_list:
                value, nodes = heuristic(action[0], action[1], update_board(temp_board, player, action), player_char, opp_char, player_win, opp_win)
                value_list.append(tuple((value, action)))
                total_nodes += nodes
            return max(value_list), total_nodes
        else:
            value_list = []
            for action in action_list:
                mval, n = min_value(action_list, update_board(temp_board, player, action), player_char, player_win, opp_win, opp_char, increment+1)
                value_list.append(tuple((mval, action)))
                total_nodes += n
            return max(value_list), total_nodes

#call the heuristic to get the correct move and then execute it. Looks ahead 2 moves (1 for opp, 1 for me)
#if the game is over, it returns the winner and the board (in a tuple)
#otherwise, board and blank
def minimax_tree(board, player, x_list, o_list, action_list):
    winner = None
    winner, choice, total_nodes = minimax_exec(board, player, x_list, o_list, action_list)
    if choice is None:
        return tuple((winner, board))
    new_board = update_board(board, player, choice)
    print_board(new_board)
    return winner, new_board, total_nodes

#updates board according to player
def update_board(board, player, choice):
    symbol = 'X'
    if player == 'p2':
        symbol = 'O'
    new_board = deepcopy(board)
    #Change board spot out with the appropriate symbol
    new_board[choice[0]][choice[1]] = symbol
    return new_board

#checks to see if the board has a row of 4 to end the game
def check_board(board):
    player = 'E'
    counter = 1
    winner = None
    for x in range(6):
        for y in range(6):
            if board[x][y] == 'E':
                continue
            else:
                if board[x][y] == 'X':
                    player = 'p1'
                    i, j = x, y
                    counter = 1
                    #horizontal check
                    while(i < 5 and board[i+1][y] == 'X'):
                        counter += 1
                        i+=1
                        if counter == 4:
                            winner = player
                            break
                    if counter == 4:
                        break
                    counter = 1
                    i, j = x, y
                    #diagonal down right check
                    while(i < 5 and j < 5 and board[i+1][j+1] == 'X'):
                        counter += 1
                        i+=1
                        j+=1
                        if counter == 4:
                            winner = player
                            break
                    if counter == 4:
                        break
                    counter = 1
                    i, j = x, y
                    #vertical check
                    while(j < 5 and board[i][j+1] == 'X'):
                        counter += 1
                        j+=1
                        if counter == 4:
                            winner = player
                            break
                    if counter == 4:
                        break
                    counter = 1
                    i, j = x, y
                    #diagonal down left check
                    while(i > 0 and j < 5 and board[i-1][j+1] == 'X'):
                        counter += 1
                        i-=1
                        j+=1
                        if counter == 4:
                            winner = player
                            break
                    if counter == 4:
                        break
                else:
                    player = 'p2'
                    i, j = x, y
                    counter = 1
                    #horizontal check
                    while(i < 5 and board[i+1][y] == 'O'):
                        counter += 1
                        i+=1
                        if counter == 4:
                            winner = player
                            break
                    if counter == 4:
                        break
                    counter = 1
                    i, j = x, y
                    #diagonal down right check
                    while(i < 5 and j < 5 and board[i+1][j+1] == 'O'):
                        counter += 1
                        i+=1
                        j+=1
                        if counter == 4:
                            winner = player
                            break
                    if counter == 4:
                        break
                    counter = 1
                    i, j = x, y
                    #vertical check
                    while(j < 5 and board[i][j+1] == 'O'):
                        counter += 1
                        j+=1
                        if counter == 4:
                            winner = player
                            break
                    if counter == 4:
                        break
                    counter = 1
                    i, j = x, y
                    #diagonal down left check
                    while(i > 0 and j < 5 and board[i-1][j+1] == 'O'):
                        counter += 1
                        i-=1
                        j+=1
                        if counter == 4:
                            winner = player
                            break
                    if counter == 4:
                        break
        if counter == 4:
            break
    return winner


#pretty self-explanatory, prints the board
def print_board(board):
    for x in range(6):
        for y in range(6):
            print(board[x][y], end='')
            print(' ', end='')
        print('\n', end='')
    print('------------------')

#start of main
if __name__ == "__main__":
    #winner_list will hold the results of all the games
    winner_list = []
    x_win = 0
    o_win = 0
    ties = 0
    player = 'p2'
    winner = None
    '''
        E - Empty
        X - p1
        O - p2
    '''
    #empty board
    new_board = [['E','E','E','E','E','E'], 
                 ['E','E','E','E','E','E'], 
                 ['E','E','E','E','E','E'], 
                 ['E','E','E','E','E','E'], 
                 ['E','E','E','E','E','E'], 
                 ['E','E','E','E','E','E']]
    #initial update puts the first move for p1 in the middle of the board
    beginning_time = clock()
    offset1 = randint(0,1)
    offset2 = randint(0,1)
    board = update_board(new_board, player, (2+offset1,2+offset2))
    end_time = clock()
    print_board(board)
    print("Time: ", end_time - beginning_time)
    action_list = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(2,0),(2,1),(2,2),(2,3),(2,4),
        (2,5),(3,0),(3,1),(3,2),(3,3),(3,4),(3,5),(4,0),(4,1),(4,2),(4,3),(4,4),(4,5),(5,0),(5,1),(5,2),(5,3),(5,4),(5,5)]
    action_list.remove((2+offset1,2+offset2))
    x_list = []
    o_list = []
    #run this 100 times to get new winners each time?
    #return p1, p2, or tie breaks the loop
    while winner is None:
        #check to see who played last, alternates between p1 and p2
        if(player == 'p1'):
            player = 'p2'
            beginning_time = clock()
            winner, board, total_nodes = minimax_tree(board, player, x_list, o_list, action_list)
            check_board(board)
            end_time = clock()
            print("Time: ", end_time - beginning_time)
            print("Total Nodes: ", total_nodes)
            winner = check_board(board)
            if winner != None:
                if winner == 'p2':
                    winner_list.append("p2")
                    o_win += 1
                else:
                    ties += 1
                break
        else:
            player = 'p1'
            beginning_time = clock()
            winner, board, total_nodes = minimax_tree(board, player, x_list, o_list, action_list)
            end_time = clock()
            print("Time: ", end_time - beginning_time)
            print("Total Nodes: ", total_nodes)
            winner = check_board(board)
            if winner != None:
                if winner == 'p1':
                    winner_list.append("p1")
                    x_win += 1
                else:
                    ties += 1
    winner_list.append(winner)
    print(winner)
    #print victory board
    print_board(board)