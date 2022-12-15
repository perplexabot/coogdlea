def safe_pawns(pawns):
    safePos = set()
    for pos in pawns:
        safePos.add( ''.join( [ chr( ord(pos[0]) - 1 ), chr( ord(pos[1]) + 1 ) ] ) )
        safePos.add( ''.join( [ chr( ord(pos[0]) + 1 ), chr( ord(pos[1]) + 1 ) ] ) )
    return sum( pawn in safePos for pawn in pawns ) 

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
