colors = "aabaa"
neededTime = [1,2,3,4,1]
output = 0

for i in range(1, len(colors)):
    if colors[i] == colors[i-1]:
        lowest = min(neededTime[i], neededTime[i-1])
        output += lowest
        print(output)


print(output)
