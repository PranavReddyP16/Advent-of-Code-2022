def main():
    with open('input.txt') as input_file:
        input = input_file.read()
        strings = input.split('\n')
        num_strings = len(strings)
    
    with open('nice_input.txt', 'w') as output_file:
        output_file.write(f'{num_strings}\n')
        for string in strings:
            output_file.write(f'{string}\n')

if __name__=='__main__':
    main()
