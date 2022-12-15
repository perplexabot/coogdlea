# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity 
# should be O(log (m+n)).
# 
# Example 1:
#     nums1 = [1, 3]
#     nums2 = [2]
#     The median is 2.0
#
# Example 2:
#     nums1 = [1, 2]
#     nums2 = [3, 4]
#     The median is (2 + 3)/2 = 2.5

def findMedianSortedArrays(nums1, nums2):
    l1 = len(nums1)
    l2 = len(nums2)
    t = l1 + l2
    p = t//2 if t%2 else t//2 - 1
    n = []
    i1 = 0
    i2 = 0

    while len(n) < p + 2:
        if i1 >= l1 and i2 >= l2:
            break
        if i1 < l1 and i2 < l2:
            if nums1[i1] < nums2[i2]:
                n.append( nums1[i1] )
                i1 += 1
            else:
                n.append( nums2[i2] )
                i2 += 1
        elif i1 < l1:
            n.append( nums1[i1] )
            i1 += 1
        else: # i2 < l2
            n.append( nums2[i2] )
            i2 += 1
    
    if len(n) == 1:
        return n[0]

    return n[-2] if t%2 else (n[-1] + n[-2])/float(2)

a = [1,3]
b = [2]
print( ''.join( ['A: ', str(a), ' B: ', str(b)] ) )
ans = findMedianSortedArrays(a,b)
print( ''.join( ['ans: ', str(ans)] ) )
print( '-------------------------------------------------' )

a = [1,2]
b = [3,4]
print( ''.join( ['A: ', str(a), ' B: ', str(b)] ) )
ans = findMedianSortedArrays(a,b)
print( ''.join( ['ans: ', str(ans)] ) )
print( '-------------------------------------------------' )

a = [1]
b = [1]
print( ''.join( ['A: ', str(a), ' B: ', str(b)] ) )
ans = findMedianSortedArrays(a,b)
print( ''.join( ['ans: ', str(ans)] ) )
print( '-------------------------------------------------' )

a = []
b = [1]
print( ''.join( ['A: ', str(a), ' B: ', str(b)] ) )
ans = findMedianSortedArrays(a,b)
print( ''.join( ['ans: ', str(ans)] ) )
print( '-------------------------------------------------' )

a = [1]
b = []
print( ''.join( ['a: ', str(a), ' b: ', str(b)] ) )
ans = findMedianSortedArrays(a,b)
print( ''.join( ['ans: ', str(ans)] ) )
print( '-------------------------------------------------' )

a = [1,2]
b = []
print( ''.join( ['a: ', str(a), ' b: ', str(b)] ) )
ans = findMedianSortedArrays(a,b)
print( ''.join( ['ans: ', str(ans)] ) )
print( '-------------------------------------------------' )

a = [1,3,4]
b = [5,23,6]
print( ''.join( ['A: ', str(a), ' B: ', str(b)] ) )
ans = findMedianSortedArrays(a,b)
print( ''.join( ['ans: ', str(ans)] ) )
print( '-------------------------------------------------' )

# assuming all input lists are valid (non empty and only ints)
#a = []
#b = []
#print( ''.join( ['A: ', str(a), ' B: ', str(b)] ) )
#ans = findMedianSortedArrays(a,b)
#print( ''.join( ['ans: ', str(ans)] ) )
#print( '-------------------------------------------------' )
