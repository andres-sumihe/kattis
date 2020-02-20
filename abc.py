number = [int(i) for i in input().split(" ")]
number.sort()
index = []
for i in input():
    if i == 'A':
        index.append(number[0])
    if i == 'B':
        index.append(number[1])
    if i == 'C': 
        index.append(number[2])
for i in range(len(index)):
    print(index[i] if i ==-1 else index[i], end=" ")