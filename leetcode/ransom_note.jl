function canConstruct(ransomNote, magazine)
    if isempty(ransomNote)
        return true
    end

    if isempty(magazine)
        return false
    end

    cntsR = Dict(char => count(i->i==char, ransomNote) for char in ransomNote)
    cntsM = Dict(char => count(i->i==char, magazine) for char in magazine)
    return all(cntsR[charR] <= get(cntsM, charR, 0) for charR in keys(cntsR))
end

cases = [
    ("a", "b", false),
    ("aa", "ab", false),
    ("aa", "aab", true),
    ("", "abc", true),
    ("abc", "", false),
    ("", "", true),
    ("abc", "cba", true),
    ("a", "aa", true),
    ("aa", "a", false),
    ("aabb", "bbaacc", true),
    ("abcc", "cbaa", false),
]

for (note, magazine, exp) in cases
    got = canConstruct(note, magazine)
    @assert got == exp "Failed case ($(note), $(magazine)) - expecting ($(exp)), got ($(got))."
end
