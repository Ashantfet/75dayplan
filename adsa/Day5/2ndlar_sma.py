def getSecondOrderElements(n: int, arr: list[int]) -> list[int]:
    
    maxi = arr[0]
    mini = arr[0]
    for i in range(1, n):
        if arr[i] > maxi:
            maxi = arr[i]
        if arr[i] < mini:
            mini = arr[i]

    
    max2 = float('-inf')
    min2 = float('inf')

    
    for i in range(n):
        if arr[i] != maxi and arr[i] > max2:
            max2 = arr[i]
        if arr[i] != mini and arr[i] < min2:
            min2 = arr[i]

    return [max2, min2]

arr = list(map(int, input().split()))
n = len(arr)
sol = getSecondOrderElements(n, arr)
print(*sol)