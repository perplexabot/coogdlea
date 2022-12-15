function kLengthApart(nums, k)
    if k < 0
        return false
    end

    if isempty(nums)
        return true
    end


    one_inds = [index for (index,num) in enumerate(nums) if num == 1]
    if length(one_inds) == 1
        diffs = []
    else
        diffs = [one_inds[i] - one_inds[i - 1] - 1 for i in range(2, length(one_inds))]
    end

    return all(i->i >= k, diffs)
end

cases = [
    ([1, 0, 0, 0, 1, 0, 0, 1], 2, true),
    ([1, 0, 0, 1, 0, 1], 2, false),
    ([1, 2, 1], -1, false),
    ([], 3, true),
    ([], 0, true),
    ([1, 0, 1], 0, true),
    ([1, 1], 0, true),
    ([1, 1, 2], 0, true),
    ([0, 1, 1, 0], 0, true),
    ([0, 0, 3, 0], 3, true),
    ([1], 10, true),
    ([0], 3, true),
    ([1, 0, 1], 5, false),
]

for (nums, k, exp) in cases
    ans = kLengthApart(nums, k)
    @assert ans == exp "Failed ($(nums), $(k)) - expecting ($(exp)), got ($(ans))"
end
