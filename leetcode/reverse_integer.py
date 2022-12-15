def reverse(x):
    y = list( str(x)[1:] if str(x)[0] in ['+', '-'] else str(x) )
    y.reverse()
    if str(x)[0] in ['+', '-']:
        y = [ str(x)[0] ] + y
    y = int(''.join( y ))
    return y if y >= -2**31 and y <= 2**31 -1 else 0

x = 1234
print("init: " + str(x) )
ans = reverse(x)
print("ans: " + str(ans) )
