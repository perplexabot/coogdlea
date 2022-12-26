function numOfStrings(patterns, word)
    if isempty(patterns) || isempty(word)
        return 0
    end

    return sum([1 for pattern in patterns if occursin(pattern, word)])
end

cases = [
    (["a", "abc", "bc", "d"], "abc", 3),
    (["a", "b", "c"], "aaaaabbbbb", 2),
    (["a", "a", "a"], "ab", 3),
    ([], "word", 0),
    (["a", "b"], "", 0),
    (["abc"], "acbccc", 0),
    (["a"], "b", 0),
    (["a"], "a", 1),
    (["ca"], "ac", 0),
    (["ab"], "ab", 1),
]

for (patterns, word, exp) in cases
    got = numOfStrings(patterns, word)
    @assert got == exp "Failed case ($(patterns), $(word)) - expecting($(exp)), got ($(got))."
end
