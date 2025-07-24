# Recursive function to generate all
# subsequences with sum of elements k
def findSubsequence(ind, sum, k, cur, arr, res):
    n = len(arr)
    
    
    if ind == n:
        
        # check if sum of elements of current
        # subset is equal to k
        if sum == k:
            
            # add the subset in result
            res.append(cur.copy())
        return
    
    # skip the current element arr[ind]
    findSubsequence(ind + 1, sum, k, cur, arr, res)
    
    # add the current element in subset
    cur.append(arr[ind])
    findSubsequence(ind + 1, sum + arr[ind], k, cur, arr, res)
    
    cur.pop()

def subsequencesSumK(arr, k):
    
    res = []
    
    # to store the current subset
    cur = []
    
    findSubsequence(0, 0, k, cur, arr, res)
    
    return res

arr = list(map(int, input().split()))
k = int(input())
result = subsequencesSumK(arr, k)
print(result)