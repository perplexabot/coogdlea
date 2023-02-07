function kWeakestRows(mat::Vector{Vector{Int64}}, k::Int64)::Vector{Int64}
    strengths = []
    for (ind, row) in enumerate(mat)
        sol_cnt = 0
        for elem in row
            if iszero(elem)
                break
            end
            sol_cnt += 1
        end
        push!(strengths, (sol_cnt, ind))
    end
    sort!(strengths)
    return [x[2] for x in strengths[begin:k]]
end

cases = [
    (
        [[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]],
        3,
        [3, 1, 4],
    ),
    ([[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]], 2, [1, 3]),
    ([[0, 0], [0, 0]], 2, [1, 2]),
    ([[1, 0], [1, 0]], 2, [1, 2]),
    ([[1, 0], [1, 0]], 1, [1]),
    ([[0, 0], [1, 0]], 1, [1]),
]

for (mat, k, exp) in cases
    got = kWeakestRows(mat, k)
    @assert got == exp "Failed case ($(mat), $(k)) - expecting ($(exp)), got ($(got))"
end
