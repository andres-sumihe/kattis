n = int(input())
for _ in range(n):
    pemberhentian = int(input()); people = 0
    for berhenti in range(pemberhentian):
        people = people + 0.5
        people = people * 2
    if pemberhentian == 0: print("0")
    else: print(str(int(people)))