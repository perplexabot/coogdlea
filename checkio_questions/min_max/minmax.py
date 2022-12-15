def mymin(*args, **kwargs):
    key = kwargs.get("key", None)
    lst = list(args[0]) if len(args) == 1 else args
    myMin = lst[0]

    if key:
        for i in lst:
            if key(i) < key(myMin):
                myMin = i
    else:
        for i in lst:
            if i < myMin:
                myMin = i
    return myMin

def mymax(*args, **kwargs):
    key = kwargs.get("key", None)
    lst = list(args[0]) if len(args) == 1 else args
    myMax = lst[0]

    if key:
        for i in lst:
            if key(i) > key(myMax):
                myMax = i
    else:
        for i in lst:
            if i > myMax:
                myMax = i
    return myMax

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert mymax(3, 2) == 3, "Simple case max"
    assert mymin(3, 2) == 2, "Simple case min"
    assert mymax([1, 2, 0, 3, 4]) == 4, "From a list"
    assert mymin("hello") == "e", "From string"
    assert mymax(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert mymin([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
    mymin(abs(i) for i in range(-10, 10))
