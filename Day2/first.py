def get_split_moves_list_from_input_file(input_file_name):
    with open(input_file_name) as input_file:
        input_string = input_file.read()
        moves_list = input_string.split('\n')
        split_moves_list = [individual_move.split(' ') for individual_move in moves_list]
        return split_moves_list

def calculate_score_for_move(move):
    score_dict = {
        'X': 1,
        'Y': 2,
        'Z': 3,
    }

    opponent_move = move[0]
    your_move = move[1]

    initial_score = score_dict[your_move]
    winner = get_winner_of_game(opponent_move, your_move)
    if winner == 'draw':
        final_score = initial_score + 3
    elif winner == 'opponent':
        final_score = initial_score
    else:
        final_score = initial_score + 6

    return final_score

def get_winner_of_game(opponent_move, your_move):
    same_letter_dict = {
        'X': 'A',
        'Y': 'B',
        'Z': 'C'
    }

    key_wins_over_value_dict = {
        'B': 'A',
        'C': 'B',
        'A': 'C',
    }

    your_modified_move = same_letter_dict[your_move]

    if opponent_move == your_modified_move:
        return 'draw'
    elif key_wins_over_value_dict[opponent_move] == your_modified_move:
        return 'opponent'
    else:
        return 'you'

def main():
    split_moves_list = get_split_moves_list_from_input_file('first_input.txt')
    score_list = [calculate_score_for_move(move) for move in split_moves_list]
    print(sum(score_list))

if __name__=="__main__":
    main()