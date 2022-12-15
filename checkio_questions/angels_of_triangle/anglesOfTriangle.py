def anglesOfTriangle(a,b,c):
    from math import acos, pi

    if a+b < c or b+c < a or c+a < b:
        return [0,0,0]

    cosA = (a**2 + b**2 - c**2 ) / (2*a*b)
    cosB = (b**2 + c**2 - a**2 ) / (2*b*c)
    cosC = (c**2 + a**2 - b**2 ) / (2*c*a)
    A = int( round(acos(cosA) * 180/pi) )
    B = int( round(acos(cosB) * 180/pi) )
    C = int( round(acos(cosC) * 180/pi) )
    
    return sorted([A, B, C])

if __name__ == '__main__':
    assert anglesOfTriangle(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert anglesOfTriangle(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert anglesOfTriangle(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"

