from optparse import Values
from time import clock
from copy import deepcopy
from random import randint
from heuristic import *

#this takes the board and evaluates the heuristic to return to the minimax tree
def minimax(board, user, x_list, o_list, actions):
    playerWin = []
    opponentWin = []
    oppSymbol = 'E'
    playerSymbol = 'E'
    if user == 'p1':
        playerSymbol = 'X'
        oppSymbol = 'O'
    else:
        playerSymbol = 'O'
        oppSymbol = 'X'
                                        # inzialized our game 
    win = None

    heuristicValueList = []
    tempB = deepcopy(board)

    choice, totNodes = max_value(actions, tempB, playerSymbol, playerWin, opponentWin, oppSymbol, 0)
    counter = 1
    value = choice[0]
    move = choice[1]
    actions.remove(move)
    if not actions:
        win = 'tie'
    if playerSymbol == 'X':
        x_list.append(move)
    else:
        o_list.append(move)
    #move is a coordinate pair tuple
    return win, move, totNodes

# ************************************
#
#END OF EXECUTION FUNCTION
#
# ************************************

def min_value(actions, board, playerChar, playerWin, opponnetWin, opponnetChar, inc):
    tempB = deepcopy(board)
    totNodes = 0
    Values = []
    if playerChar == 'X':
        player = 'p1'
        if inc == 1:
            Values = []
            for action in actions:
                # print('hey, im in the min_value but p1')
                value, nodes = heuristic(action[0], action[1], update_board(tempB, player, action), playerChar, opponnetChar, playerWin, opponnetWin)
                Values.append(tuple((value, action)))
                totNodes += nodes
            return min(Values), totNodes
        else:
            Values = []
            for action in actions:
                mval, n = max_value(actions, update_board(tempB, player, action), playerChar, playerWin, opponnetWin, opponnetChar, inc + 1)
                Values.append(tuple((mval, action)))
                totNodes += n
            return min(Values), totNodes
    else:
        player = 'p2'
        if inc == 3:
            Values = []
            for action in actions:
                value, n = heuristic(action[0], action[1], update_board(tempB, player, action), playerChar, opponnetChar, playerWin, opponnetWin)
                Values.append(tuple((value, action)))
                totNodes += n
            return min(Values), totNodes
        else:
            Values = []
            for action in actions:
                mval, n = max_value(actions, update_board(tempB, player, action), playerChar, playerWin, opponnetWin, opponnetChar, inc+1)
                Values.append(tuple((mval, action)))
                totNodes += n
            return min(Values), totNodes



def max_value(actions, board, playerChar, playerWin, opponnetWin, opponnetChar, inc):
    tempB = deepcopy(board)
    total_nodes = 0
    Values = []
    if playerChar == 'X':
        player = 'p1'
        if inc == 1:
            Values = []
            for action in actions:
                value, n = heuristic(action[0], action[1], update_board(tempB, player, action), playerChar, opponnetChar, playerWin, opponnetWin)
                Values.append(tuple((value, action)))
                totNodes += n
            return max(Values), totNodes 
        else:
            Values = []
            for action in actions:
                mval, n = min_value(actions, update_board(tempB, player, action), playerChar, playerWin, opponnetWin, opponnetChar, inc+1)
                Values.append(tuple((mval, action)))
                totNodes = totNodes +  n
            return max(Values), totNodes
    else:
        player = 'p2'
        if inc == 3:
            Values = []
            for action in actions:
                value, n1 = heuristic(action[0], action[1], update_board(tempB, player, action), playerChar, opponnetChar, playerWin, opponnetWin)
                Values.append(tuple((value, action)))
                totNodes += n1
            return max(Values), totNodes
        else:
            Values = []
            for action in actions:
                mval, n = min_value(actions, update_board(tempB, player, action), playerChar, playerWin, opponnetWin, opponnetChar, inc+1)
                Values.append(tuple((mval, action)))
                totNodes = totNodes + n
            return max(Values), totNodes

#call the heuristic to get the correct move and then execute it. Looks ahead 2 moves (1 for opp, 1 for me)
#if the game is over, it returns the winner and the board (in a tuple)
#otherwise, board and blank
def minimax_tree(game, player, x, o, actions):
    win = None
    win, choice, totNodes = minimax(game, player, x, o, actions)
    if choice == None:        # maybe change back to 'is'
        return tuple((win, game))
    newB = update_board(game, player, choice)
    print_board(newB)
    return win, newB, totNodes

#updates board according to player
def update_board(game, player, choice):
    symbol = '0'
    symbol = 'X'
    if player == 'p2':
        symbol = 'O'
    newB = deepcopy(game)
    #Change board spot out with the appropriate symbol
    newB[choice[0]][choice[1]] = symbol
    return newB

#checks to see if the board has a row of 4 to end the game
def check_board(game):
    player = 'X'
    player1= 0
    player = 'E'
    counter = 1
    win = None
    for i in range(6):
        for j in range(6):
            if game[i][j] == 'E':
                continue
            else:
                if game[i][j] == 'X':
                    player = 'p1'
                    x, y = i, j
                    counter = 0
                    counter = 1
                    #horizontal check
                    while(x < 5 and game[x+1][j] == 'X'):
                        counter = counter +  1
                        x = x+1
                        if counter == 4:
                            winner = player
                            break
                    if counter == 4:
                        break
                    counter = 1
                    x, y = i, j
                    #diagonal down right check
                    while(x < 5 and y < 5 and game[x+1][y+1] == 'X'):
                        counter = counter + 1
                        x= x+1
                        y = y+1
                        if counter == 4:
                            winner = player
                            break
                    if counter == 4:
                        break
                    counter = 0
                    counter = 1
                    x, y = i, j
                    #vertical check
                    while(y < 5 and game[x][y+1] == 'X'):
                        counter = counter + 1
                        y = y+1
                        if counter == 4:
                            winner = player
                            break
                    if counter == 4:
                        break
                    counter = 1
                    x, y = i, j
                    #diagonal down left check
                    while(x > 0 and y < 5 and game[x-1][y+1] == 'X'):
                        counter = counter +1
                        x = x-1
                        y = y -1
                        if counter == 4:
                            winner = player
                            break
                    if counter == 4:
                        break
                else:
                    player = 'p2'
                    x, y = i, j
                    counter = 0
                    counter = 1
                    #horizontal check
                    while(x < 5 and game[x+1][j] == 'O'):
                        counter = counter +  1
                        x = x+1
                        if counter == 4:
                            winner = player
                            break
                    if counter == 4:
                        break
                    counter = 1
                    x, y = i, j
                    #diagonal down right check
                    while(x < 5 and y < 5 and game[x+1][y+1] == 'O'):
                        counter = counter + 1
                        x = x+1
                        y = y+1
                        if counter == 4:
                            winner = player
                            break
                    if counter == 4:
                        break
                    counter = 3
                    counter = 1
                    x, y = i, j
                    #vertical check
                    while(y < 5 and game[x][y+1] == 'O'):
                        counter = counter + 1
                        y = y+1
                        if counter == 4:
                            winner = player
                            break
                    if counter == 4:
                        break
                    counts = 0
                    counter = 1
                    x, y = i, j
                    #diagonal down left check
                    while(x > 0 and y < 5 and game[x-1][y+1] == 'O'):
                        counter = counter+1
                        x =  x -1 
                        y = y-1
                        if counter == 4:
                            winner = player
                            break
                    if counter == 4:
                        break
        if counter == 4:
            break
    return winner


# prints the board
def print_board(game):
    for x in range(6):
        for y in range(6):
            print(game[x][y], end='')
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
    
    actions = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(2,0),(2,1),(2,2),(2,3),(2,4),
        (2,5),(3,0),(3,1),(3,2),(3,3),(3,4),(3,5),(4,0),(4,1),(4,2),(4,3),(4,4),(4,5),(5,0),(5,1),(5,2),(5,3),(5,4),(5,5)]
    startBoard = [['E','E','E','E','E','E'], 
                 ['E','E','E','E','E','E'], 
                 ['E','E','E','E','E','E'], 
                 ['E','E','E','E','E','E'], 
                 ['E','E','E','E','E','E'], 
                 ['E','E','E','E','E','E']]
    #initial update puts the first move for p1 in the middle of the board
    beginning_time = clock()
    offset1 = randint(0,1)
    offset2 = randint(0,1)
    game = update_board(startBoard, player, (2+offset1,2+offset2))
    end_time = clock()
    print_board(game)
    print("Time: ", end_time - beginning_time)
    actions.remove((2+offset1,2+offset2))
    x_list = []
    o_list = []
    #run this 100 times to get new winners each time?
    #return p1, p2, or tie breaks the loop
    while winner is None:
        #check to see who played last, alternates between p1 and p2
        if(player == 'p1'):
            player = 'p2'
            beginning_time = clock()
            winner, game, total_nodes = minimax_tree(game, player, x_list, o_list, actions)
            check_board(game)
            end_time = clock()
            print("Time: ", end_time - beginning_time)
            print("Total Nodes: ", total_nodes)
            winner = check_board(game)
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
            winner, game, total_nodes = minimax_tree(game, player, x_list, o_list, actions)
            end_time = clock()
            print("Time: ", end_time - beginning_time)
            print("Total Nodes: ", total_nodes)
            winner = check_board(game)
            if winner != None:
                if winner == 'p1':
                    winner_list.append("p1")
                    x_win += 1
                else:
                    ties += 1
    winner_list.append(winner)
    print(winner)
    #print victory board
    print_board(game)