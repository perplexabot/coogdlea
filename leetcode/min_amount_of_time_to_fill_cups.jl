function getMinIndex(x)
    y = Vector{Int64}()
    for e in x
        if iszero(e)
            append!(y, inf)
        else
            append!(y, e)
        end
    end

    mi = 1
    if y[2] < y[mi]
        mi = 2
    end

    if y[3] < y[mi]
        mi = 3
    end
    return mi
end

function getMaxIndex(x)
    mi = 1
    if x[2] > x[mi]
        mi = 2
    end

    if x[3] > x[mi]
        mi = 3
    end
    return mi
end

function fillCups(amount)
    fills = 0

    while amount != [0,0,0]
        done = count(i->i==0, amount)
        if iszero(done)
            amount[getMinIndex(amount)] -= 1
            amount[getMaxIndex(amount)] -= 1
            fills += 1
        elseif done == 1
            inds = [ind for (ind, elem) in enumerate(amount) if !iszero(elem)]
            amount[inds[1]] -= 1
            amount[inds[2]] -= 1
            fills += 1
        else
            fills += sum(amount)
            amount = [0,0,0]
        end
    end
    return fills
end

cases = [
    ([1, 4, 2], 4),
    ([5, 4, 4], 7),
    ([5, 0, 0], 5),
    ([0, 0, 0], 0),
    ([1, 1, 1], 2),
    ([0, 0, 1], 1),
    ([0, 1, 0], 1),
    ([1, 0, 0], 1),
    ([1, 0, 1], 1),
    ([0, 1, 1], 1),
]

for (amounts, exp) in cases
    got = fillCups(amounts)
    @assert got == exp "Failed case ($(amounts)) - expecting ($(exp)), got ($(got))"
end
