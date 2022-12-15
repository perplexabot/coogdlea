function countWords(words1, words2)
    if isnothing(words1) || isnothing(words2) || isempty(words1) || isempty(words2)
        return 0
    end

    counts1 = Dict(k=>count(x->x==k, words1) for k in words1)
    counts2 = Dict(k=>count(x->x==k, words2) for k in words2)
    return length([k for (k,v) in counts1 if haskey(counts2, k) && counts2[k] == 1 && counts1[k] == 1])
end

cases = [
    (["b", "bb", "bbb"], ["a", "aa", "aaa"], 0),
    (["a", "ab"], ["a", "a", "a", "ab"], 1),
    (nothing, ["a"], 0),
    ([], [], 0),
    (["a"], ["b"], 0),
    (["b"], ["b"], 1),
]

for (words1, words2, exp) in cases
    ans = countWords(words1, words2)
    @assert ans == exp "Failed ($(words1), $(words2)) - expecting ($(exp)), got ($(ans))"
end
