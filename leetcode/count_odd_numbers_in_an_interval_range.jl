function countOdds(low::Int64, high::Int64)::Int64
    if isodd(low) && isodd(high)
        return 2 + (fld(high-low,2) - 1)
    elseif iseven(low) && iseven(high)
        return fld(high-low,2)
    else
        return fld(high-low+1,2)
    end
end

cases = [(3, 7, 3), (8, 10, 1), (1, 10, 5), (1, 1, 1), (2, 2, 0), (1, 2, 1), (1, 3, 2), (2, 4, 1)]

for (low, high, exp) in cases
    got = countOdds(low, high)
    @assert got == exp "Failed case ($(low), $(high)) - expecting ($(exp)), got ($(got))."
end
