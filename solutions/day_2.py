text_path = "solutions/inputs/day_2.txt" # Path to the input file

file = open(text_path, 'r')


array = []

for line in file:
    array.append(list(map(int, line.strip().split())))

safe_count = 0


def verify_safety(arr):
    
    is_safe = True

    difference_between_elements = 0

    is_increasing = False
    is_decreasing = False


    for j in range(len(arr)):
        
        current = arr[j] 
        prev = arr[abs(j-1)]

        if current == prev:
            is_safe = False
            break
        if j > 0:

            difference_between_elements = abs(current - prev)
            
            if(not 1 <= difference_between_elements <= 3):
                is_safe = False
                break
        if(j != len(arr) -1):
            next = arr[j+1]
            if (current > next):
                is_decreasing = True
            else:
                is_increasing = True
        if(is_decreasing and is_increasing):
            is_safe = False
            break
    return is_safe

# PART ONE

for i in array:

    is_safe = verify_safety(i)
 
    if is_safe:
        safe_count+=1

print(safe_count)


# PART TWO


safe_count = 0
count = 0


for i in array:

    is_safe = False

    for level in range(len(i)):
        
        array_copy = i[:]
        array_copy.pop(level)

        safety = verify_safety(array_copy)
        if(safety):
            print(i, count+1)
            is_safe = True
            break

    if is_safe:
        safe_count+=1
    count += 1
    
print(safe_count)

