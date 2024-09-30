##This case handles the duplicate values
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def helper(arr, ans, i):
    if i >= len(arr):
        ans.append(arr[:])
        return
    seen = set()
    for j in range(i, len(arr)):
        if arr[j] in seen:
            continue
        seen.add(arr[j])
        swap(arr, i, j)
        helper(arr, ans, i+1)
        swap(arr, i, j)
def permutationOfIntegers(arr):
    ans = []
    helper(arr, ans, 0)
    return ans

if __name__ == "__main__":
    print(permutationOfIntegers([1,1,2]))