function maxRepeating(sequence::String, word::String)::Int64
    global max_count = 0
    for i in range(1, length(sequence) - length(word) + 1, step=1)
        global max_count
        count = 0
        curr = i
        while sequence[curr: curr + length(word)-1] == word
            curr += length(word)
            count += 1
            if curr + length(word) - 1 > length(sequence)
                break
            end
        end
        max_count = max(max_count, count)
    end
    return max_count
end

cases = [
    ("ababc", "ab", 2),
    ("ababc", "ba", 1),
    ("ababc", "ac", 0),
    ("aaabaaaabaaaabaaaaba", "aaaba", 4),
    ("aaabaaaabaaabaaaabaaaabaaaabaaaaba", "aaaba", 5),
]

for (seq, word, exp) in cases
    got = maxRepeating(seq, word)
    @assert got == exp "Failed case ($(seq), $(word)) - expecting $(exp), got $(got)"
end
