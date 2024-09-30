import sys
sys.setrecursionlimit(10**6)

def helper(arr, n, i, ans, output):
    if i == n:
        output.append(ans.copy())
        return

    helper(arr, n,i+1, ans, output)

    ans.append(arr[i])
    helper(arr, n, i+1, ans, output)
    ans.pop()


def subsetsOfArray(arr):
    n = len(arr)
    if n == 0:
        return []

    output = []
    helper(arr, n, 0, [], output)
    return output


if __name__ == "__main__":
    print(subsetsOfArray([1,2,3 ]))