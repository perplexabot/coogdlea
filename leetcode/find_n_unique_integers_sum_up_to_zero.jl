function sumZero(n::Int64)::Vector{Int64}
    nums = []
    if iszero(n % 2)
        m = n + 1
        postives = range(1, fld((m-1), 2), step=1)
        negatives = range(-1,-fld((m-1), 2), step=-1)
        push!(nums, negatives...)
        push!(nums, 0)
        push!(nums, postives...)
        nums[end-1] += nums[end]
        pop!(nums)
    else
        postives = range(1, fld((n-1), 2), step=1)
        negatives = range(-1,-fld((n-1), 2), step=-1)
        push!(nums, negatives...)
        push!(nums, 0)
        push!(nums, postives...)
    end
    return nums
end

cases = [(5, [-2, -1, 0, 1, 2]), (3, [-1, 0, 1]), (1, [0]), (2, [-1, 1])]

for (case, exp) in cases
    got = sumZero(case)
    @assert Set(got) == Set(exp) "Failed case ($(case)) - expecting ($(exp)), got ($(got))."
end
