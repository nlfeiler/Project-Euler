sum = 0
for i in range(505000):
    if((i*i) % 2 == 1):
        sum += i*i
print(sum)