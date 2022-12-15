"""Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
"""

# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b


class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    def maxPoints(self, points: 'List[Point]') -> int:
        from collections import defaultdict, Counter
        from decimal import Decimal

        if len(points) == 1:
            return 1
        if not points:
            return 0

        pts = [(p.x, p.y) for p in points]
        cts = Counter(pts)
        pts = list(set(pts))
        if len(pts) == 1:
            return list(cts.values())[0]

        common = defaultdict(set)
        for i in range(len(pts) - 1):
            for j in range(i + 1, len(pts)):
                x1, y1 = pts[i][0], pts[i][1]
                x2, y2 = pts[j][0], pts[j][1]
                m = Decimal(y1 - y2) / Decimal(x1 - x2) if x1 != x2 else 'undef'
                yinter = y1 - (m * x1) if x1 != x2 else 'undef'
                if not m:
                    xinter = 'undef'
                else:
                    xinter = -yinter / m if x1 != x2 else x1
                pt1, pt2 = (pts[i][0], pts[i][1]), (pts[j][0], pts[j][1])
                common[(m, yinter, xinter)].update([pt1, pt2])

        bucket_sizes = []
        for k in common:
            c = 0
            for pt in common[k]:
                c += cts[pt]
            bucket_sizes.append(c)

        return max(bucket_sizes)


inps = [
    ([Point(0, 0), Point(94_911_151, 94_911_150), Point(94_911_152, 94_911_151)], 2),
    ([Point(1, 1), Point(1, 1), Point(1, 1), Point(2, 2), Point(3, 4), Point(3, 4)], 5),
    ([Point(1, 1), Point(2, 2), Point(3, 3)], 3),
    ([Point(1, 1), Point(3, 2), Point(5, 3), Point(4, 1), Point(2, 3), Point(1, 4)], 4),
    ([Point(1, 1)], 1),
    ([], 0),
    ([Point(0, 0), Point(0, 0)], 2),
    (
        [
            Point(0, -12),
            Point(5, 2),
            Point(2, 5),
            Point(0, -5),
            Point(1, 5),
            Point(2, -2),
            Point(5, -4),
            Point(3, 4),
            Point(-2, 4),
            Point(-1, 4),
            Point(0, -5),
            Point(0, -8),
            Point(-2, -1),
            Point(0, -11),
            Point(0, -9),
        ],
        6,
    ),
    (
        [
            Point(40, -23),
            Point(9, 138),
            Point(429, 115),
            Point(50, -17),
            Point(-3, 80),
            Point(-10, 33),
            Point(5, -21),
            Point(-3, 80),
            Point(-6, -65),
            Point(-18, 26),
            Point(-6, -65),
            Point(5, 72),
            Point(0, 77),
            Point(-9, 86),
            Point(10, -2),
            Point(-8, 85),
            Point(21, 130),
            Point(18, -6),
            Point(-18, 26),
            Point(-1, -15),
            Point(10, -2),
            Point(8, 69),
            Point(-4, 63),
            Point(0, 3),
            Point(-4, 40),
            Point(-7, 84),
            Point(-8, 7),
            Point(30, 154),
            Point(16, -5),
            Point(6, 90),
            Point(18, -6),
            Point(5, 77),
            Point(-4, 77),
            Point(7, -13),
            Point(-1, -45),
            Point(16, -5),
            Point(-9, 86),
            Point(-16, 11),
            Point(-7, 84),
            Point(1, 76),
            Point(3, 77),
            Point(10, 67),
            Point(1, -37),
            Point(-10, -81),
            Point(4, -11),
            Point(-20, 13),
            Point(-10, 77),
            Point(6, -17),
            Point(-27, 2),
            Point(-10, -81),
            Point(10, -1),
            Point(-9, 1),
            Point(-8, 43),
            Point(2, 2),
            Point(2, -21),
            Point(3, 82),
            Point(8, -1),
            Point(10, -1),
            Point(-9, 1),
            Point(-12, 42),
            Point(16, -5),
            Point(-5, -61),
            Point(20, -7),
            Point(9, -35),
            Point(10, 6),
            Point(12, 106),
            Point(5, -21),
            Point(-5, 82),
            Point(6, 71),
            Point(-15, 34),
            Point(-10, 87),
            Point(-14, -12),
            Point(12, 106),
            Point(-5, 82),
            Point(-46, -45),
            Point(-4, 63),
            Point(16, -5),
            Point(4, 1),
            Point(-3, -53),
            Point(0, -17),
            Point(9, 98),
            Point(-18, 26),
            Point(-9, 86),
            Point(2, 77),
            Point(-2, -49),
            Point(1, 76),
            Point(-3, -38),
            Point(-8, 7),
            Point(-17, -37),
            Point(5, 72),
            Point(10, -37),
            Point(-4, -57),
            Point(-3, -53),
            Point(3, 74),
            Point(-3, -11),
            Point(-8, 7),
            Point(1, 88),
            Point(-12, 42),
            Point(1, -37),
            Point(2, 77),
            Point(-6, 77),
            Point(5, 72),
            Point(-4, -57),
            Point(-18, -33),
            Point(-12, 42),
            Point(-9, 86),
            Point(2, 77),
            Point(-8, 77),
            Point(-3, 77),
            Point(9, -42),
            Point(16, 41),
            Point(-29, -37),
            Point(0, -41),
            Point(-21, 18),
            Point(-27, -34),
            Point(0, 77),
            Point(3, 74),
            Point(-7, -69),
            Point(-21, 18),
            Point(27, 146),
            Point(-20, 13),
            Point(21, 130),
            Point(-6, -65),
            Point(14, -4),
            Point(0, 3),
            Point(9, -5),
            Point(6, -29),
            Point(-2, 73),
            Point(-1, -15),
            Point(1, 76),
            Point(-4, 77),
            Point(6, -29),
        ],
        25,
    ),
    (
        [
            Point(560, 248),
            Point(0, 16),
            Point(30, 250),
            Point(950, 187),
            Point(630, 277),
            Point(950, 187),
            Point(-212, -268),
            Point(-287, -222),
            Point(53, 37),
            Point(-280, -100),
            Point(-1, -14),
            Point(-5, 4),
            Point(-35, -387),
            Point(-95, 11),
            Point(-70, -13),
            Point(-700, -274),
            Point(-95, 11),
            Point(-2, -33),
            Point(3, 62),
            Point(-4, -47),
            Point(106, 98),
            Point(-7, -65),
            Point(-8, -71),
            Point(-8, -147),
            Point(5, 5),
            Point(-5, -90),
            Point(-420, -158),
            Point(-420, -158),
            Point(-350, -129),
            Point(-475, -53),
            Point(-4, -47),
            Point(-380, -37),
            Point(0, -24),
            Point(35, 299),
            Point(-8, -71),
            Point(-2, -6),
            Point(8, 25),
            Point(6, 13),
            Point(-106, -146),
            Point(53, 37),
            Point(-7, -128),
            Point(-5, -1),
            Point(-318, -390),
            Point(-15, -191),
            Point(-665, -85),
            Point(318, 342),
            Point(7, 138),
            Point(-570, -69),
            Point(-9, -4),
            Point(0, -9),
            Point(1, -7),
            Point(-51, 23),
            Point(4, 1),
            Point(-7, 5),
            Point(-280, -100),
            Point(700, 306),
            Point(0, -23),
            Point(-7, -4),
            Point(-246, -184),
            Point(350, 161),
            Point(-424, -512),
            Point(35, 299),
            Point(0, -24),
            Point(-140, -42),
            Point(-760, -101),
            Point(-9, -9),
            Point(140, 74),
            Point(-285, -21),
            Point(-350, -129),
            Point(-6, 9),
            Point(-630, -245),
            Point(700, 306),
            Point(1, -17),
            Point(0, 16),
            Point(-70, -13),
            Point(1, 24),
            Point(-328, -260),
            Point(-34, 26),
            Point(7, -5),
            Point(-371, -451),
            Point(-570, -69),
            Point(0, 27),
            Point(-7, -65),
            Point(-9, -166),
            Point(-475, -53),
            Point(-68, 20),
            Point(210, 103),
            Point(700, 306),
            Point(7, -6),
            Point(-3, -52),
            Point(-106, -146),
            Point(560, 248),
            Point(10, 6),
            Point(6, 119),
            Point(0, 2),
            Point(-41, 6),
            Point(7, 19),
            Point(30, 250),
        ],
        22,
    ),
]

sol = Solution()
for ind, (pts, exp) in enumerate(inps):
    print(f"Running test {ind} and asserting...")
    ans = sol.maxPoints(pts)
    assert ans == exp, f"got: {ans}, expected: {exp}"
