function numIdenticalPairs(nums)
    if isempty(nums)
        return 0
    end

    cnts = Dict(val=>count(i->i==val, nums) for val in nums)
    return sum([factorial(cnt) / (2 * factorial(cnt - 2)) for cnt in values(cnts) if cnt > 1])
end


cases = [([1, 2, 3], 0), ([1, 2, 3, 1, 1, 3], 4), ([1, 1, 1, 1], 6), ([], 0), ([1], 0)]

for (nums, exp) in cases
    got = numIdenticalPairs(nums)
    @assert got == exp "Assert fail with ($(nums)) - expecting ($(exp)), got ($(got))"
end
