BOARD_DIM = 6
EMPTY_CHAR = 'E'

"""
CASE NUMBERS
0: No moves
1: two-side-open-3-in-a-row
2: one-side-3-in-a-row
3: open-2-in-a-row
"""


# Checks spaces that are above and below the given space
# Returns the appropriate case number and sorted coordinates of the case
def check_vertical(x, y, board, player_char, opp_char):

	coordinate_list = [(x,y)]

	vertical_char_count = 1
	empty_space_count = 0

	j = y
	counter = 0
	# Checking Upward
	while(j != 0):
		counter += 1
		current_char = board[x][j-1]

		if current_char == player_char:
			vertical_char_count += 1
			j-=1
			coordinate_list.append((x,j))
			continue

		elif current_char == opp_char:
			break

		elif current_char == EMPTY_CHAR:
			empty_space_count += 1
			break

	# Checking Downward
	j = y
	while(j != BOARD_DIM-1):
		counter += 1
		current_char = board[x][j+1]

		if current_char == player_char:
			vertical_char_count += 1
			coordinate_list.append((x,j))
			j+=1
			continue

		elif current_char == opp_char:
			break

		elif current_char == EMPTY_CHAR:
			empty_space_count += 1
			break

	# Returning the appropriate case numbers and coordinate_list

	# Sort the list by the x coordinate
	coordinate_list = sorted(coordinate_list, key=lambda coord: coord[0])
	# print(vertical_char_count)
	# print(empty_space_count)
	if vertical_char_count >= 4:
		return 4, coordinate_list, counter
	elif vertical_char_count <= 1 or empty_space_count == 0:
		# print(1)
		coordinate_list = []
		# print('return')
		return 0, coordinate_list, counter

	elif vertical_char_count == 2:
		# print('return')
		return 3, coordinate_list, counter

	elif vertical_char_count == 3:
		if empty_space_count == 1:
			# print('return')
			return 2, coordinate_list, counter
		elif empty_space_count == 2:
			# print('return')
			return 1, coordinate_list, counter

def check_horizontal(x, y, board, player_char, opp_char):

	coordinate_list = [(x,y)]

	horizontal_char_count = 1
	empty_space_count = 0

	# Checking Left
	i = x
	counter = 0
	while(i != 0):
		counter += 1
		current_char = board[i-1][y]

		if current_char == player_char:
			horizontal_char_count += 1
			coordinate_list.append((i,y))
			i -= 1
			continue

		elif current_char == opp_char:
			break

		elif current_char == EMPTY_CHAR:
			empty_space_count += 1
			break

	# Checking Right
	i = x
	while(i != BOARD_DIM-1):
		counter += 1
		current_char = board[i+1][y]

		if current_char == player_char:
			horizontal_char_count += 1
			coordinate_list.append((i,y))
			i += 1
			continue

		elif current_char == opp_char:
			break

		elif current_char == EMPTY_CHAR:
			empty_space_count += 1
			break

	# Returning the appropriate case numbers and coordinate_list
	coordinate_list = sorted(coordinate_list, key=lambda coord: coord[0])

	if horizontal_char_count >= 4:
		return 4, coordinate_list, counter
	elif horizontal_char_count <= 1 or empty_space_count == 0:
		coordinate_list = []
		return 0, coordinate_list, counter

	elif horizontal_char_count == 2:
		return 3, coordinate_list, counter

	elif horizontal_char_count == 3:
		if empty_space_count == 1:
			return 2, coordinate_list, counter
		elif empty_space_count == 2:
			return 1, coordinate_list, counter

def check_diagonal_down(x, y, board, player_char, opp_char):

	coordinate_list = [(x,y)]

	diagonal_char_count = 1
	empty_space_count = 0

	counter = 0
	# Checking Left and Up
	i, j = x, y
	while(i != 0 and j != 0):
		counter += 1
		current_char = board[i-1][j-1]

		if current_char == player_char:
			diagonal_char_count += 1
			coordinate_list.append((i,j))
			i-=1
			j-=1
			continue

		elif current_char == opp_char:
			break

		elif current_char == EMPTY_CHAR:
			empty_space_count += 1
			break

	# Checking Right and Down
	i, j = x, y
	while(i != BOARD_DIM-1 and j != BOARD_DIM-1):
		counter += 1
		current_char = board[i+1][j+1]

		if current_char == player_char:
			diagonal_char_count += 1
			coordinate_list.append((i,j))
			i+=1
			j+=1
			continue

		elif current_char == opp_char:
			break

		elif current_char == EMPTY_CHAR:
			empty_space_count += 1
			break


	# Returning the appropriate case numbers and coordinate_list
	coordinate_list = sorted(coordinate_list, key=lambda coord: coord[0])

	if diagonal_char_count >= 4:
		return 4, coordinate_list, counter
	elif diagonal_char_count <= 1 or empty_space_count == 0:
		coordinate_list = []
		return 0, coordinate_list, counter

	elif diagonal_char_count == 2:
		return 3, coordinate_list, counter

	elif diagonal_char_count == 3:
		if empty_space_count == 1:
			return 2, coordinate_list, counter
		elif empty_space_count == 2:
			return 1, coordinate_list, counter


def check_diagonal_up(x, y, board, player_char, opp_char):

	coordinate_list = [(x,y)]
	diagonal_char_count = 1
	empty_space_count = 0

	# LEFT AND DOWN
	i, j = x, y
	counter = 0
	while(j != BOARD_DIM-1 and i != 0):
		counter += 1
		current_char = board[i-1][j+1]

		if current_char == player_char:
			diagonal_char_count += 1
			coordinate_list.append((i,j))
			i-=1
			j+=1
			continue

		elif current_char == opp_char:
			break

		elif current_char == EMPTY_CHAR:
			empty_space_count += 1
			break

	# Checking Right and Up
	i, j = x,y

	while(j != 0 and i != BOARD_DIM-1):
		counter += 1
		current_char = board[i+1][j-1]

		if current_char == player_char:
			diagonal_char_count += 1
			coordinate_list.append((i,j))
			i+=1
			j-=1
			continue

		elif current_char == opp_char:
			break

		elif current_char == EMPTY_CHAR:
			empty_space_count += 1
			break

	# Returning the appropriate case numbers and coordinate_list
	coordinate_list = sorted(coordinate_list, key=lambda coord: coord[0])

	if diagonal_char_count >= 4:
		return 4, coordinate_list, counter
	elif diagonal_char_count <= 1 or empty_space_count == 0:
		coordinate_list = []
		return 0, coordinate_list, counter

	elif diagonal_char_count == 2:
		return 3, coordinate_list, counter

	elif diagonal_char_count == 3:
		if empty_space_count == 1:
			return 2, coordinate_list, counter
		elif empty_space_count == 2:
			return 1, coordinate_list, counter

def populate_lists(x,y, board, player_char, opp_char, three_two_open, three_one_open, two_open, win, check_function):
	nodes = 0
	case, coordinates, num_nodes = check_function(x, y, board, player_char, opp_char)
	nodes += num_nodes
	if coordinates:
		if case == 1:
			if coordinates not in three_two_open:
				three_two_open.append(coordinates)

		elif case == 2:
			if coordinates not in three_one_open:
				three_one_open.append(coordinates)

		elif case == 3:
			if coordinates not in two_open:
				two_open.append(coordinates)
		elif case == 4:
			if coordinates not in win:
				win.append(coordinates)

	return nodes

def heuristic(x, y, board, player_char, opp_char, player_win, opponent_win):
	player_three_two_open = []
	player_three_one_open = []
	player_two_open = []

	opponent_three_two_open = []
	opponent_three_one_open = []
	opponent_two_open = []

	total_nodes = 0

	for i in range(BOARD_DIM):
		for j in range(BOARD_DIM):
			if board[i][j] == EMPTY_CHAR:
				continue

			elif board[i][j] == player_char:
				# Vertical Check
				total_nodes += populate_lists(i, j, board, player_char, opp_char, player_three_two_open, player_three_one_open, player_two_open, player_win, check_vertical)
				# Horizontal Check
				total_nodes += populate_lists(i, j, board, player_char, opp_char, player_three_two_open, player_three_one_open, player_two_open, player_win, check_horizontal)
				# Check Diagonal
				total_nodes += populate_lists(i, j, board, player_char, opp_char, player_three_two_open, player_three_one_open, player_two_open, player_win, check_diagonal_up)
				total_nodes += populate_lists(i, j, board, player_char, opp_char, player_three_two_open, player_three_one_open, player_two_open, player_win, check_diagonal_down)

			elif board[i][j] == opp_char:
				# Vertical Check
				total_nodes += populate_lists(i, j, board, opp_char, player_char, opponent_three_two_open, opponent_three_one_open, opponent_two_open, opponent_win, check_vertical)
				# Horizontal Check
				total_nodes += populate_lists(i, j, board, opp_char, player_char, opponent_three_two_open, opponent_three_one_open, opponent_two_open, opponent_win, check_horizontal)
				# Check Diagonal
				total_nodes += populate_lists(i, j, board, opp_char, player_char, opponent_three_two_open, opponent_three_one_open, opponent_two_open, opponent_win, check_diagonal_up)
				total_nodes += populate_lists(i, j, board, opp_char, player_char, opponent_three_two_open, opponent_three_one_open, opponent_two_open, opponent_win, check_diagonal_down)


	#if there is a successful win condition on the board make it a large value
	# if player_win:
	# 	return 1000000000, total_nodes

	# #if there is a bad win condition on the board make it a low value
	# if opponent_win:
	# 	return -1000000000, total_nodes

	p_tto = len(player_three_two_open)
	p_too = len(player_three_one_open)
	p_to = len(player_two_open)

	o_tto = len(opponent_three_two_open)
	o_too = len(opponent_three_one_open)
	o_to = len(opponent_two_open)

	heuristic = (5 * p_tto) - (10 * o_tto) + (3 * p_too) - (6 * o_too) + p_to - o_to

	return heuristic, total_nodes