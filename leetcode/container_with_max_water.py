# Given n non-negative integers a1, a2, ..., an, where each represents a point at 
# coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line 
# i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a 
# container, such that the container contains the most water.
# 
# Note: You may not slant the container and n is at least 2.

def maxArea(heights):
    if len(heights) < 2:
        return 0
    else:
        l = 0
        r = len(heights) - 1

        area = 0
        while l < r:
            area = max(area, (r - l)*min(heights[l], heights[r]) ) 
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return area

from random import randint

aLen = 10

for i in range(10):
    h = [randint(1,100) for _ in range(aLen)]
    ans = maxArea(h)
    print(''.join(['h: ', str(h), '\na: ', str(ans)]))

h = [randint(1,100) for _ in range(2)]
ans = maxArea(h)
print(''.join(['h: ', str(h), '\na: ', str(ans)]))

h = [randint(1,100) for _ in range(1)]
ans = maxArea(h)
print(''.join(['h: ', str(h), '\na: ', str(ans)]))

h = [randint(1,100) for _ in range(0)]
ans = maxArea(h)
print(''.join(['h: ', str(h), '\na: ', str(ans)]))

h = [randint(1,100) for _ in range(100)]
ans = maxArea(h)
print(''.join(['h: ', str(h), '\na: ', str(ans)]))
