function minimumAbsDifference(arr::Vector{Int64})::Vector{Vector{Int64}}
    sort!(arr)
    global mindiff = Inf16
    global found = []
    for ind in range(1, length(arr) - 1, step=1)
        currdiff = abs(arr[ind] - arr[ind+1])
        global found
        global mindiff
        if currdiff < mindiff
            found = [[arr[ind],arr[ind+1]]]
            mindiff = currdiff
        elseif currdiff == mindiff
            push!(found, [arr[ind],arr[ind+1]])
        end
    end
    return found
end

cases = [
    ([4, 2, 1, 3], [[1, 2], [2, 3], [3, 4]]),
    ([1, 3, 6, 10, 15], [[1, 3]]),
    ([3, 8, -10, 23, 19, -4, -14, 27], [[-14, -10], [19, 23], [23, 27]]),
]


for (arr, exp) in cases
    got = minimumAbsDifference(arr)
    @assert got == exp "Failed case ($(arr)) - got ($(got)), expecting ($(exp))."
end
