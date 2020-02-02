n = int(input())

for y in range(1, n + 1):
    a = input().split(" ")
    m = int(a[1])
    pos = int((m * (m + 1)) / 2)
    even = m * (m + 1)
    odd = (m * (m + 1)) - m
    print(str(y) + " " + str(pos) + " " + str(odd) + " " + str(even))