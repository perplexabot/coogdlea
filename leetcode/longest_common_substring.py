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
                                                                    # this +1 takes care of the case when the string is of size 1, 
                                                                    # in any other case it 
    d = [ set( s[i:j] for i in range( len(s) ) for j in range( i+1, len(s)+1 ) ) for s in strs ]
    u = set.intersection( *d ) if d else set()
    return '' if not u else max( u , key=len)

a = longestCommonPrefix(["hello"])
# assert a == 'hello'
print(a)

b = longestCommonPrefix(['hello', 'lets see if this works'])
print(b)
# assert b == 'o'

c = longestCommonPrefix(["flower","flow","flight"])
print(c)
# assert c == 'fl'

d = longestCommonPrefix(["dog","racecar","car"])
print(d)
# assert d == ''

e = longestCommonPrefix(["123456789","2345678","3456"])
print(e)
# assert e == '3456'

f = longestCommonPrefix(["i","i","i"])
print(f)
# assert f == 'i'

g = longestCommonPrefix([])
print(g)
# assert g == 'i'

print('***********')
# for some reason the answer should be '' here
h = longestCommonPrefix(["ca","a"])
print(h)
assert h == ''
