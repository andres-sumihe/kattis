n = int(input())
negatif_N = 0
temperature = input().split(" ")
for i in range(n):
    if int(temperature[i]) < 0:
        negatif_N+=1
print(negatif_N)