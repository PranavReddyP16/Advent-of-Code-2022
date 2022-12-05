import numpy as np

def handle_input():
    with open('input.txt') as input_file:
        input = input_file.read()
        initial_stack, moves_string = input.split('\n\n')
        moves_list = moves_string.split('\n')

        char_array_2d = [list(row) for row in initial_stack.split('\n')]
        char_array_2d.pop()
        char_array_2d = char_array_2d[::-1]

        list_of_stacks = []
        for col in range(len(char_array_2d[0])):
            cur_stack = []
            for row in range(len(char_array_2d)):
                cur_char = char_array_2d[row][col]
                if cur_char.isalpha():
                    cur_stack.append(cur_char)
            
            if cur_stack:
                list_of_stacks.append(cur_stack)
        
    with open('nice_input.txt', 'w') as output_file:
        output_file.write(f'{len(list_of_stacks)}\n')
        for stack in list_of_stacks:
            # print(stack)
            output_file.write(f'{len(stack)}\n')
            for element in stack:
                output_file.write(f'{element} ')
            output_file.write('\n')

        output_file.write(f'\n{len(moves_list)}\n')
        for move in moves_list:
            split_move = move.split(' ')
            for element in split_move:
                if element.isnumeric():
                    output_file.write(f'{element} ')
            output_file.write('\n')


handle_input()