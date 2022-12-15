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
# try: 1000021

def isPalindrome(x):
    # if positive and single digit then palindrome
    if x > -1 and x < 10:
        return True

    # if negative then not palindrome
    if x < 0:
        return False

    # if positive with int having a number of digits greater than one
    # calculuate number of digits in x
    t = x
    lenX = 0
    while t > 0:
        t //= 10
        lenX += 1

    # iterate and compare left and right digits
    i = 0
    while i < lenX//2:
        if not ( x // (10**i)  ) % 10 == ( x // ( 10 ** (lenX-1-i) ) ) % 10:
            return False
        i += 1

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

a = 1000021
ans = isPalindrome(a)
print( ''.join( [ 'a: ', str(a), '\nans: ', str(ans) ] ) )
print( '-------------------------------------------------')
