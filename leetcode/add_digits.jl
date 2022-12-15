function addDigits(num)
    if num == nothing || isempty(num)
        return 0
    end

    digits = split(string(num), "")

    while length(digits) > 1
        s = sum([parse(Int, x) for x in digits])
        digits = split(string(s), "")
    end

    return parse(Int, digits[1])
end

cases = [(38, 2), (0, 0), ("", 0), (nothing, 0), (12345, 6), (1, 1), (11, 2), (1000, 1), (9, 9)]

for (num, exp) in cases
    ans = addDigits(num)
    @assert ans == exp "Failed ($(num)) - got ($(ans)), expecting ($(exp))"
end
