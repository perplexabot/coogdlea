using DataStructures

function distinctAverages(nums::Vector{Int64})::Int64
    d = DataStructures.Deque{Int64}()
    for num in sort(nums)
        push!(d, num)
    end

    aves = Set()
    while !isempty(d)
        push!(aves, pop!(d) + popfirst!(d))
    end

    return length(aves)
end

cases = [
    ([4, 1, 4, 0, 3, 5], 2),
    ([1, 100], 1),
    ([1, 1, 1, 1], 1),
    ([1, 2, 3, 4], 1),
    ([4, 3, 2, 1], 1),
    ([3, 4, 2, 1], 1),
    ([1, 2, 1, 2], 1),
    ([1, 2, 12, 14], 2),
]

for (nums, exp) in cases
    got = distinctAverages(nums)
    @assert got == exp "Failed case ($(nums)) - expecting ($(exp)), got ($(got))."
end
