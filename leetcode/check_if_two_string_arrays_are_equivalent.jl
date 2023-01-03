function arrayStringsAreEqual(word1::Vector, word2::Vector)::Bool
    return join(word1) == join(word2)
end

cases = [
    (["ab", "c"], ["a", "bc"], true),
    (["a", "cb"], ["ab", "c"], false),
    (["abc", "d", "defg"], ["abcddefg"], true),
    (["a"], ["b"], false),
    (["a", "b"], ["ab"], true),
    ([], ["a"], false),
    (["a"], [], false),
    ([], [], true),
    (["a"], ["a"], true),
    (["ab"], ["ba"], false),
]

for (word1, word2, exp) in cases
    got = arrayStringsAreEqual(word1, word2)
    @assert got == exp "Failed case ($(word1), $(word2)) - expecting ($(exp)), got ($(got))."
end
