n = int(input())
a = map(int, input().split())
b = []
for i in a:
    if i >= 0:
        b.append(i)
print(sum(b)/len(b))