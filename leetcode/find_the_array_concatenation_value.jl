using DataStructures

function findTheArrayConcVal(nums::Vector{Int64})::Int64
    final = 0
    d = DataStructures.Deque{String}()
    push!(d, [string(x) for x in nums]...)

    while length(d) > 1
        final += parse(Int, popfirst!(d) * pop!(d))
    end

    if !isempty(d)
        final += parse(Int, pop!(d))
    end
    return final
end

cases = [([7, 52, 2, 4], 596), ([1], 1), ([5, 14, 13, 8, 12], 673)]

for (nums, exp) in cases
    got = findTheArrayConcVal(nums)
    @assert got == exp "Failed case ($(nums)) - expecting ($(exp)), got ($(got))."
end
