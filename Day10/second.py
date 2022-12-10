import numpy as np

def handle_input():
    with open('input.txt') as input_file:
        input = input_file.read()
        operations = input.split('\n')

        return operations

def advance_crt(x, y):
    y+=1
    if y>39:
        y=0
        x+=1
    return x, y

def main():
    operations = handle_input()
    crt_pos = (0, 0)
    X = 1
    ans = np.chararray((6, 40), unicode=True)
    for operation in operations:
        if crt_pos[0] in [X-1, X, X+1]:
            ans[crt_pos[0]][crt_pos[1]] = '#'
        else:
            ans[crt_pos[0]][crt_pos[1]] = '.'
        
        if operation == 'noop':
            crt_pos = advance_crt(*crt_pos)
        else:
            value = int(operation.split(' ')[1])
            crt_pos = advance_crt(*crt_pos)
            if crt_pos[0] in [X-1, X, X+1]:
                ans[crt_pos[0]][crt_pos[1]] = '#'
            else:
                ans[crt_pos[0]][crt_pos[1]] = '.'
            crt_pos = advance_crt(*crt_pos)
            X += value
        print(crt_pos)
    
    with open('output.txt', 'w') as output_file:
        output_file.write(str(ans))

if __name__=='__main__':
    main()