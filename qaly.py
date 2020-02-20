n = input()
qaly = []
for i in range(int(n)):
    a = [float(i) for i in input().split()]
    qaly.append((a[0]*a[1]))
print("%.3f"%sum(qaly))