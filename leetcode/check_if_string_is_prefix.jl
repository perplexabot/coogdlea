function isPrefixString(s, words)
    clen = 0
    curr = []
    for word in vcat(words, [""])
        if clen < length(s)
            append!(curr, [word])
            clen += length(word)
        elseif clen == length(s)
            return s == join(curr)
        else
            return false
        end
    end
end

cases = [
    ("hi", ["h", "i"], true),
    ("h", ["h"], true),
    ("h", ["h", "b"], true),
    ("h", ["haaa", "b"], false),
    ("iloveleetcode", ["i", "love", "leetcode", "apples"], true),
    ("iloveleetcode", ["apples", "i", "love", "leetcode"], false),
]

for (s, words, exp) in cases
    got = isPrefixString(s, words)
    @assert got == exp "Failed case ($(s), $(words)) - expecting ($(exp)), got ($(got))"
end
