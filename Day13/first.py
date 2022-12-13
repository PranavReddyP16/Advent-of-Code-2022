def handle_input():
    with open('input.txt') as input_file:
        input = input_file.read()
        str_list_of_pairs = input.split('\n\n')

        list_of_pairs = format_pair(str_list_of_pairs)
        return list_of_pairs

def format_pair(str_list_of_pairs):
    list_of_pairs = []
    for str_pair in str_list_of_pairs:
        str_pair1, str_pair2 = str_pair.split('\n')
        pair1 = format_list(str_pair1)
        pair2 = format_list(str_pair2)

        list_of_pairs.append([pair1, pair2])

    return list_of_pairs

def format_list(list_str):
    if list_str.isnumeric():
        return int(list_str)
    
    if list_str == '[]':
        return []

    sub_str = list_str[1:-1]

    list_items = []
    cur_item = ""
    cur_value=0
    for character in sub_str:
        if character == ',' and cur_value == 0:
            list_items.append(cur_item)
            cur_item = ""
            continue
        if character == '[':
            cur_value += 1
        if character == ']':
            cur_value -= 1

        cur_item += character
    list_items.append(cur_item)

    list_items = [format_list(list_item) for list_item in list_items]
    return list_items

def compare_pair(item1, item2):
    if isinstance(item1, int) and isinstance(item2, int):
        if item1<item2:
            return 'less'
        elif item1>item2:
            return 'more'
        else:
            return 'equal'

    if isinstance(item1, int) and isinstance(item2, list):
        return compare_pair([item1], item2)
    
    if isinstance(item1, list) and isinstance(item2, int):
        return compare_pair(item1, [item2])

    if isinstance(item1, list) and isinstance(item2, list):
        index=0
        if index>=len(item1) and index<len(item2):
            return 'less'
        elif index>=len(item2) and index<len(item1):
            return 'more'
        elif index>=len(item1) and index>=len(item2):
            return 'equal'

        while compare_pair(item1[index], item2[index]) == 'equal':
            index+=1
            if index>=len(item1) and index<len(item2):
                return 'less'
            elif index>=len(item2) and index<len(item1):
                return 'more'
            elif index>=len(item1) and index>=len(item2):
                return 'equal'

        return compare_pair(item1[index], item2[index])

def main():
    list_of_pairs = handle_input()
    answers = [compare_pair(pair[0], pair[1]) for pair in list_of_pairs]

    final_answer=0
    for index, answer in enumerate(answers, 1):
        if answer=='less': final_answer+=index
    print(final_answer)


if __name__=='__main__':
    main()