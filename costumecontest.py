n = int(input())
a=[]
for i in range(n):
    b = input()
    a.append(b)
c = [a.count(_) for _ in a]
d =[]
for i in a:
    if a.count(i) == min(c):
        d.append(i)
d=list(set(d))
d.sort()
print('\n'.join(d))