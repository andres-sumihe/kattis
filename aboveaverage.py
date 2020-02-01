n = int(input())
for i in range(n):
    s = list(input().split());a = int(s[0]);x = 0;del s[0];w = sum(int(j) for j in s) / a
    for j in s:
        if int(j)>w:x+=1
    print('{:.3f}%'.format((x/a)*100))