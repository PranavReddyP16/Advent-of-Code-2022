def get_split_moves_list_from_input_file(input_file_name):
    with open(input_file_name) as input_file:
        input_string = input_file.read()
        moves_list = input_string.split('\n')
        split_moves_list = [individual_move.split(' ') for individual_move in moves_list]
        return split_moves_list

def calculate_score_for_move(move):
    score_dict = {
        'A': 1,
        'B': 2,
        'C': 3,
    }

    result_dict = {
        'X': 0,
        'Y': 3,
        'Z': 6,
    }

    opponent_move = move[0]
    result = move[1]

    your_move = get_move_from_result(opponent_move, result)

    final_score = score_dict[your_move] + result_dict[result]
    return final_score

def get_move_from_result(opponent_move, result):
    key_wins_over_value_dict = {
        'B': 'A',
        'C': 'B',
        'A': 'C',
    }

    if result == 'X':
        your_move = key_wins_over_value_dict[opponent_move]
    elif result == 'Y':
        your_move = opponent_move
    else:
        value_loses_over_key_dict = {v: k for k, v in key_wins_over_value_dict.items()}
        your_move = value_loses_over_key_dict[opponent_move]

    return your_move

def main():
    split_moves_list = get_split_moves_list_from_input_file('first_input.txt')
    score_list = [calculate_score_for_move(move) for move in split_moves_list]
    print(sum(score_list))

if __name__=="__main__":
    main()