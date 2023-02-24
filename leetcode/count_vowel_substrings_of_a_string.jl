function countVowelSubstrings(word::String)::Int64
    if length(word) < 5
        return 0
    end

    vowels = Set(collect("aeiou"))
    ways = 0
    for s in range(1, length(word), step=1)
        println("here $(word[s])")
        if word[s] in vowels
            println("here too")
            e = s + 1
            while e <= length(word) && word[e] in vowels
                if isempty(symdiff(Set(word[s:e]), vowels))
                    ways += 1
                end
                e += 1
            end
        end
    end
    return ways
end

cases = [("aeiou", 1), ("abeiou", 0), ("unicornarihan", 0), ("cuaieuouac", 7)]

for (word, exp) in cases
    got = countVowelSubstrings(word)
    @assert got == exp "Failed case ($(word)) - expecting ($(exp)), got ($(got))"
end
