function maxSubsequence(nums, k)
    if k > length(nums) || k == 0
        return []
    end

    if k == length(nums)
        return nums
    end

    maxes = nums[1:k]
    for i in nums[k+1:end]
        if i > minimum(maxes)
            deleteat!(maxes, findall(x->x==minimum(maxes), maxes))
            append!(maxes,[i])
        end
    end

    return maxes
end


cases = [
    ([2, 1, 3, 3], 2, [3, 3]),
    ([-1, -2, 3, 4], 3, [-1, 3, 4]),
    ([3, 4, 3, 3], 2, [3, 4]),
    ([], 3, []),
    ([1], 10, []),
    ([1], 1, [1]),
    ([1, 2], 1, [2]),
    ([1, 2], 2, [1, 2]),
    ([1, 2, 34], 1, [34]),
    ([1, 2, 3], 0, []),
]

for (nums, k, exp) in cases
    ans = maxSubsequence(nums, k)
    @assert ans == exp "Failed ($(nums), $(k)) - expecting ($(exp)), got($(ans))"
end
