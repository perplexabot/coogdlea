function minimumOperations(nums::Vector{Int64})::Int64
    s = Set(nums)
    if isempty(nums) || s == Set([0])
        return 0
    end

    setdiff!(s, 0)

    ops = 0
    while true
        m = minimum(s)
        s = Set(e - m for e in s)
        ops += 1
        if s == Set([0])
            return ops
        else
            setdiff!(s,0)
        end
    end
end

cases = [
    ([1, 5, 0, 3, 5], 3),
    ([0], 0),
    ([1], 1),
    (Vector{Int64}(), 0),
    ([2, 1], 2),
    ([1, 2, 3], 3),
    ([0, 1], 1),
]

for (nums, exp) in cases
    got = minimumOperations(nums)
    @assert got == exp "Failed case ($(nums)) - expecting ($(exp)), got ($(got))."
end
