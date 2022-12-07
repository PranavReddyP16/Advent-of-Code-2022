def handle_input():
    with open('input.txt') as input_file:
        input = input_file.read()
        terminal_output = input.split('\n')
        return terminal_output

def main():
    lines = handle_input()
    dir_size = {}
    dir_stack = []
    for line in lines:
        if line[0] == '$':
            words = line.split(' ')
            command = words[1]

            if command == 'cd':
                dir = words[2]
                if dir == '..':
                    dir_stack.pop()
                else:
                    dir_stack.append(dir)
        else:
            ls_output_words = line.split(' ')
            if ls_output_words[0] != 'dir':
                for level, cur_dir in enumerate(dir_stack):
                    dir_size['/'.join(dir_stack[:level+1])] = dir_size.get('/'.join(dir_stack[:level+1]), 0) + int(ls_output_words[0])

    ans=0
    for dir, size in dir_size.items():
        if size <= 100000:
            ans += size
            print(dir, size)

    print(ans)

if __name__=='__main__':
    main()