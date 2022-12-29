function xorOperation(n, start)
    if n <= 0 || start < 0
        return nothing
    end

    return reduce(xor, [start + (2*i) for i in range(0,n-1)])
end

cases = [(5, 0, 8), (4, 3, 8), (0, 10, nothing), (10, -1, nothing)]

for (n, start, exp) in cases
    got = xorOperation(n, start)
    @assert got == exp "Failed case ($(n), $(start)) - expecting ($(exp)), got ($(got))"
end
