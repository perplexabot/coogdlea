# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, two is written as II in Roman numeral, just two one's added together.
# Twelve is written as, XII, which is simply X + II. The number twenty seven is
# written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However,
# the numeral for four is not IIII. Instead, the number four is written as IV.
# Because the one is before the five we subtract it making four. The same principle
# applies to the number nine, which is written as IX. There are six instances where
# subtraction is used:
#
#     I can be placed before V (5) and X (10) to make 4 and 9.
#     X can be placed before L (50) and C (100) to make 40 and 90.
#     C can be placed before D (500) and M (1000) to make 400 and 900.
#     Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
#
#     Example 1:
#
#     Input: "III"
#     Output: 3
#     Example 2:
#
#     Input: "IV"
#     Output: 4
#     Example 3:
#
#     Input: "IX"
#     Output: 9
#     Example 4:
#
#     Input: "LVIII"
#     Output: 58
#     Explanation: C = 100, L = 50, XXX = 30 and III = 3.
#     Example 5:
#
#     Input: "MCMXCIV"
#     Output: 1994
#     Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    terms = [   {'i':1, 'ii':2, 'iii':3, 'iv':4, 'v':5, 'vi':6, 'vii':7, 'viii':8, 'ix':9  },
                {'x':10 , 'xx':20 , 'xxx':30 , 'xl':40 , 'l':50 , 'lx':60 , 'lxx':70 , 'lxxx':80 , 'xc':90 },
                {'c':100 , 'cc':200 , 'ccc':300 , 'cd':400 , 'd':500 , 'dc':600 , 'dcc':700 , 'dccc':800 , 'cm':900 },
                {'m':1000 , 'mm':2000 , 'mmm':3000 } ]
    ls = len(s)
    total = 0
    temp = s.lower()
    pos = 0
    while temp:
        lt = len(temp)
        if temp[-1] in terms[pos]:
            j = -1
            while temp[j:] in terms[pos] and j >= -lt:
                j -= 1
            total += terms[pos][ temp[j+1:] ]
            temp = temp[:j+1]
        elif lt > 1 and temp[-2:] in terms[pos]:
            total += terms[pos][ temp[-2:] ]
            temp = temp[:-2]
        pos += 1
    return total

a = 'III'
ans = romanToInt(a)
print( ''.join( ['a: ', a, '\nans: ', str(ans) ] ) )
print( '-------------------------------------' )

a = 'IV'
ans = romanToInt(a)
print( ''.join( ['a: ', a, '\nans: ', str(ans) ] ) )
print( '-------------------------------------' )

a = 'IX'
ans = romanToInt(a)
print( ''.join( ['a: ', a, '\nans: ', str(ans) ] ) )
print( '-------------------------------------' )

a = 'LVIII'
ans = romanToInt(a)
print( ''.join( ['a: ', a, '\nans: ', str(ans) ] ) )
print( '-------------------------------------' )

a = 'MCMXCIV'
ans = romanToInt(a)
print( ''.join( ['a: ', a, '\nans: ', str(ans) ] ) )
print( '-------------------------------------' )
