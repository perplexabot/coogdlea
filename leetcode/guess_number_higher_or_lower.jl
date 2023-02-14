function guess(g::Int64)::Int64
    if g < pick
        return 1
    end

    if g > pick
        return -1
    end

    return 0
end

function guessNumber(n::Int64)::Int64
    left = 0
    right = n
    g = round(Int,left + ceil((right-left)/2))

    while true
        a = guess(g)
        if iszero(a)
            return g
        elseif a == -1
            right = g
        else
            left = g
        end

        g = round(Int,left + ceil((right - left)/2))
    end
end

cases = [(10, 6), (1, 1), (2, 1)]
for (n, p) in cases
    global pick = p
    got = guessNumber(n)
    @assert got == pick "Failed case ($(n), $(pick)) - expecting ($(pick)), got ($(got))"
end
