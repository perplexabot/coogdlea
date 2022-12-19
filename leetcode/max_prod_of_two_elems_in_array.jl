function maxProduct(nums)
    if length(nums) < 2
        return 0
    end

    max0, max1 = nums[1:2]

    for n in nums[3:end]
        if n > minimum([max0,max1])
            if max0 < max1
                max0 = n
            else
                max1 = n
            end
        end
    end
    return (max0 - 1) * (max1 - 1)
end

cases = [
    ([3, 4, 5, 2], 12),
    ([1, 5, 4, 5], 16),
    ([3, 7], 12),
    ([], 0),
    ([1], 0),
    ([1, 2], 0),
    ([1, 1], 0),
    ([10, 1, 10], 81),
    ([10, 10, 1], 81),
    ([1, 10, 10], 81),
    ([2, 1, 2, 1], 1),
]

for (nums, exp) in cases
    got = maxProduct(nums)
    @assert got == exp "Failed case ($(nums)) - expecting ($(exp)), got ($(got))"
end
