def mostWantedLetter(text: str) -> str:
    from collections import Counter
    d = Counter(text.lower().strip())
    
    myMax = float('-inf')
    for k in d:
        if ord(k) <= ord('z') and ord(k) >= ord('a'):
            if d[k] > d[myMax]:
                myMax = k
            elif d[k] == d[myMax]:
                if k < myMax:
                    myMax = k
        
    return myMax

a = 'hereweGOOOOO'
print("using: " + a)
ans = mostWantedLetter(a)
print("ans: " + ans)

a = '1234,1234,1234 S 1234,1234,'
print("using: " + a)
ans = mostWantedLetter(a)
print("ans: " + ans)
