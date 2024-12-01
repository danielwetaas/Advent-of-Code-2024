output = 0

with open("Day 1\Input.txt","r") as f:
    list = f.readlines()
    splitted = [line.split() for line in list]

    unsorted = []
    for line in splitted:
        temp = [int(line[0]),int(line[1])]
        unsorted.append(temp)
    
    leftlist = []
    rightlist = []
    for digits in unsorted:
        leftlist.append(digits[0])
        rightlist.append(digits[1])
    leftlist.sort()
    rightlist.sort()
    

    
    
    for i in leftlist:
        dict = {}
        for j in rightlist:

            if i==j:
            
                if i in dict:
                    dict[i] += 1
                else:
                    dict[i] = 1
        for key, value in dict.items():
            output += key * value
print(output)