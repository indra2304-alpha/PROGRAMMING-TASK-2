from collections import Counter

input()
print(Counter(input().split()).most_common()[-1][0])
