function areAlmostEqual(s1::String, s2::String)::Bool
    if s1 == s2
        return true
    end

    cnts = 0
    conflict = []
    for index in range(1,length(s1))
        if s1[index] == s2[index]
            continue
        end

        cnts += 1
        append!(conflict, index)
        if cnts > 2
            return false
        end
    end

    return cnts == 2 && s1[conflict[1]] == s2[conflict[2]] && s1[conflict[2]] == s2[conflict[1]]
end

cases = [
    ("bank", "kanb", true),
    ("attack", "defend", false),
    ("kelb", "kelb", true),
    ("", "", true),
    ("a", "a", true),
    ("ab", "ba", true),
    ("abc", "cbd", false),
    ("what", "hwat", true),
]

for (s1, s2, exp) in cases
    got = areAlmostEqual(s1, s2)
    @assert got == exp "Failed ($(s1), $(s2)) - expecting ($(exp)), got ($(got))"
end
