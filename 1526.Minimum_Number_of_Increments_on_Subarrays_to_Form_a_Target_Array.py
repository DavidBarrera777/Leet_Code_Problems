target = [3,1,1,2]
output = target[0]


for i in range(1, len(target)):
    if target[i] > target[i-1]:
        output += target[i] - target[i - 1]


print(output)








