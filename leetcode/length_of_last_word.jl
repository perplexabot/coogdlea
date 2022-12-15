function lengthOfLastWord(s)
    if isnothing(s) || isempty(strip(s))
        return 0
    end

    return length(split(s)[end])
end


cases = [
    ("Hello World", 5),
    ("   fly me   to   the moon  ", 4),
    ("luffy is still joyboy", 6),
    ("", 0),
    ("a", 1),
    (nothing, 0),
    ("    ", 0),
]

for (s, exp) in cases
    ans = lengthOfLastWord(s)
    @assert ans == exp "Failed with ($(s)) - expecting ($(exp)), got ($(ans))"
end
