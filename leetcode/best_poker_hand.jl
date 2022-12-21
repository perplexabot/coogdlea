function bestHand(ranks, suits)
    cnts = Dict(rank => count(i->i==rank, ranks) for rank in ranks)
    if length(Set(suits)) == 1
        return "Flush"
    end

    if any(i->i>2, values(cnts))
        return "Three of a Kind"
    end

    if 2 in Set(values(cnts))
        return "Pair"
    end
    return "High Card"
end

cases = [
    ([13, 2, 3, 1, 9], ["a", "a", "a", "a", "a"], "Flush"),
    ([4, 4, 2, 4, 4], ["d", "a", "a", "b", "c"], "Three of a Kind"),
    ([10, 10, 2, 12, 9], ["a", "b", "c", "a", "d"], "Pair"),
    ([1, 2, 3, 4, 5], ["a", "b", "c", "a", "d"], "High Card"),
    ([2, 10, 7, 10, 7], ["a", "b", "a", "d", "b"], "Pair"),
]

for (ranks, suits, exp) in cases
    got = bestHand(ranks, suits)
    @assert got == exp "Failed case ($(ranks), $(suits)) - got ($(got)), expecting ($(exp))"
end
