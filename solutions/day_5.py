text_path = "solutions/inputs/day_5.txt" # Path to the input file

file = open(text_path, 'r')


page_ordering_rules = []
numbers_of_each_update = []
end_page_ordering_rules = False

arrays = []
total = 0

for line in file:

    line = line.strip()

    if(line == ''):
        end_page_ordering_rules = True
        continue

    if(not end_page_ordering_rules):
        page_ordering_rules.append(line.split("|"))
    else:
        line = line.split(",")
        numbers_of_each_update.append(line)

def is_update_line_correctly_ordered(line):
    for number in line:
        for i in page_ordering_rules:
            if(number in i and i[1] in line and i[1] != number):
                idx = line.index(number)
                idx2 = line.index(i[1])

                order_is_valid = idx < idx2
                if(not order_is_valid):
                    return False
    return True

def sum_of_middles(arrays):
    total = 0
    for array in arrays:
        middle_idx = len(array) // 2
        total += int(array[middle_idx])
    return total

for i in numbers_of_each_update:
    if(is_update_line_correctly_ordered(i)):
        arrays.append(i)

print(sum_of_middles(arrays))


#PART TWO

invalid_arrays = []

def is_update_line_incorrectly_ordered(line):
    for number in line:
        for i in page_ordering_rules:
            if(number in i and i[1] in line and i[1] != number):
                idx = line.index(number)
                idx2 = line.index(i[1])

                order_is_valid = idx < idx2
                if(not order_is_valid):
                    aux = line[idx]
                    line[idx] = line[idx2]
                    line[idx2] = aux

                    new_line = line.copy()

                    if(not is_update_line_incorrectly_ordered(new_line)):
                        invalid_arrays.append(new_line)
                    return True
    return False


for i in numbers_of_each_update:
    is_update_line_incorrectly_ordered(i)

print(sum_of_middles(invalid_arrays))
