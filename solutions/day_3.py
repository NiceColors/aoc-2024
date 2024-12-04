text_path = "solutions/inputs/day_3.txt" # Path to the input file

file = open(text_path, 'r')

text= ""

for line in file:
    text += line

counter = 0

numbers = []
 
text = text.split('mul(')

enable = True


for item in text:

    aux = ""

            
    if(enable and item[0].isdigit()):
        for letter in item:
            if(letter.isdigit() or (len(aux)>0)and letter == ','):
                aux += letter
            elif letter == ')' and len(aux)>0:
                numbers.append(aux)
                break
            else:
                aux = ""
                break
        
    if("don't()" in item or "do()" in item):
        enable = "do()" in item
    if("don't()" in item and "do()" in item):
        dont_index = item.index("don't()")
        do_index = item.index("do()")
        if(dont_index < do_index):
            enable = False
        break

  
            
for number in numbers:
    number = number.split(",")
    if len(number) == 2:
        if len(number[0]) > 3 or len(number[1]) > 3 or len(number[0]) < 1 or len(number[1]) < 1:
            continue
        counter += (int(number[0]) * int(number[1]))

print(counter)

