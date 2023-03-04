function freqAlphabets(s::String)::String
    alphas0 = "jklmnopqrstuvwxyz"
    alphas1 = "abcdefghi"
    map_0 = Dict(join([string(num + 9), "#"]) => char for (num, char) in enumerate(alphas0))
    map_1 = Dict(string(num) => char for (num, char) in enumerate(alphas1))

    for key in keys(map_0)
        s = replace(s, key => map_0[key])
    end

    for key in keys(map_1)
        s = replace(s, key => map_1[key])
    end
    return s
end

cases = [("10#11#12", "jkab"), ("1326#", "acz")]

for (s, exp) in cases
    got = freqAlphabets(s)
    @assert got == exp "Failed case ($(s)) - expecting ($(exp)), got ($(got))."
end
