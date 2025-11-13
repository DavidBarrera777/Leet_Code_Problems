from collections import Counter

nums = [1, 1, 2, 2, 3, 4, 2, 3]
k = 6
x = 2

answer = []

windows = zip(*(nums[i:] for i in range(k)))

for w in windows:
    counts = Counter(w)
    duplicates = [num for num, count in counts.items() for _ in range(count) if count > 1]
    duplicate_sum = sum(duplicates)
    answer.append(duplicate_sum)

print(answer)
