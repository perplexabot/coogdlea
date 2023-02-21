function validMountainArray(arr::Vector{Int64})::Bool
    if length(arr) < 3
        return false
    end

    if arr[2] <= arr[1]
        return false
    end

    curr = 3
    while arr[curr] > arr[curr-1]
        curr += 1
        if curr == length(arr) + 1
            return false
        end
    end

    while arr[curr] < arr[curr-1]
        curr += 1
        if curr == length(arr) + 1
            return true
        end
    end

    return false
end

cases = [
    ([2, 1], false),
    ([3, 5, 5], false),
    ([0, 3, 2, 1], true),
    ([1], false),
    ([1, 2], false),
    ([1, 2, 1], true),
    ([1, 2, 2], false),
    ([2, 2, 1], false),
    ([1, 1, 1], false),
    ([1, 1, 2, 1], false),
    ([0, 1, 2, 3, 2], true),
    ([1, 2, 3, 2, 1, 0], true),
    ([1, 2, 3, 2, 1, 1], false),
]

for (arr, exp) in cases
    got = validMountainArray(arr)
    @assert got == exp "Failed case ($(arr)) - expecting ($(exp)), got ($(got))."
end
