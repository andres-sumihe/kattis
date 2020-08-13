n = int(input())
a = []
for i in range(n):
    b = input()
    a.append((int(b[:-1])**int(b[-1])))
print(sum(a))