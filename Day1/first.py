def get_sum_of_elf(calorie_string):
    calorie_string_list = calorie_string.split('\n')
    calorie_list = [int(calorie_string) for calorie_string in calorie_string_list]
    return sum(calorie_list)

with open('first_input.txt') as input_file:
    input = input_file.read()
    
    split_input = input.split('\n\n')
    
    list_of_total_calories = [get_sum_of_elf(string_of_individual_calorie_list) for string_of_individual_calorie_list in split_input]
    print(max(list_of_total_calories))