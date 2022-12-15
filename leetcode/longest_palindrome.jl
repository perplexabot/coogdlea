function longestPalindrome(s)
    if isempty(s)
        return 0
    end

    c = Dict(c => count(i->i==c, s) for c in s)
    x = sum([fld(c[key], 2) for (key,value) in c if c[key] > 1])

    if length(s) > 2 * x
        return 2 * x + 1
    else
        return 2 * x
    end
end

cases = [("abccccdd", 7), ("a", 1), ("", 0), ("Aa", 1), ("AAa", 3), ("aaa", 3), ("aa", 2)]

for (s, exp) in cases
    ans = longestPalindrome(s)
    @assert ans == exp "Failed ($(s)) - expecting ($(exp)), got ($(ans))"
end
