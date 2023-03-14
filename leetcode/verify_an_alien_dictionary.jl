function isAlienSorted(words::Vector{String}, order::String)::Bool
    weights = Dict(char => i for (i, char) in enumerate(order))
    if length(words) < 2
        return true
    end

    i = 2
    first = words[1]
    second = words[i]
    while true
        for j in range(1, length(first), step=1)
            if j > length(second)
                return false
            elseif weights[first[j]] > weights[second[j]]
                return false
            elseif weights[first[j]] < weights[second[j]]
                return true
            end
        end

        i += 1
        if i > length(words)
            return True
        end

        first = second
        second = words[i]
    end
end

cases = [
    (["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz", true),
    (["word", "world", "row"], "worldabcefghijkmnpqstuvxyz", false),
    (["apple", "app"], "abcdefghijklmnopqrstuvwxyz", false),
    (["kuvp", "q"], "ngxlkthsjuoqcpavbfdermiywz", true),
]

for (words, order, exp) in cases
    got = isAlienSorted(words, order)
    @assert got == exp "Failed case ($(words), $(order)), expecting ($(exp)), got ($(got))."
end
