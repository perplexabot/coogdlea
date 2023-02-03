function shiftGrid(grid::Any, k::Int64)::Any
    if typeof(grid) == Vector{Int64} && length(grid) == 1
        return grid
    end

    global b = grid
    for i in range(1,k, step=1)
        global b
        b = circshift(b, (0,1))
        b[:,1] = circshift(b[:,1], 1)
    end
    return b
end


cases = [
    ([1 2 3; 4 5 6; 7 8 9], 1, [9 1 2; 3 4 5; 6 7 8]),
    (
        [3 8 1 9; 19 7 2 5; 4 6 11 10; 12 0 21 13],
        4,
        [12 0 21 13; 3 8 1 9; 19 7 2 5 ;4 6 11 10],
    ),
    (transpose([1 2 3]), 1, transpose([3  1 2])),
    ([1 2 3], 1, [3 1 2]),
    ([1], 100, [1]),
]

for (grid, k, exp) in cases
    got = shiftGrid(grid, k)
    @assert got == exp "Failed case ($(grid) $(k))"
end
