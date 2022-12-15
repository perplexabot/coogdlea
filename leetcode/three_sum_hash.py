def threeSum(nums):
    from itertools import combinations
    from collections import Counter

    l3 = []
    nCount = Counter(nums)
    numSet = set(nums)
    #l3Set = set()
    for pair in combinations(nums, 2):
        a = sum(pair)
        nCount[pair[0]] -= 1
        nCount[pair[1]] -= 1

        if -a in numSet:
            if nCount[-a] > 0:
                #l3Set.add( tuple( sorted( [-a,*pair] ) ) )
                l3.append([-a,*pair])

        nCount[pair[0]] += 1
        nCount[pair[1]] += 1

#    l3 = list(l3Set)
#    l3 = [list(x) for x in l3]

    sl3 = [ tuple( sorted(x) ) for x in l3 ]
    l3Set = set(sl3)
    l3 = list(l3Set)
    l3 = [list(x) for x in l3]

    return l3
