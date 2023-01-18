function repeatedNTimes(nums::Vector{Int64})::Int64
    n = fld(length(nums), 2)
    cnts = Dict()

    for num in nums
        cnts[num] = get(cnts, num, 0) + 1
        if cnts[num] == n
            return num
        end
    end
end

cases = [
    ([1, 2], 1),
    ([1, 1, 2, 3], 1),
    ([2, 3, 1, 1], 1),
    ([1, 2, 3, 3], 3),
    ([2, 1, 2, 5, 3, 2], 2),
    ([5, 1, 5, 2, 5, 3, 5, 4], 5),
]

for (case, exp) in cases
    got = repeatedNTimes(case)
    @assert got == exp "Failed case ($(case)) - expecting ($(exp)), got ($(got))."
end
