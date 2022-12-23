function kidsWithCandies(candies, extraCandies)
    if isempty(candies)
        return []
    end

    m = maximum(candies)
    if iszero(extraCandies)
        return [x >= m for x in candies]
    end
    return [m - ccnt <= extraCandies for ccnt in candies]
end

cases = [
    ([2, 3, 5, 1, 3], 3, [true, true, true, false, true]),
    ([4, 2, 1, 1, 2], 1, [true, false, false, false, false]),
    ([12, 1, 12], 10, [true, false, true]),
    ([], 10, []),
    ([1, 2], 0, [false, true]),
    ([2, 2], 0, [true, true]),
    ([1], 0, [true]),
    ([1], 10, [true]),
]

for (candies, extraCandies, exp) in cases
    got = kidsWithCandies(candies, extraCandies)
    @assert got == exp "Failed case ($(candies), $(extraCandies)) - expecting ($(exp)), got ($(got))"
end
