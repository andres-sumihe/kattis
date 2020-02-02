import  math

while True:
    a = input().split(' ')
    r = float(a[0])
    if r == 0:
        break
    m = int(a[1])
    c = int(a[2])

    sebenarnya = math.pi * (r ** 2)
    area_kotak = (r * 2) * (r * 2)
    rasio = c / m
    perkiraan = area_kotak * rasio

    result = str(sebenarnya) + ' ' + str(perkiraan)

    print(result)