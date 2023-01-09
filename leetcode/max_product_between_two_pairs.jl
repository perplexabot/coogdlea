# modifying input array, can make copy instead.
function maxProductDifference(nums::Vector{Int64})::Int64
    sort!(nums)
    return (nums[end] * nums[end-1]) - (nums[1] * nums[2])
end

cases = [
    ([5, 6, 2, 7, 4], 34),
    ([4, 2, 5, 9, 7, 4, 8], 64),
    ([1, 1, 1, 1], 0),
    ([1, 2, 3, 4], 10),
    ([1, 1, 2, 2], 3),
]

for (nums, exp) in cases
    got = maxProductDifference(nums)
    @assert got == exp "Failed ($(nums)) - expecting ($(exp)), got ($(got))"
end
