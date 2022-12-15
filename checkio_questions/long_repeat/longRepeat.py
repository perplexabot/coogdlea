def long_repeat(line: str) -> int:
    maxStreak = 1
    currStreak = 1
    for i in range(1,len(line)):
        if line[i-1] == line[i]:
            currStreak += 1
        else:
            if currStreak > maxStreak:
                maxStreak = currStreak
            currStreak = 1

    if currStreak > maxStreak:
        maxStreak = currStreak

    return maxStreak if line else 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    assert long_repeat('aa') == 2, "2fer"
    print('"Run" is good. How is "Check"?')
