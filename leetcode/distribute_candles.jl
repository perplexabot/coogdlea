function distributeCandies(candyType)
    if isempty(candyType)
        return 0
    end

    half = length(candyType) / 2
    uniques = length(Set(candyType))

    if uniques >= half
        return half
    else
        return uniques
    end
end

cases = [
    ([1, 1, 2, 2, 3, 3], 3),
    ([1, 1, 2, 3], 2),
    ([6, 6, 6, 6], 1),
    ([], 0),
    ([1, 2, 3, 4], 2),
    ([1, 2], 1),
    ([1, 1], 1),
]

for (candyType, exp) in cases
    got = distributeCandies(candyType)
    @assert got == exp "Failed case ($(candyType)) - expecting ($(exp)), got ($(got))"
end
