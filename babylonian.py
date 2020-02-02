def toInt(s):
    return 0 if s == '' else int(s)
n = int(input())
for i in range(n):
    vals = input().split(',')
    k = 0
    num = 0
    for j in range(len(vals) - 1,  - 1, -1):
        num += toInt(vals[j]) * (60 ** k)
        k += 1
    print(num)