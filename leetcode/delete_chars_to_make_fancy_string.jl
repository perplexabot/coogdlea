function makeFancyString(s::String)::String
    if length(s) < 3
        return s
    end

    reps = []
    prev = s[begin]
    curr_s = 1
    curr_e = 1
    for (ind, e) in enumerate(s[2:end])
        if e == prev
            curr_e = ind + 1
        else
            push!(reps, (curr_s, curr_e))
            curr_s = ind + 1
            curr_e = ind + 1
            prev = e
        end
    end
    push!(reps, (curr_s, curr_e))

    new_str = []
    for (st, en) in reps
        if en - st > 1
            append!(new_str, s[st] ^ 2)
        else
            append!(new_str, s[st:en])
        end
    end

    return join(new_str)
end


cases = [
    ("leeetcode", "leetcode"),
    ("aaabaaaa", "aabaa"),
    ("aab", "aab"),
    ("a", "a"),
    ("ab", "ab"),
    ("aaa", "aa"),
    ("aa", "aa"),
    ("abc", "abc"),
    ("aba", "aba"),
    ("aaaaaaaaaaaaaaaaaaaaa", "aa"),
]

for (s, exp) in cases
    got = makeFancyString(s)
    @assert got == exp "Failed case ($(s)) -  got ($(got)), expecting ($(exp))"
end
