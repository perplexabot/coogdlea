function areOccurrencesEqual(s)
    if isempty(s)
        return true
    end

    counts = Dict(char => count(i->i==char, s) for char in s)
    return length(Set(values(counts))) == 1
end

cases = [
    ("abacbc", true),
    ("aaabb", false),
    ("", true),
    ("a", true),
    ("aa", true),
    ("ab", true),
    ("abb", false),
]

for (s, exp) in cases
    ans = areOccurrencesEqual(s)
    @assert ans == exp "Failed with $(s) - got $(ans), expecting $(exp)"
end
