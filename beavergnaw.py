from math import pi

while True:
    D, V = [int(i) for i in input().split(' ')]
    if D == 0 and V == 0:break
    print(((((-6) * V) / pi) + (D * D * D)) ** (1 / 3))