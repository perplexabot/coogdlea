function countLargestGroup(n::Int64)::Int64
    counts = Dict()
    for i in range(1,n)
        digs = []
        while ! iszero(i)
            append!(digs, i%10)
            i = fld(i,10)
        end

        s = sum(digs)
        if s in keys(counts)
            counts[s] += 1
        else
            counts[s] = 1
        end
    end
    max_count = maximum(values(counts))
    return sum(1 for k in keys(counts) if counts[k] == max_count)
end

cases = [(13, 4), (2, 2)]

for (n, exp) in cases
    got = countLargestGroup(n)
    @assert got == exp "Failed case ($(n)) - expecting ($(exp)), got ($(got))"
end
