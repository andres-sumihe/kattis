while True:
    a = sorted(list(map(int,input().split())))
    if all([a[0]==0, a[1]==0, a[2]==0]):break
    x = (a[0]**2)+(a[1]**2);print('right' if x == a[2]**2 else 'wrong')