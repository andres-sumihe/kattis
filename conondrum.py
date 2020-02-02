text = input(); per = "PER"; days = 0
for i in range(len(text)):
    if text[i] != per[i % 3]:days += 1
print(str(days))