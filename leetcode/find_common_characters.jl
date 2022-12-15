function commonChars(words)
    if isempty(words)
        return []
    end

    counts = Dict(string(char) => [count(i->i==char, word) for word in words] for char in words[1])
    
    ans = String[]
    for (char, cnt) in counts
        if !(0 in counts[char])
            append!(ans, [char for i in range(0,minimum(cnt)-1)])
        end
    end

    return ans
end


cases = [
    (["bella", "label", "roller"], ["e", "l", "l"]),
    (["a", "b", "c"], []),
    (["aaa", "aa", "a"], ["a"]),
    (["cool", "lock", "cook"], ["c", "o"]),
    ([], []),
    ([""], []),
    (["", ""], []),
    (["a", ""], []),
]

for (words, exp) in cases
    ans = commonChars(words)
    @assert ans == exp "Woops! Failed with $(words) - got $(ans) expecting $(exp)"
end
