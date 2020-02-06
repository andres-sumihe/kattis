a = []
for i in range(2):
    c = input()
    a.append(c)
if int(a[0]) < 0 and int(a[1]) > 0:print("2")
elif int(a[0]) > 0 and int(a[1]) > 0:print("1")
elif int(a[0]) < 0 and int(a[1]) < 0:print("3")
else :print("4")
