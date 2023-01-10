function prefixCount(words::Vector{String}, pref::String)::Int64
    return sum(1 for word in words if startswith(word, pref); init=0)
end

cases = [
    (["leetcode", "win", "loops", "success"], "code", 0),
    (["pay", "attention", "practice", "attend"], "at", 2),
    (["h"], "h", 1),
    (["ah"], "a", 1),
    (["ah"], "h", 0),
]

for (words, prefix, exp) in cases
    got = prefixCount(words, prefix)
    @assert got == exp "Failed case ($(words), $(prefix)) - expecting ($(exp)), got ($(got))."
end
