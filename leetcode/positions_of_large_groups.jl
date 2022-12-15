function largeGroupPositions(s)
    if length(s) < 3
        return []
    end

    start = 1
    curr = s[1]
    bounds = []

    for (ind,c) in enumerate(s[2:end])
        if c != curr
            append!(bounds, [[start, ind]])
            curr = c
            start = ind + 1
        end
    end

    append!(bounds, [[start, length(s)]])
    return [[x[1]-1,x[2]-1] for x in bounds if x[2] - x[1] > 1]
end

cases = [
    ("abbxxxxzzy", [[3, 6]]),
    ("abc", []),
    ("abcdddeeeeaabbbcd", [[3, 5], [6, 9], [12, 14]]),
    ("", []),
    ("a", []),
    ("aa", []),
    ("aaa", [[0, 2]]),
    ("abbc", []),
    ("abcdeee", [[4, 6]]),
    ("abcdeeefff", [[4, 6], [7, 9]]),
]

for (s, exp) in cases
    ans = largeGroupPositions(s)
    @assert isequal(ans,exp) "Failed case ($(s)), got ($(ans)) but expecting ($(exp))"
end
