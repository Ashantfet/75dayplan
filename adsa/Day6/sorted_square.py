n = int(input())
arr = list(map(int,input().split()))
ans = sorted(x ** 2 for x in arr)
print(*ans)