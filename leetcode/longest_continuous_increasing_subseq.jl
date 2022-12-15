function findLengthOfLCIS(nums)
    if length(nums) < 2
        if isempty(nums)
            return 0
        else
            return 1
        end
    end

    max_sub = -Inf
    s = 1
    while s < length(nums)
        curr = s + 1
        e = s
        while curr < length(nums) + 1 && nums[curr] > nums[curr - 1]
            curr += 1
            e += 1
        end
        max_sub = maximum([max_sub, e - s + 1])
        s = curr

    end
    return max_sub
end

cases = [
    ([1, 3, 5, 4, 7], 3),
    ([2, 2, 2, 2, 2], 1),
    ([], 0),
    ([1], 1),
    ([1, 0, -3], 1),
    ([1, 2], 2),
    ([1, 2, 3], 3),
    ([-1, 0, 1], 3),
]

for (nums, exp) in cases
    ans = findLengthOfLCIS(nums)
    @assert ans == exp "Failed ($(nums)) - expecting ($(exp)), got ($(ans))"
end
