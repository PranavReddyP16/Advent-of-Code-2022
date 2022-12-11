from functools import total_ordering
from tqdm import tqdm
from pympler.asizeof import asizeof
import math
import copy

@total_ordering
class Monkey:
    def __init__(self, starting_items, op1, op2, operation, divisible_by, monkey_if_true, monkey_if_false):
        self.starting_items = starting_items
        self.op1 = op1
        self.op2 = op2
        self.operation = operation
        self.divisible_by = divisible_by
        self.monkey_if_true = monkey_if_true
        self.monkey_if_false = monkey_if_false
        self.number_of_inspections = 0

    def inspect(self, item, lcm):
        operation_function = self.__get_func_from_operands(lcm)
        operation_value = operation_function(item)

        self.number_of_inspections += 1
        return operation_value


    def check(self, item):
        return item % self.divisible_by == 0

    def __get_func_from_operands(self, lcm):
        def operation_function(item):
            left_op = item if self.op1=='old' else int(self.op1)
            right_op = item if self.op2=='old' else int(self.op2)

            if self.operation == '*':
                return (left_op * right_op) % lcm
            elif self.operation == '+':
                return (left_op + right_op) % lcm
            else:
                return

        return operation_function

    def __repr__(self):
        return str(self.starting_items)

    def __eq__(self, other):
        return self.number_of_inspections == other.number_of_inspections

    def __lt__(self, other):
        return self.number_of_inspections < other.number_of_inspections

def handle_input():
    with open('input.txt') as input_file:
        input = input_file.read()
        monkey_descriptions = input.split('\n\n')

        monkey_details = []
        
        for monkey_number, description in enumerate(monkey_descriptions):
            lines = description.split('\n')

            # Starting Items
            starting_items = lines[1].split(' ')[4:]
            starting_items = [starting_item[:-1] if starting_item[-1]==',' else starting_item for starting_item in starting_items]
            starting_items = [int(starting_item) for starting_item in starting_items]

            # Operation
            op1, operation, op2 = lines[2].split(' ')[5:]

            # Test
            divisible_by = int(lines[3].split(' ')[5])

            # True
            monkey_if_true = int(lines[4].split(' ')[9])

            # False
            monkey_if_false = int(lines[5].split(' ')[9])

            monkey_details.append(Monkey(starting_items, op1, op2, operation, divisible_by, monkey_if_true, monkey_if_false))

        return monkey_details

def throw(monkey1, monkey2, item_to_throw):
    del monkey1.starting_items[0]
    monkey2.starting_items.append(item_to_throw)

def finish_round(monkeys, lcm):
    monkeys = copy.deepcopy(monkeys)
    for monkey in monkeys:
        for _ in range(len(monkey.starting_items)):
            item_to_throw = monkey.inspect(monkey.starting_items[0], lcm) 
            if monkey.check(item_to_throw):
                throw(monkey, monkeys[monkey.monkey_if_true], item_to_throw)
            else:
                throw(monkey, monkeys[monkey.monkey_if_false], item_to_throw)

    return monkeys

def main():
    monkeys = handle_input()
    number_of_rounds = 10000

    lcm = math.prod([monkey.divisible_by for monkey in monkeys])
    print(lcm)

    for _ in tqdm(range(number_of_rounds)):
        monkeys = finish_round(monkeys, lcm)

    first_place, second_place = sorted(monkeys)[-2:]
    print(first_place.number_of_inspections * second_place.number_of_inspections)

if __name__=='__main__':
    main()