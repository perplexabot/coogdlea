def getLongestPal(s):
    def palRangeHelper(s, i, offset):
        j = 1
        while i-j+offset>-1 and i+j<len(s):
            if s[i-j+offset] != s[i+j]:
                return i-j+1+offset,i+j-1
            j += 1

        if i-j+offset<0 and i+j>=len(s):
            return i-j+1+offset, len(s)
        elif i-j+offset<0:
            return i-j+1+offset,i+j-1
        else:
            return i-j+offset,len(s)

    def getPalRange(s,i):
        if not i:
            return i, i+2
        else:
            if s[i-1] == s[i+1]:
                return palRangeHelper(s, i, 0)
            elif s[i] == s[i+1]:
                return palRangeHelper(s, i, 1)

    if not s:
        return None
    elif len(s) == 1:
        return s[0]
    elif len(s) == 2:
        return s if s[0] == s[1] else s[0]
    else:
        vInd = []
        for i in range(len(s) - 1):
            if not i:
                if s[i] == s[i+1]:
                    vInd.append(i)
            else:
                if s[i] == s[i+1] or s[i-1] == s[i+1]:
                    vInd.append(i)
        if not vInd:
            return s[0]
        else:
            En = float('-inf')
            St = 0
            for i in vInd:
                st,en = getPalRange(s,i)
                if en-st > En-St:
                    St = st
                    En = en
            return s[St:En]

s0 = 'a'
s1 = 'baa'
s2 = 'aab'
s3 = 'aba'
s4 = 'abacaba'
s5 = 'abacada'
s6 = 'caac'
s7 = 'abacaca'

print('s0: ', s0)
ans = getLongestPal(s0)
print('ans: ', ans)

print('s1: ', s1)
ans = getLongestPal(s1)
print('ans: ', ans)

print('s2: ', s2)
ans = getLongestPal(s2)
print('ans: ', ans)

print('s3: ', s3)
ans = getLongestPal(s3)
print('ans: ', ans)

print('s4: ', s4)
ans = getLongestPal(s4)
print('ans: ', ans)

print('s5: ', s5)
ans = getLongestPal(s5)
print('ans: ', ans)

print('s6: ', s6)
ans = getLongestPal(s6)
print('ans: ', ans)

print('s7: ', s7)
ans = getLongestPal(s7)
print('ans: ', ans)

