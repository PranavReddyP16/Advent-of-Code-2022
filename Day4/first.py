def main():
    input_list = handle_input()
    score_list = [does_pair_have_overlap(pair) for pair in input_list]
    print(sum(score_list))

def handle_input():
    with open('input.txt') as input_file:
        input_string = input_file.read()
        input_list = input_string.split('\n')
        return input_list

def does_pair_have_overlap(pair):
    first_range, second_range = split_pair(pair)
    lower_first_range, upper_first_range = get_bounds_of_range(first_range)
    lower_second_range, upper_second_range = get_bounds_of_range(second_range)

    if lower_first_range <= lower_second_range and upper_first_range >= upper_second_range:
        return True
    elif lower_second_range <= lower_first_range and upper_second_range >= upper_first_range:
        return True
    else:
        return False

def split_pair(pair):
    first_range, second_range = pair.split(',')
    return first_range, second_range

def get_bounds_of_range(range):
    range_lower, range_upper = range.split('-')
    return int(range_lower), int(range_upper)

if __name__=='__main__':
    main()
