safe_digits = 0

with open("Day 2/Input.txt","r") as f:
    data = f.readlines()
    
    
betterdata = []
for line in data:
     betterdata.append(line.strip().split())


convert_to_int = []

for line in betterdata:
    list = []
    for digit in line:
        list.append(int(digit))
    convert_to_int.append(list)

#Logic

for line in convert_to_int:
    safe = False
    testing_descending = False
    for i in range(len(line)):
        if i == 1:
            if line[i] < line[i-1] and line[i-1] - line[i] <= 3:
                testing_descending = True
            elif line[i] > line[i-1] and line[i] - line[i-1] <= 3:
                continue
            else:
                break
        if i > 1 and testing_descending:
            if line[i] < line[i-1] and line[i-1] - line[i] <= 3:
                safe = True
            else:
                safe = False
                break
        if i > 1 and not testing_descending:
            if line[i] > line[i-1] and line[i] - line[i-1] <= 3:
                safe = True
            else:
                safe = False
                break
    if safe:
        safe_digits += 1

print(safe_digits)