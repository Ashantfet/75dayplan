def upperBound(arr: list[int], x: int, n: int) -> int:
    # Write your code here.
    if arr[n-1]==x:
        return n
    l=0
    r=n-1
    ans=0
    while(l<=r):
        mid=(l+r)//2
        if arr[mid] <= x:
            ans =mid+1
            l= mid+1
        else:
            r=mid-1
    return ans
arr = list(map(int, input().split()))
x = int(input())
n = len(arr)
sol = upperBound(arr, x, n)
print(sol)