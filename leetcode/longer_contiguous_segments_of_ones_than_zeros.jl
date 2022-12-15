function seq_check(s)
    if isempty(s)
        return false
    end

    prev = s[1]
    cnt = 1
    maxes = Dict("0" => 0, "1" => 0, "x" => -Inf)

    for e in s[2:end] * "x"
        if e == prev
            cnt += 1
        else
            maxes[string(prev)] = max(maxes[string(prev)], cnt)
            cnt = 1
            prev = e
        end
    end
    return maxes["1"] > maxes["0"]
end

cases = [
    ("1101", true),
    ("", false),
    ("0", false),
    ("1", true),
    ("111000", false),
    ("110100010", false),
    ("01111110", true),
]

for (s, exp) in cases
    ans = seq_check(s)
    @assert ans == exp
end
