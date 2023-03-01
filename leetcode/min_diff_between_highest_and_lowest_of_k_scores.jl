function minimumDifference(nums::Vector{Int64}, k::Int64)::Int64
    sort!(nums)
    s = 1
    e = s + k - 1
    ans = Inf
    while e <= length(nums)
        ans = min(ans, nums[e] - nums[s])
        s += 1
        e += 1
    end
    return ans
end

cases = [([90], 1, 0), ([9, 4, 1, 7], 2, 2)]

for (nums, k, exp) in cases
    got = minimumDifference(nums, k)
    @assert got == exp "Failed case ($(nums), $(k)) - expecting ($(exp)), got ($(got))."
end
