"""
    Input: s = ["h","e","l","l","o"]
    len(s) = 5
    mid = 5 // 2
    curr = 1
        s[curr],s[end-curr+1] = s[end-curr+1],s[curr]
    curr = 2
        s[curr],s[end-curr+1] = s[end-curr+1],s[curr]

"""
function reverseString(s::Vector{String})
    for curr in range(1,fld(length(s),2),step=1)
        temp = s[curr]
        s[curr] = s[end-curr+1]
        s[end-curr+1] = temp
    end
end

cases = [
    (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
    (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
    (["a"], ["a"]),
    (["a", "b"], ["b", "a"]),
]

for (s, exp) in cases
    reverseString(s)
    @assert s == exp "Failed. Expecting $(exp), got $(s)"
end
