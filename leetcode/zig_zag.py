# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of
# rows like this: (you may want to display this pattern in a fixed font for better
# legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   numRows
#
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number
# of rows:
#
#     string convert(string text, int nRows);
#     convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

def zigZagConv(s, numRows):
    #list of cols class
    class colClass:
        def __init__(self, cnt):
            self.cols = [[] for _ in range(cnt)]

        def isEmpty(self):
            for i in self.cols:
                if i:
                    return False
            return True

    if numRows >= len(s) or numRows < 2 or not s:
        return s
    else:
        i = 0
        index = 0
        columns = colClass( len(s)//numRows + 1)
        dots = colClass( len(s)//numRows + 1)
        while i < len(s):
            j = 0
            while j < numRows and i+j < len(s):
                columns.cols[index].append(s[i+j])
                j += 1
            i += numRows

            j = 0
            while j < numRows-2 and i+j < len(s):
                dots.cols[index].append(s[i+j])
                j += 1

            while len(dots.cols[index]) != numRows - 2:
                dots.cols[index].append(None)

            i += numRows-2
            index += 1

        convertedString = []
        line = 0
        while not columns.isEmpty():
            #loop through non empty columns (using class iterator)
            for ccol, dcol in zip(columns.cols, dots.cols):
                if ccol:
                    convertedString.append(ccol.pop(0))
                if line not in [0,numRows-1] and dcol:
                    t = dcol.pop()
                    if t:
                        convertedString.append(t)
            line += 1

        if not dots.isEmpty():
            for d in dots:
                convertedString.extend(d)

        return ''.join(convertedString)

s = "PAYPALISHIRING"
print(''.join(["Str: ", s]))
ans = zigZagConv(s,3)
print(''.join(["Ans: ", ans]))

s = "HEREISANOTHERATTEMPTATIT"
print(''.join(["Str: ", s]))
ans = zigZagConv(s,4)
print(''.join(["Ans: ", ans]))

s = "ABC"
print(''.join(["Str: ", s]))
ans = zigZagConv(s,2)
print(''.join(["Ans: ", ans]))

s = ""
print(''.join(["Str: ", s]))
ans = zigZagConv(s,1)
print(''.join(["Ans: ", ans]))

s = "ABCDE"
print(''.join(["Str: ", s]))
ans = zigZagConv(s,4)
print(''.join(["Ans: ", ans]))
