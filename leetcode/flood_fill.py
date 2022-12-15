"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value
    of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image
    starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to
    the starting pixel of the same color as the starting pixel, plus any pixels connected
    4-directionally to those pixels (also with the same color), and so on. Replace the color of
    all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

Example 1:
    Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
    Output: [[2,2,2],[2,2,0],[2,0,1]]
    Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel),
        all pixels connected by a path of the same color as the starting pixel (i.e., the blue
        pixels) are colored with the new color.
    Note the bottom corner is not colored 2, because it is not 4-directionally connected to
        the starting pixel.

Example 2:
    Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
    Output: [[0,0,0],[0,0,0]]
    Explanation: The starting pixel is already colored 0, so no changes are made to the image.

Constraints:
    m == image.length
    n == image[i].length
    1 <= m, n <= 50
    0 <= image[i][j], color < 216
    0 <= sr < m
    0 <= sc < n

A:
    sr,sc not in grid -> not possible
    grid is empty -> return empty
    grid with one element -> return colored element
    n != m
    m x 1 and 1 x n images?
D:
    [1 1 1] sc=1, sr=1, color=2
    [1 1 0]
    [1 0 1]

    set (sr,sc) to 2
    (1,1) neighbors:
        - left:     (sc-1,sr) if sc-1 >= 0
        - right:    (sc+1,sr) if sc+1 < n
        - up:       (sc,sr-1) if sr-1 >= 0
        - down:     (sc,sr+1) if sr+1 < m

P:
    Q = queue((sr,sc))
    while Q:
        curr = Q.pop(0)
        curr.color = 2
        for neighbor in curr.neighbors:
            Q.append(neighbor) if neighbor.color != color

    return image
"""


def floodFill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    from collections import deque

    m = len(image)
    n = len(image[0])
    start = (sr, sc)
    match_color = image[sr][sc]
    Q = deque([start])
    while Q:
        curr_row, curr_col = Q.popleft()
        image[curr_row][curr_col] = color

        potential_neighbors = [
            (curr_row - 1, curr_col),
            (curr_row + 1, curr_col),
            (curr_row, curr_col - 1),
            (curr_row, curr_col + 1),
        ]
        actual_neighbors = [
            neighbor
            for neighbor in potential_neighbors
            if 0 <= neighbor[0] < m and 0 <= neighbor[1] < n
        ]

        for (neighbor_row, neighbor_col) in actual_neighbors:
            if (
                image[neighbor_row][neighbor_col] != color
                and image[neighbor_row][neighbor_col] == match_color
            ):
                Q.append((neighbor_row, neighbor_col))

    return image


cases = [
    ([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2, [[2, 2, 2], [2, 2, 0], [2, 0, 1]]),
    ([[0, 0, 0], [0, 0, 0]], 0, 0, 0, [[0, 0, 0], [0, 0, 0]]),
    ([[1]], 0, 0, 100, [[100]]),
    ([[1, 1, 1]], 0, 1, 100, [[100, 100, 100]]),
    ([[1, 1, 1]], 0, 0, 100, [[100, 100, 100]]),
    ([[1], [1], [1]], 0, 0, 100, [[100], [100], [100]]),
]

for (image, sr, sc, color, exp) in cases:
    assert (
        got := floodFill(image, sr, sc, color)
    ) == exp, f"Failed with ({image}, {sr}, {sc}, {color}) - expecting ({exp}), got ({got})"
