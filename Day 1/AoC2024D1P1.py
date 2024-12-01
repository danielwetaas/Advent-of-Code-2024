data = []
output = 0

with open("Input.txt","r") as f:
    list = f.readlines()
    splitted = [line.split() for line in list]
    for line in splitted:
        temp = [int(line[0]),int(line[1])]
        data.append(temp)
    print(data)

    for line in data:
        output += abs(line[0]-line[1])

print(output)

