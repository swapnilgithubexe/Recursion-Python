import sys
sys.setrecursionlimit(10**8)

def helper(arr, k, i, ans, output):
    if k == 0:
        output.append(ans.copy())
        return

    if i >= len(arr):
        return

    if arr[i] <= k:
        ans.append(arr[i])
        helper(arr, k - arr[i], i+1, ans, output)
        ##backtrack
        ans.pop()

    helper(arr, k, i+1,ans, output)

def subsetsSumsToK(arr, k):
    output = []
    helper(arr, k, 0, [], output)
    return output

if __name__ == "__main__":
    print(subsetsSumsToK([5, 12, 3, 17, 1, 18, 15, 3, 17,], 6))