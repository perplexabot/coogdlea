function longestNiceSubstring(s::String)::String
    if length(s) < 2
        return ""
    end

    notNice = Set()
    function isNice(s::String, start::Int64, endd::Int64)::String
        if start == endd
            return ""
        end

        if (start,endd) in notNice
            s0 = isNice(s, start, endd - 1)
            s1 = isNice(s, start + 1, endd)
            if length(s0) >= length(s1)
                return s0
            else
                return s1
            end
        else
            cnts = Dict(v=>count(i->i==v, s[start:endd]) for v in s)
            nice = true
            for c in s[start:endd]
                if get(cnts,lowercase(c),0) > 0 && get(cnts, uppercase(c),0) > 0
                    continue
                else
                    push!(notNice, (start,endd))
                    nice = false
                    break
                end
            end

            if nice
                return s[start:endd]
            end

            s0 = isNice(s, start, endd - 1)
            s1 = isNice(s, start + 1, endd)
            if length(s0) >= length(s1)
                return s0
            else
                return s1
            end

        end
    end

    return isNice(s, 1, length(s))
end

cases = [
    ("YazaAay", "aAa"),
    ("Bb", "Bb"),
    ("c", ""),
    ("", ""),
    ("azz", ""),
    ("aZz", "Zz"),
    ("aAbcC", "aA"),
    ("aabcCccc", "cCccc"),
    ("abCcccCBA", "abCcccCBA"),
    ("xLeElzxgHzcWslEdgMGwEOZCXwwDMwcEhgJHLL", ""),
]

for (case, exp) in cases
    got = longestNiceSubstring(case)
    @assert got == exp "Failed case ($(case)) - got ($(got)), expecting ($(exp))"
end
