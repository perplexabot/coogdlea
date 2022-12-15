function containsPattern(arr, m, k)
    if isempty(arr) && m == 0
        return true
    end

    if length(arr) < m
        return false
    end

    if m == 1 && k == 1 && ! isempty(arr)
        return true
    end

    if m * k > length(arr)
        return false
    end

    index = 1
    while index + m < length(arr) + 1
        xstart = index
        xend = xstart + m - 1

        count = 0
        curr_pattern = arr[xstart:xend]
        while xend < length(arr) + 1 && curr_pattern == arr[xstart:xend]
            count += 1
            xstart = xend + 1
            xend = xstart + m - 1
        end

        if count >= k
            return true
        end

        index += 1
    end

    return false
end


cases = [
    ([1, 2, 4, 4, 4, 4], 1, 3, true),
    ([1, 2, 1, 2, 1, 1, 1, 3], 2, 2, true),
    ([1, 2, 1, 2, 1, 3], 2, 3, false),
    ([], 1, 1, false),
    ([1], 1, 1, true),
    ([1, 1], 1, 1, true),
    ([1, 1], 4, 1, false),
    ([], 0, 0, true),
    ([1, 2, 3, 1, 2], 2, 2, false),
    ([1, 2], 1, 2, false),
    ([1, 1], 1, 2, true),
    ([3, 6, 6, 6, 5, 1, 5, 2, 2, 3, 1, 5, 2, 6, 1, 5, 1, 2, 6, 3, 3, 5, 3, 6, 3, 4], 6, 2, false),
    ([3, 2, 2, 1, 2, 2, 1, 1, 1, 2, 3, 2, 2], 3, 2, true),
]

for (arr, m, k, exp) in cases
    ans = containsPattern(arr, m, k)
    @assert ans == exp "Failed ($(arr), $(m), $(k)) - expecting ($(exp)), got ($(ans))"
end
