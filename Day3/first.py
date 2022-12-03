def main():
    sack_list = handle_input()
    scores_per_sack = [get_score_for_sack(sack_string) for sack_string in sack_list]

    print(sum(scores_per_sack))

def handle_input():
    with open('input.txt') as input_file:
        input_string = input_file.read()
        input_list = input_string.split('\n')

        return input_list

def get_score_for_sack(sack_string):
    first_half, second_half = split_sack(sack_string)
    common_letters = list(set(first_half).intersection(set(second_half)))

    scores_per_letter = [get_score_for_letter(letter) for letter in common_letters]

    return sum(scores_per_letter)

def split_sack(sack_string):
    assert(len(sack_string)%2 == 0)

    halfway_index = len(sack_string)//2
    first_half = sack_string[:halfway_index]
    second_half = sack_string[halfway_index:]

    return first_half, second_half

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
