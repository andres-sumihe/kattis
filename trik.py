string = input()
A = 2
B = 3
C = 1
index = 1
for i in string:
    if i == 'A':
        index = A
        A = 1
    if i == 'B':
        index = B
        B = 2
    if i == 'C':
        index = C
        c = 3
print(index)
