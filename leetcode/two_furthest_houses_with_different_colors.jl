function maxDistance(colors::Vector{Int64})::Int64
    distance = length(colors)
    while ! iszero(distance)
        s = 1
        e = s + distance
        while e <= length(colors)
            if colors[e] != colors[s]
                return distance
            end
            s += 1
            e += 1
        end
        distance -= 1
    end
    return 0
end

cases = [([1, 1, 1, 6, 1, 1, 1], 3), ([1, 8, 3, 8, 3], 4), ([0, 1], 1), ([1, 1], 0)]

for (colors, exp) in cases
    got = maxDistance(colors)
    @assert got == exp "Failed case ($(colors)) - expecting ($(exp)), got ($(got))."
end
