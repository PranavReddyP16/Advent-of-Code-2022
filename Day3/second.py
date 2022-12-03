def main():
    sack_list = handle_input()
    group_list = [sack_list[start: start+3] for start in range(0, len(sack_list), 3)]

    scores_per_group = [get_score_for_group(group) for group in group_list]
    print(sum(scores_per_group))

def handle_input():
    with open('input.txt') as input_file:
        input_string = input_file.read()
        input_list = input_string.split('\n')

        return input_list

def get_score_for_group(group):
    first, second, third = group
    common_letters = list(set(first).intersection(set(second)).intersection(set(third)))

    scores_per_letter = [get_score_for_letter(letter) for letter in common_letters]

    return sum(scores_per_letter)

def get_score_for_letter(letter):
    if letter.isupper():
        score_relative_to_A = __ascii(letter) - __ascii('A') + 1
        final_score = score_relative_to_A + 26
    else:
        final_score = __ascii(letter) - __ascii('a') + 1

    return final_score

def __ascii(letter):
    return ord(letter)

if __name__=='__main__':
    main()
