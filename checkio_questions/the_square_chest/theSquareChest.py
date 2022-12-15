# On the chest keypad is a grid of numbered dots. The grid is comprised 
# of a square shaped array of dots and contains lines that connect some 
# pairs of adjacent dots. The answer to the code is the number of squares 
# that are formed by these lines. For example, in the figure shown below, 
# there are 3 squares: 2 small squares and 1 medium square.
def theSquareChest(list_of_lines):
    smalls = set()
    mediums = set()
    bigs = set()
    listSet = set( [ frozenset(x) for x in list_of_lines ] )

    #create small squres
    for i in range(1,12):
        if not i%4:
            continue
        smalls.add( frozenset( [ frozenset( [i, i+1] ),              #top
                                 frozenset( [4+i, 4+i+1] ),          #bottom
                                 frozenset( [i, i+4] ),              #left 
                                 frozenset( [i+1, i+5] ) ] ) )       #right

    #create medium squres
    i = 1
    while i < 7:
        mediums.add( frozenset( [ frozenset( [i,i+1]), frozenset( [i+1,i+2] ),                         #top
                                  frozenset( [i,i+4]), frozenset( [i+4,i+8] ),                         #left
                                  frozenset( [i+2,i+2+4]), frozenset( [i+2+4,i+2+4+4] ),               #right
                                  frozenset( [i+4+4,i+4+4+1]), frozenset( [i+4+4+1,i+4+4+2] ) ] ) )    #bottom 
        if not i%3:
            i += 2
        else:
            i += 1

    #create big square
    bigs.update( frozenset( [i,i+1] ) for i in range(1,4) )      #top
    bigs.update( frozenset( [i,i+4] ) for i in range(1,13,4) )   #left
    bigs.update( frozenset( [i,i+1] ) for i in range(13,16) )    #bottom
    bigs.update( frozenset( [i,i+4] ) for i in range(4,16,4) )   #right

    sm = sum( len( listSet.intersection(x) ) == len(x) for x in smalls )
    md = sum( len( listSet.intersection(x) ) == len(x) for x in mediums )
    bg = 1 if len( listSet.intersection(bigs) ) == len(bigs) else 0 

    return sm + md + bg

if __name__ == '__main__':
    assert (theSquareChest([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                     [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    assert (theSquareChest([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    assert (theSquareChest([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    assert (theSquareChest([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    assert (theSquareChest([[16, 15], [16, 12], [15, 11], [11, 10],
                     [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"
