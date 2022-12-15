function floodFill(image, sr, sc, color)
    # keep inputs the same to match python inputs but mod them here to account for lists starting with 1 (vs 0) in julia
    sr = sr+1
    sc = sc+1
    m = length(image)
    n = length(image[1])
    start = (sr,sc)
    match_color = image[sr][sc]
    Q = [start]

    while ! isempty(Q)
        curr_row, curr_col = popfirst!(Q)
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
            if 1 <= neighbor[1] <= m && 1 <= neighbor[2] <= n 
        ]

        for (neighbor_row, neighbor_col) in actual_neighbors
            neighbor_color = image[neighbor_row][neighbor_col]
            if  neighbor_color != color && neighbor_color == match_color
                append!(Q, [(neighbor_row, neighbor_col)])
            end
        end
    end

    return image
end


cases = [
    ([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2, [[2, 2, 2], [2, 2, 0], [2, 0, 1]]),
    ([[0, 0, 0], [0, 0, 0]], 0, 0, 0, [[0, 0, 0], [0, 0, 0]]),
    ([[1]], 0, 0, 100, [[100]]),
    ([[1, 1, 1]], 0, 1, 100, [[100, 100, 100]]),
    ([[1, 1, 1]], 0, 0, 100, [[100, 100, 100]]),
    ([[1], [1], [1]], 0, 0, 100, [[100], [100], [100]]),
]

for (image, sr, sc, color, exp) in cases
    got = floodFill(image, sr, sc, color)
    @assert got == exp "Failed with ($(image), $(sr), $(sc), $(color)) - expecting ($(exp)), got ($(got))"
end
