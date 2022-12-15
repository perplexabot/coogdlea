function isPerfectSquare(num)
    function binSearch(s,e,val)
        m = s + fld(e-s,2)
        if m*m == num
            return true
        end

        if m*m < val < (m+1)*(m+1)
            return false
        end

        if m*m < val
            return binSearch(m,e,val)
        else
            return binSearch(s,m,val)
        end
    end

    if num > 1
        return binSearch(0,num,num)
    else
        return true
    end
end

cases = [
    (16, true),
    (14, false),
    (145, false),
    (144, true),
    (0, true),
    (1, true),
    (2, false),
    (4, true),
    (9, true),
    (36, true),
    (100, true),
    (101, false),
]

for (num, exp) in cases
    got = isPerfectSquare(num)
    @assert got == exp "Failed ($(num)) - expecting ($(exp)), got ($(got))"
end
