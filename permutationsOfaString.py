def swap(s, i, j):
    s[i], s[j] = s[j], s[i]
def helper(s, ans, i):
    if i >= len(s):
        ans.append("".join(s))

    for j in range(i, len(s)):
        swap(s,i,j)
        helper(s, ans, i+1)
        swap(s,i,j)
def permutationsOfString(string):
    s = list(string)
    ans = []
    helper(s,ans, 0)
    return ans

if __name__ == "__main__":
    print(permutationsOfString("abc"))
