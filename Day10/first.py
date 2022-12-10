def handle_input():
    with open('input.txt') as input_file:
        input = input_file.read()
        operations = input.split('\n')

        return operations

def main():
    operations = handle_input()
    current_cycle=1
    X = 1
    ans=0
    important_cycles = [20, 60, 100, 140, 180, 220]
    for operation in operations:
        if current_cycle in important_cycles:
            ans += X*current_cycle
        
        if operation == 'noop':
            current_cycle+=1
        else:
            value = int(operation.split(' ')[1])
            current_cycle+=1
            if current_cycle in important_cycles:
                ans += X*current_cycle
            current_cycle+=1
            X += value
    
    print(ans)

if __name__=='__main__':
    main()