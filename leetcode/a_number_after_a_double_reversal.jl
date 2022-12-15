function isSameAfterReversals(num)
    return (num == 0) ? true : (! endswith(string(num), '0') && ! startswith(string(num), '0'))
end

cases = [
    (526, true),
    (1800, false),
    (0, true),
    (000, true),
    (10, false),
    (1, true),
    (111, true),
]

for (num,exp) in cases
    ans = isSameAfterReversals(num)
    @assert ans == exp "Failed ($(num)) - got ($(ans)), expecting ($(exp))"
end
