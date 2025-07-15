def getFloorAndCeil(a, n, x):
    # Write your code here.
    if a[0] > x:
        return (-1 ,a[0])
    if a[n-1] <x:
        return (a[n-1], -1)
    l=0
    r=n-1
    ans = 0
    while(l<=r):
        mid = (l+r)//2
        if a[mid] ==x:
            return (a[mid] ,a[mid])
        elif a[mid] < x:
            ans = mid+1
            l = mid +1
        else:
            r = mid -1
    return (a[ans-1] ,a[ans])

arr = list(map(int, input().split()))
x = int(input())
n = len(arr)
sol = getFloorAndCeil(arr, n, x)
print(sol[0], sol[1])