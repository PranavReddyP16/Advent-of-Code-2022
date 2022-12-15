import numpy as np

def handle_input():
    with open('input.txt') as input_file:
        input = input_file.read()
        path_string_list = input.split('\n')

        return [split_path(path) for path in path_string_list]

def split_path(path):
    coords_list = path.split(' -> ')
    coords_list = [[int(axis) for axis in coord.split(',')] for coord in coords_list]
    return coords_list

def fill_path(grid, path):
    for index in range(len(path)-1):
        x1, y1 = path[index]
        x2, y2 = path[index+1]

        if x1==x2:
            min_y = min(y1, y2)
            max_y = max(y1, y2)
            grid[x1, min_y:max_y+1] = 1
        else:
            min_x = min(x1, x2)
            max_x = max(x1, x2)
            grid[min_x:max_x+1, y1] = 1

    return grid

def count_static_blocks(original_grid):
    grid = original_grid.copy()
    ans=0
    cur_pos = [500, 0]
    while True:
        x, y = cur_pos
        if y == 199:
            break
        if grid[x][y+1] == 0:
            cur_pos = [x, y+1]
        elif grid[x-1][y+1] == 0:
            cur_pos = [x-1, y+1]
        elif grid[x+1][y+1] == 0:
            cur_pos = [x+1, y+1]
        else:
            grid[x][y] = 1
            ans+=1
            cur_pos = [500, 0]

    return ans

def main():
    paths = handle_input()
    grid = np.zeros((600, 200))
    for path in paths:
        grid = fill_path(grid, path)

    # print(grid[494:504, :10])
    print(count_static_blocks(grid))

if __name__=='__main__':
    main()