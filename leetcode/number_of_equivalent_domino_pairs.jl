function numEquivDominoPairs(dominoes)
    cnts = Dict()
    for d in dominoes
        if haskey(cnts, d)
            cnts[d] += 1
        elseif haskey(cnts, reverse(d))
            cnts[reverse(d)] += 1
        else
            cnts[d] = 1
        end
    end

    return sum(binomial(cnt,2) for cnt in values(cnts))
end

cases = [([[1, 2], [2, 1], [3, 4], [5, 6]], 1), ([[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]], 3)]

for (doms, exp) in cases
    got = numEquivDominoPairs(doms)
    @assert got == exp "Failed case ($(doms)) - expecting ($(exp)), got ($(got))"
end
