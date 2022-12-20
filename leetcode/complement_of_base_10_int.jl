function bitwiseComplement(n)
    if isnothing(n)
        return nothing
    end

    return parse(Int, String(join([1-d for d in reverse(digits(n,base=2))])), base=2)
end

cases = [(5, 2), (7, 0), (10, 5), (0, 1), (nothing, nothing), (1, 0)]

for (n, exp) in cases
    got = bitwiseComplement(n)
    @assert got == exp "Failed ($(n)) - expecting ($(exp)), got ($(got))"
end
