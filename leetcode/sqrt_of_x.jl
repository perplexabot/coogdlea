function mySqrt(x)
    function binSearch(x, xstart, xend)
        mid = fld(xend-xstart, 2) + xstart
        if mid * mid <= x < (mid + 1) * (mid + 1)
            return mid
        elseif mid * mid < x
            return binSearch(x, mid, xend)
        else
            return binSearch(x, xstart, mid)
        end
    end

    if x < 2
        return x
    else
        return binSearch(x, 0, x)
    end
end

cases = [
    (4, 2),
    (8, 2),
    (0, 0),
    (81, 9),
    (144, 12),
    (9, 3),
    (1, 1),
    (2, 1),
    (100, 10),
    (101, 10),
    (99, 9),
]

for (x, exp) in cases
    ans = mySqrt(x)
    @assert ans == exp "Failed with ($(x)) - expecting ($(exp)), got ($(ans))"
end
