function minCostClimbingStairs(cost)
    modcost = copy(cost)
    append!(modcost, [0])

    save = Dict()
    function mincost(i)
        if i < 3
            return modcost[i]
        end

        if i in keys(save)
            return save[i]
        end

        save[i] = modcost[i] + min(mincost(i-2), mincost(i-1))
        return save[i]
    end

    return mincost(length(cost) + 1)
end

cases = [
    ([10, 15, 20], 15),
    ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
    ([0, 0, 0, 0], 0),
    ([0, 1, 2], 1),
]

for (cost, exp) in cases
    ans = minCostClimbingStairs(cost)
    @assert ans == exp "Failed ($(cost)) - got ($(ans)), expecting ($(exp))"
end
