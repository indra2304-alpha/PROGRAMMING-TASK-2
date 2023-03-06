n = int(input().strip())
t = tuple(int(i) for i in input().strip().split())

print(hash(t))
