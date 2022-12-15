function numUniqueEmails(emails)
    uniques = Set()
    for e in emails
        at_ind = findfirst(i->i=='@', e)
        curr = []
        for i in range(1, at_ind-1)
            if e[i] == '.'
                continue
            elseif e[i] == '+'
                break
            else
                append!(curr, e[i])
            end
        end
        append!(curr, e[at_ind:end])
        push!(uniques, join(curr))
    end
    return length(uniques)
end


cases = [
    (
        [
            "test.email+alex@leetcode.com",
            "test.e.mail+bob.cathy@leetcode.com",
            "testemail+david@lee.tcode.com",
        ],
        2,
    ),
    (["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"], 3),
    ([], 0),
    (["a@gmail.com"], 1),
    (["abcd@gmail.com", "abcd@nmail.com"], 2),
    (["abcd@gmail.com", "a.b.c.d@gmail.com"], 1),
    (["abcd@gmail.com", "a.b.c.d+@gmail.com"], 1),
    (["abcd@gmail.com", "+abcd@gmail.com"], 2),
    (["abcd@gmail.com", "+a.b.c.d@gmail.com"], 2),
    (["abcd@gmail.com", "abcd+abcd@gmail.com"], 1),
    (["abcd@gmail.com", "ab...cd@gmail.com"], 1),
    (["........a@gmail.com", "...........a@gmail.com"], 1),
    (["a....b@gmail.com", "a.b@gmail.com"], 1),
    (["....+...@gmail.com", ".......+.@gmail.com"], 1),
]

for (emails, exp) in cases
    got = numUniqueEmails(emails)
    @assert got == exp "Failed with ($(emails)) - expecting ($(exp)), got ($(got))"
end
