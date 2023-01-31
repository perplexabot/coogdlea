# julia is 1-index based, so expected cases need to be incremented by one.

function findKDistantIndices(nums::Vector{Int64}, key::Int64, k::Int64)::Vector{Int64}
    ans = Set()
    for (index, element) in enumerate(nums)
        if element == key
            union!(ans, range(index - k, index + k, step=1))
        end
    end

    ans = sort!([e for e in ans if e > 0 && e <= length(nums)])
    return ans
end

cases = [
    ([3, 4, 9, 1, 3, 9, 5], 9, 1, [2, 3, 4, 5, 6, 7]),
    ([2, 2, 2, 2, 2], 2, 2, [1, 2, 3, 4, 5]),
    ([1], 1, 1, [1]),
    ([1], 5, 1, []),
    ([1], 1, 4, [1]),
]

for (nums, key, k, exp) in cases
    got = findKDistantIndices(nums, key, k)
    @assert got == exp "Failed case ($(nums), $(key), $(k)) - expecting ($(exp)), got ($(got))."
end
