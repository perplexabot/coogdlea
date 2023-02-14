function smallestEvenMultiple(n::Int64)::Int64
    cnt = n
    while true
        if iszero(cnt % 2) && iszero(cnt % n)
            return cnt
        end
        cnt += 1
    end
end

cases = [(5, 10), (6, 6), (1, 2)]

for (n, exp) in cases
    got = smallestEvenMultiple(n)
    @assert got == exp "Failed case ($(n)) - expecting ($(exp)), got ($(got))."
end
