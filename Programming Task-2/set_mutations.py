m = int(input().strip())
A = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    cmd, n = input().split()
    lis = set(map(int, input().split()))
    s = f"A.{cmd}({lis})"
    eval(s)
    
print(sum(A))
