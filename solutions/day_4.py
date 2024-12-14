text_path = "solutions/inputs/day_4.txt" # Path to the input file

file = open(text_path, 'r')


array = []

for line in file:
    array.append(list(line.strip()))


phrase = "XMAS"

counter = list()

def find_phrases(array):
    counter = []
    
    for i in range(len(array)):
        for j in range(len(array[i])):
            current_phrase = array[i][j]
            first_letter = phrase[0]
            
            if current_phrase == first_letter:
                row, col = i, j
                found_positions = []
                
                if col + len(phrase) <= len(array[row]):
                    sliced_array = array[row][col:col+len(phrase)]
                    if "".join(sliced_array) == phrase:
                        found_positions = [[row, col + k] for k in range(len(phrase))]
                        counter.append(found_positions)
                    elif "".join(sliced_array) == phrase[::-1]:
                        found_positions = [[row, col + k] for k in range(len(phrase)-1, -1, -1)]
                        counter.append(found_positions)
                
                if col - len(phrase) >= -1:
                    sliced_array = array[row][col-len(phrase)+1:col+1]
                    if "".join(sliced_array) == phrase:
                        found_positions = [[row, k] for k in range(col-len(phrase)+1, col+1)]
                        counter.append(found_positions)
                    elif "".join(sliced_array) == phrase[::-1]:
                        found_positions = [[row, k] for k in range(col, col-len(phrase), -1)]
                        counter.append(found_positions)
                
                if row + len(phrase) <= len(array):
                    vertical_slice = []
                    positions = []
                    for k in range(len(phrase)):
                        vertical_slice.append(array[row + k][col])
                        positions.append([row + k, col])

                    if "".join(vertical_slice) == phrase:
                        counter.append(positions)
                    elif "".join(vertical_slice) == phrase[::-1]:
                        counter.append(positions[::-1])
                
                if row - len(phrase) >= -1:
                    vertical_slice = []
                    positions = []
                    for k in range(len(phrase)):
                        vertical_slice.append(array[row - k][col])
                        positions.append([row - k, col])
                        
                    if "".join(vertical_slice) == phrase:
                        counter.append(positions)
                    elif "".join(vertical_slice) == phrase[::-1]:
                        counter.append(positions[::-1])
                
                directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
                
                for row_dir, col_dir in directions:
                    diagonal_slice = []
                    positions = []
                    valid = True
                    
                    for k in range(len(phrase)):
                        new_row = row + (k * row_dir)
                        new_col = col + (k * col_dir)
                        
                        if new_row < 0 or new_row >= len(array) or new_col < 0 or new_col >= len(array[0]):
                            valid = False
                            break
                            
                        diagonal_slice.append(array[new_row][new_col])
                        positions.append([new_row, new_col])
                    
                    if valid:    
                        if "".join(diagonal_slice) == phrase:
                            counter.append(positions)
                        elif "".join(diagonal_slice) == phrase[::-1]:
                            counter.append(positions[::-1])

    return counter
        

print(len(find_phrases(array)))

