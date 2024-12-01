text_path = "solutions/inputs/day_1.txt" # Path to the input file

file = open(text_path, 'r')

array_left = []
array_right = []

for line in file:
    left, right = map(int, line.strip().split())
    array_left.append(left)
    array_right.append(right)

array_left.sort()
array_right.sort()

array_size = len(array_right)

# PART ONE

distance = 0

for i in range(array_size):
    distance += abs(int(array_left[i]) - int(array_right[i]))

print("Distance: ", distance)

# PART TWO 

similarity_score = 0

for i in range(array_size):
    similarity_score += array_left[i] * array_right.count(array_left[i]) 

print("Similarity score: ", similarity_score)


