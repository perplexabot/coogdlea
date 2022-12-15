function buddyStrings(s, goal)
    if length(s) != length(goal)
        return false
    end

    cnts = Dict(char=>count(i->i==char, s) for char in s)
    diffs = []

    for i in range(1,length(s))
        if s[i] != goal[i]
            append!(diffs, [(s[i], goal[i])])
        end
    end

    if length(diffs) == 1
        return false
    elseif isempty(diffs)
        if any(i->i>1,values(cnts))
            return true
        else
            return false
        end
    elseif length(diffs) > 2
        return false
    elseif diffs[1][1] == diffs[2][2] && diffs[2][1] == diffs[1][2]
        return true
    else
        return false
    end
end

cases = [
    ("ab", "ba", true),
    ("ab", "ab", false),
    ("aa", "aa", true),
    ("a", "a", false),
    ("aaa", "aaa", true),
    ("", "", false),
    ("cab", "bac", true),
    ("abac", "abad", false),
    ("abcd", "badc", false),
    ("ab", "babbb", false),
]

for (s, goal, exp) in cases
    got = buddyStrings(s, goal)
    @assert got == exp "Failed with ($(s), $(goal)) - expecting ($(exp)), got ($(got))"
end
