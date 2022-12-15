# Write a function to find the longest common prefix string amongst an array of strings.
# 
# If there is no common prefix, return an empty string "".
# 
# Example 1:
#     Input: ["flower","flow","flight"]
#     Output: "fl"
# Example 2:
#     Input: ["dog","racecar","car"]
#     Output: ""
# 
# Explanation: There is no common prefix among the input strings.
# Note:
#   All given inputs are in lowercase letters a-z.

def longestCommonPrefix(strs):
    # input list[str]
    # output str
    if not strs:
        return ''

    loops = len( min( strs, key=len) )
    i = 0

    while i < loops and all( strs[x][i] == strs[0][i] for x in range( 1, len(strs) ) ):
        i += 1

    return strs[0][:i]

a = longestCommonPrefix(["hello"])
# print(a)
assert a == 'hello'

b = longestCommonPrefix(['hello', 'lets see if this works'])
# print(b)
assert b == ''

c = longestCommonPrefix(["flower","flow","flight"])
# print(c)
assert c == 'fl'

d = longestCommonPrefix(["dog","racecar","car"])
# print(d)
assert d == ''

e = longestCommonPrefix(["123456789","2345678","3456"])
# print(e)
assert e == ''

f = longestCommonPrefix(["i","i","i"])
# print(f)
assert f == 'i'

g = longestCommonPrefix([])
# print(g)
assert g == ''

h = longestCommonPrefix(["ca","a"])
# print(h)
assert h == ''
