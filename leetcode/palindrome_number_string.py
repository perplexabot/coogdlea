# Determine whether an integer is a palindrome. An integer is a palindrome
# when it reads the same backward as forward.
# 
# Example 1:
#     in:     121
#     out:    true
# 
# Example 2:
#     in:     -121
#     out:    false
# 
# Example 3:
#     in:     10
#     out:    false
# 
# Follow up:
#     Could you solve it without converting the integer to a string?

def isPalindrome(x):
    xStr = str(x)
    if len(xStr) < 2:
        return True
    
    l = 0 
    r = len(xStr) - 1

    while l < r:
        if xStr[l] != xStr[r]:
            return False
        l += 1
        r -= 1
    return True
            

a = 121
ans = isPalindrome(a)
print( ''.join( [ 'a: ', str(a), '\nans: ', str(ans) ] ) )
print( '-------------------------------------------------')

a = -121
ans = isPalindrome(a)
print( ''.join( [ 'a: ', str(a), '\nans: ', str(ans) ] ) )
print( '-------------------------------------------------')

a = 10
ans = isPalindrome(a)
print( ''.join( [ 'a: ', str(a), '\nans: ', str(ans) ] ) )
print( '-------------------------------------------------')

a = 111
ans = isPalindrome(a)
print( ''.join( [ 'a: ', str(a), '\nans: ', str(ans) ] ) )
print( '-------------------------------------------------')

a = 1022351346246
ans = isPalindrome(a)
print( ''.join( [ 'a: ', str(a), '\nans: ', str(ans) ] ) )
print( '-------------------------------------------------')

a = -345234
ans = isPalindrome(a)
print( ''.join( [ 'a: ', str(a), '\nans: ', str(ans) ] ) )
print( '-------------------------------------------------')

a = 1110111
ans = isPalindrome(a)
print( ''.join( [ 'a: ', str(a), '\nans: ', str(ans) ] ) )
print( '-------------------------------------------------')
