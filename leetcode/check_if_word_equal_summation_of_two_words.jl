chars = "abcdefghij"
char_to_val = Dict(char => index-1 for (index,char) in enumerate(chars))

function isSumEqual(firstWord::String, secondWord::String, targetWord::String)::Bool
    fval = parse(Int64,join([char_to_val[c] for c in firstWord]))
    sval = parse(Int64,join([char_to_val[c] for c in secondWord]))
    tval = parse(Int64,join([char_to_val[c] for c in targetWord]))
    return fval + sval == tval
end

cases = [
    ("acb", "cba", "cdb", true),
    ("aaa", "a", "aab", false),
    ("aaa", "a", "aaaa", true),
    ("a", "a", "a", true),
    ("a", "b", "b", true),
    ("aba", "a", "ba", true),
]

for (firstWord, secondWord, targetWord, expected) in cases
    got = isSumEqual(firstWord, secondWord, targetWord)
    @assert got == expected "Trying case ($(firstWord), $(secondWord), $(targetWord)) - got ($(got)), expecting ($(expected))"
end
