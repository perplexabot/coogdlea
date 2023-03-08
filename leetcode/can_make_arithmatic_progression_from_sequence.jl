function canMakeArithmeticProgression(arr::Vector{Int64})::Bool
    sort!(arr)

    i = 2
    diffs = Set()
    while i <= length(arr)
        push!(diffs, arr[i] - arr[i-1])
        i += 1
    end
    return length(diffs) == 1
end

cases = [([3, 5, 1], true), ([1, 2, 4], false)]

for (arr, exp) in cases
    got = canMakeArithmeticProgression(arr)
    @assert got == exp "Failed case ($(arr)) - expecting ($(exp)), got ($(got))."
end
