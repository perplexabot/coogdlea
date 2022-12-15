# Implement atoi to convert a string to an integer.
# Hint: Carefully consider all possible input cases. If you want a challenge,
#  please do not see below and ask yourself what are the possible input cases.
# Notes: It is intended for this problem to be specified vaguely (ie, no
#  given input specs). You are responsible to gather all the input
#  requirements up front.

def atoi(s):
    def boundReturn(sign, myInt):
        if sign > 0 and myInt > 2147483647:
            return 2147483647
        elif sign < 0 and myInt > 2147483648:
            return -2147483648
        else:
            return sign * myInt

    smod = s.strip()
    if not smod:
        return 0
    else:
        if smod[0] == '-':
            sign = -1
            smod = smod[1:]
        else:
            if smod[0] == '+':
                smod = smod[1:]
            sign = 1

        if not smod:
            return 0

        myInt = 0
        for i in smod:
            a = ord(i) - ord('0')
            if  a >= 0 and a <= 9:
                myInt *= 10
                myInt += a
            else:
                return boundReturn(sign, myInt)
        return boundReturn(sign, myInt)

s = '-2147483649'
print(''.join(['s: ', str(s)]))
a = atoi(s)
print(''.join(['a: ', str(a)]))
print('--------------------------------------------')

s = '2147483648'
print(''.join(['s: ', str(s)]))
a = atoi(s)
print(''.join(['a: ', str(a)]))
print('--------------------------------------------')

s = '12345i23423'
print(''.join(['s: ', str(s)]))
a = atoi(s)
print(''.join(['a: ', str(a)]))
print('--------------------------------------------')

s = '12345 23423'
print(''.join(['s: ', str(s)]))
a = atoi(s)
print(''.join(['a: ', str(a)]))
print('--------------------------------------------')

s = '12345 -3 -322'
print(''.join(['s: ', str(s)]))
a = atoi(s)
print(''.join(['a: ', str(a)]))
print('--------------------------------------------')

s = '12345'
print(''.join(['s: ', str(s)]))
a = atoi(s)
print(''.join(['a: ', str(a)]))
print('--------------------------------------------')

s = '+12345'
print(''.join(['s: ', str(s)]))
a = atoi(s)
print(''.join(['a: ', str(a)]))
print('--------------------------------------------')

s = '+'
print(''.join(['s: ', str(s)]))
a = atoi(s)
print(''.join(['a: ', str(a)]))
print('--------------------------------------------')

s = '-'
print(''.join(['s: ', str(s)]))
a = atoi(s)
print(''.join(['a: ', str(a)]))
print('--------------------------------------------')

s = '-+'
print(''.join(['s: ', str(s)]))
a = atoi(s)
print(''.join(['a: ', str(a)]))
print('--------------------------------------------')

s = '00134123'
print(''.join(['s: ', str(s)]))
a = atoi(s)
print(''.join(['a: ', str(a)]))
print('--------------------------------------------')

s = '+00134123'
print(''.join(['s: ', str(s)]))
a = atoi(s)
print(''.join(['a: ', str(a)]))
print('--------------------------------------------')

s = '256'
print(''.join(['s: ', str(s)]))
a = atoi(s)
print(''.join(['a: ', str(a)]))
print('--------------------------------------------')

s = '7'
print(''.join(['s: ', str(s)]))
a = atoi(s)
print(''.join(['a: ', str(a)]))
print('--------------------------------------------')

s = '23498567234968727460'
print(''.join(['s: ', str(s)]))
a = atoi(s)
print(''.join(['a: ', str(a)]))
print('--------------------------------------------')

s = '-43'
print(''.join(['s: ', str(s)]))
a = atoi(s)
print(''.join(['a: ', str(a)]))
print('--------------------------------------------')

s = '0'
print(''.join(['s: ', str(s)]))
a = atoi(s)
print(''.join(['a: ', str(a)]))
print('--------------------------------------------')

s = '-132453453452'
print(''.join(['s: ', str(s)]))
a = atoi(s)
print(''.join(['a: ', str(a)]))
print('--------------------------------------------')

s = '-132453453i452'
print(''.join(['s: ', str(s)]))
a = atoi(s)
print(''.join(['a: ', str(a)]))
print('--------------------------------------------')

s = ''
print(''.join(['s: ', str(s)]))
a = atoi(s)
print(''.join(['a: ', str(a)]))
print('--------------------------------------------')

s = '7-321--1'
print(''.join(['s: ', str(s)]))
a = atoi(s)
print(''.join(['a: ', str(a)]))
print('--------------------------------------------')

s = '-!-'
print(''.join(['s: ', str(s)]))
a = atoi(s)
print(''.join(['a: ', str(a)]))
print('--------------------------------------------')
