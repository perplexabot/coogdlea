function smallerNumbersThanCurrent(nums)
    snums = sort(nums)
    return [findfirst(i->i==val, snums) - 1 for val in nums]
end

cases = [
    ([8, 1, 2, 2, 3], [4, 0, 1, 1, 3]),
    ([6, 5, 4, 8], [2, 1, 0, 3]),
    ([7, 7, 7, 7], [0, 0, 0, 0]),
    ([1], [0]),
    ([], []),
    ([1, 1], [0, 0]),
    ([1, 2, 3], [0, 1, 2]),
    ([3, 2, 1], [2, 1, 0]),
    ([1, 10, 0], [1, 2, 0]),
]

for (nums, exp) in cases
    got = smallerNumbersThanCurrent(nums)
    @assert got == exp "Failed with ($(nums)) - expecting ($(exp)), got ($(got))"
end
