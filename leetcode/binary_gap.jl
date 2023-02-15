function binaryGap(n::Int64)::Int64
    binary = bitstring(n)
    if count(i->i=='1', binary) == 1
        return 0
    end

    start = findfirst(i->i=='1', binary)
    max_count = -Inf
    cnt = 0
    for b in binary[start:end]
        if b == '1'
            max_count = max(cnt, max_count)
            cnt = 0
        end
        cnt += 1
    end

    return max_count
end

cases = [(22, 2), (8, 0), (5, 2)]

for (n, exp) in cases
    got = binaryGap(n)
    @assert got == exp "Failed case ($(n)) - expecting ($(exp)), got ($(got))."
end
