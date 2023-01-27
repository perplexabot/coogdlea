"""
    Given that julia is 1-indexed based, the following changes now hold:
        -   middleindex == 1, left side considered 0
        -   middleindex == len(nums), right side considered 0
    Cases expected values will also change
"""
function findMiddleIndex(nums::Vector{Int64})::Int64
    if length(nums) == 1
        return 1
    end

    if sum(nums[2:end]) == 0
        return 1
    end

    if sum(nums[1:end-1]) == 0
        return length(nums)
    end

    for index in range(1,length(nums),step=1)
        if index == 1
            left = 0
            right = sum(nums[2:end])
        elseif index == length(nums)
            left = sum(nums[1:end-1])
            right = 0
        else
            left = sum(nums[1:index-1])
            right = sum(nums[index+1:end])
        end
        if left == right
            return index
        end
    end
    return -1
end

cases = [
    ([2, 3, -1, 8, 4], 4),
    ([1, -1, 4], 3),
    ([2, 5], -1),
    ([0], 1),
    ([1, -1, 1], 1),
    ([-1, 1, 10], 3),
    ([1], 1),
]

for (nums, exp) in cases
    got = findMiddleIndex(nums)
    @assert got == exp "Failed case ($(nums)) - expecting ($(exp)), got ($(got))."
end

