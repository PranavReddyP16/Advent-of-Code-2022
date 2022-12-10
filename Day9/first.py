from math import sqrt

def handle_input():
    with open('input.txt') as input_file:
        input = input_file.read()
        squashed_moves = input.split('\n')

        moves = []
        for squashed_move in squashed_moves:
            direction, frequency = squashed_move.split(' ')
            for _ in range(int(frequency)):
                moves.append(direction)

        return moves

class Head:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def next(self, move):
        if move=='R':
            self.x += 1
        elif move=='L':
            self.x -=1
        elif move=='U':
            self.y += 1
        else:
            self.y -=1

def get_nearest_pos(head, tail_x, tail_y):
    adj = [
        (head.x-1, head.y),
        (head.x+1, head.y),
        (head.x, head.y-1),
        (head.x, head.y+1),
    ]

    initial_distance = get_distance(head.x, head.y, tail_x, tail_y)
    if initial_distance < 2:
        return (tail_x, tail_y)

    min_dist_pos = 0
    min_dist = 3
    for index, adj_pos in enumerate(adj):
        distance = get_distance(adj_pos[0], adj_pos[1], tail_x, tail_y)
        if distance < min_dist:
            min_dist = distance
            min_dist_pos = index
    return adj[min_dist_pos]

def get_distance(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1-y2)**2)

def main():
    moves = handle_input()
    finished_positions = set()

    head = Head(0, 0)
    tail_x = 0
    tail_y = 0
    for move in moves:
        head.next(move)
        next_tail_pos = get_nearest_pos(head, tail_x, tail_y)
        # print(nexs_tail_pos)
        finished_positions.add(next_tail_pos)
        tail_x = next_tail_pos[0]
        tail_y = next_tail_pos[1]

    print(len(finished_positions))

if __name__=='__main__':
    main()