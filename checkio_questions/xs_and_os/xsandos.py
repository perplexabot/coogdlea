def xsandos(game_result: list) -> str:
    diagonal = ''.join( [ game_result[i][i] for i in range(3) ] )
    antidiagonal = ''.join( [ game_result[i][2 - i] for i in range(3) ] )
    transposed = list( map( ''.join, zip(*game_result) ) )
    def checkSym(s):
        t = [True if x.lower().count(s.lower()) == 3 else False for x in game_result + transposed + [diagonal] + [antidiagonal] ]
        if any(t):
            return s.upper()
        else:
            return ''
    res = ''.join( [checkSym('o'), checkSym('x')] )
    return res if not res in ['','ox'] else 'D'

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert xsandos([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert xsandos([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert xsandos([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert xsandos([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


