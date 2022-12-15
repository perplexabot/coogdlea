function plusOne(digits)
    if isempty(digits) || isnothing(digits)
        return nothing
    end

    carry = 1
    final = copy(digits)
    for (ind, elem) in enumerate(reverse(final))
        summation = elem + carry
        ones = summation % 10
        carry = fld(summation, 10)
        final[length(digits) - ind + 1] = ones
    end

    if carry > 0
        return append!([carry], final)
    else
        return final
    end
end

cases = [
    ([1, 2, 3], [1, 2, 4]),
    ([4, 3, 2, 1], [4, 3, 2, 2]),
    ([9], [1, 0]),
    ([], nothing),
    ([0], [1]),
    ([9, 9, 9], [1, 0, 0, 0]),
]

for (digits, exp) in cases
    ans = plusOne(digits)
    @assert ans == exp "Failed with ($(digits)) - expecting ($(exp)), got ($(ans))"
end
