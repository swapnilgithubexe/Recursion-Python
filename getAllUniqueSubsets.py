def helper(arr, i, n, ans, output):
    if i == n:
        output.append(ans.copy())
        return

    ans.append(arr[i])
    helper(arr, i+1, n, ans, output)
    ans.pop()

    while i + 1 < n and arr[i] == arr[i+1]:
        i+=1

    helper(arr, i+1, n, ans, output)

def getAllUniqueSubsets(arr):
    arr.sort()
    n = len(arr)
    if n == 0:
        return []
    output = []
    helper(arr, 0, n, [], output)
    return output

if __name__ == "__main__":
    print(getAllUniqueSubsets([1,2,2,4,4]))
