set = 1
answer=[]
while True:
    n = int(input())
    if n == 0:break
    a = []
    for i in range(n):
        b = input()
        a.append(b)
    gj = 0
    gn = 1
    list1 = []
    list2 = []
    list3 = []
    for i in range(len(a)//2):
        list1.append(a[gn])
        list2.append(a[gj])
        gn += 2
        gj += 2
    if len(a)%2==1:
        list3.append(a[-1])
    list1.reverse()
    answer.append(("SET "+ str(set)))
    if len(a)%2==0:
        for i in list2:
            answer.append(i)
        for i in list1:
            answer.append(i)
    else:
        for i in list2:
            answer.append(i)
        for i in list3:
            answer.append(i)
        for i in list1:
            answer.append(i)
    set+=1
print("\n".join(answer))