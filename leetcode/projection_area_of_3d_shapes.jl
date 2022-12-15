function projectionArea(grid)
    if isempty(grid)
        return 0
    end

    return count(i->i!=0, grid) +
        sum(findmax(grid,dims=1)[1]) +
        sum(findmax(transpose(grid),dims=1)[1])
end


cases = [
    ([1 2; 3 4], 17),
    ([2], 5),
    ([1 0;0 2], 8),
    ([0 0;0 0], 0),
    ([], 0),
    ([0], 0),
    ([1], 3),
]

for (grid, exp) in cases
    ans = projectionArea(grid)
    @assert ans == exp "Failed ($(grid)) - got ($(ans)), expecting ($(exp))"
end
