# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.
# 
# An input string is valid if:
# 
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Note that an empty string is also considered valid.

def validParan(s):
    from collections import Counter

    opening = set( [ '[', '{', '(' ] )
    pairs = { ']':'[', ')':'(', '}':'{', '[':']', '(':')', '{':'}', '-1':'-1' }

    balance = Counter()
    lastOpen = ['-1']
    for sym in s:
        if sym in opening:
            lastOpen.append(sym)
            balance[sym] += 1
        else:
            lastO = lastOpen.pop()
            if sym != pairs[lastO]:
                return False
            balance[sym] -= 1
    return True if not sum( balance.values() ) else False



s = "({)})}))})((}][]"
ans = validParan(s)
print( ''.join( [ 's: ', s, '\nans: ', str(ans) ] ) )
print( '---------------------------------' )
s = "((())[]{[()()()]})"
ans = validParan(s)
print( ''.join( [ 's: ', s, '\nans: ', str(ans) ] ) )
print( '---------------------------------' )
s = "([)]"
ans = validParan(s)
print( ''.join( [ 's: ', s, '\nans: ', str(ans) ] ) )
print( '---------------------------------' )
s = "((((((("
ans = validParan(s)
print( ''.join( [ 's: ', s, '\nans: ', str(ans) ] ) )
print( '---------------------------------' )
s = "))))"
ans = validParan(s)
print( ''.join( [ 's: ', s, '\nans: ', str(ans) ] ) )
print( '---------------------------------' )
s = ""
ans = validParan(s)
print( ''.join( [ 's: ', s, '\nans: ', str(ans) ] ) )
print( '---------------------------------' )
s = "(()))"
ans = validParan(s)
print( ''.join( [ 's: ', s, '\nans: ', str(ans) ] ) )
print( '---------------------------------' )
s = "(())"
ans = validParan(s)
print( ''.join( [ 's: ', s, '\nans: ', str(ans) ] ) )
print( '---------------------------------' )
s = "()"
ans = validParan(s)
print( ''.join( [ 's: ', s, '\nans: ', str(ans) ] ) )
print( '---------------------------------' )
s = "[][]()(){}{}"
ans = validParan(s)
print( ''.join( [ 's: ', s, '\nans: ', str(ans) ] ) )
print( '---------------------------------' )
s = "((((((((()))"
ans = validParan(s)
print( ''.join( [ 's: ', s, '\nans: ', str(ans) ] ) )
print( '---------------------------------' )
s = ")("
ans = validParan(s)
print( ''.join( [ 's: ', s, '\nans: ', str(ans) ] ) )
print( '---------------------------------' )
s = "([[]])"
ans = validParan(s)
print( ''.join( [ 's: ', s, '\nans: ', str(ans) ] ) )
print( '---------------------------------' )
