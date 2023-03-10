function rearrangeCharacters(s::String, target::String)::Int64
    c = Dict(char => count(i->i==char, s) for char in s)
    times = 0
    while all(v > 0 for v in values(c))
        for char in target
            if !(char in keys(c))
                return times
            elseif c[char] > 0
                c[char] -= 1
            else
                return times
            end
        end
        times += 1
    end
    return times
end

cases = [
    ("ilovecodingonleetcode", "code", 2),
    ("abcba", "abc", 1),
    ("abbaccaddaeea", "aaaaa", 1),
    ("abc", "d", 0),
    ("a", "aaa", 0),
    ("a", "a", 1),
]

for (s, target, exp) in cases
    got = rearrangeCharacters(s, target)
    @assert got == exp "Failed case ($(s), $(target)) - expecting ($(exp)), got ($(got))."
end
