function isPowerOfFour(n)
    if n <= 0
        return false
    end

    ans = log(n) / log(4)
    return ans - trunc(Int, ans) == 0
end

cases = [
    (16, true),
    (5, false),
    (1, true),
    (0, false),
    (-1, false),
    (4, true),
    (-4, false),
    (625, false),
]

for (n, exp) in cases
    ans = isPowerOfFour(n)
    @assert ans == exp "Failed ($(n)) - expecting ($(exp)), got ($(ans))"
end
