# Given an integer, convert it to a roman numeral.
# Input is guaranteed to be within the range from 1 to 3999.

def integerToRoman(num):
    t = num 
    pos = 0
    #           ones        tens       hundreds  thous
    romans = [['I', 'V'], ['X', 'L'], ['C','D'], ['M']]
    romanForm = []
    while pos < len(str(num)):
        digi = t%10
        t //= 10

        if digi == 4:
            romanForm.append( romans[pos][1] )
            romanForm.append( romans[pos][0] )
        elif digi == 9:
            romanForm.append( romans[pos+1][0] )
            romanForm.append( romans[pos][0] )
        elif digi >= 5:
            for i in range(digi-5):
                romanForm.append(romans[pos][0])
            romanForm.append(romans[pos][1])
        else: # digi < 4
            for i in range(digi):
                romanForm.append(romans[pos][0])
        pos += 1
    return ''.join(romanForm[::-1])

for i in range(35):
    print(''.join(["West: ", str(i), " | Roman: ", integerToRoman(i)]))

i = 3999
print(''.join(["West: ", str(i), " | Roman: ", integerToRoman(i)]))
