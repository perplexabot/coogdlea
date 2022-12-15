"""
Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides
    lowercase letters, the email may contain one or more '.' or '+'.
    - For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com"
        is the domain name.

If you add periods '.' between some characters in the local name part of an email address, mail sent
    there will be forwarded to the same address without dots in the local name. Note that this rule
    does not apply to domain names.
    - For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same
        email address.

If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This
    allows certain emails to be filtered. Note that this rule does not apply to domain names.
    - For example, "m.y+name@email.com" will be forwarded to "my@email.com".

It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each emails[i], return the number
    of different addresses that actually receive mails.

Example 1:
    Input: emails = ["test.email+alex@leetcode.com",
                     "test.e.mail+bob.cathy@leetcode.com",
                     "testemail+david@lee.tcode.com"]
    Output: 2
    Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.

Example 2:
    Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
    Output: 3

Constraints:
    1 <= emails.length <= 100
    1 <= emails[i].length <= 100
    emails[i] consist of lowercase English letters, '+', '.' and '@'.
    Each emails[i] contains exactly one '@' character.
    All local and domain names are non-empty.
    Local names do not start with a '+' character.
    Domain names end with the ".com" suffix.

A:
    no at sign in email -> ignore it (throw it away) (constraint says not possible)
    email with only '@' (no local or domain) -> ignore/throw away (constraint says not possible)
    only dots and/or at for local name -> treat it as a valid email
D:
    emails = ["test.email+alex@leetcode.com",
              "test.e.mail+bob.cathy@leetcode.com",
              "testemail+david@lee.tcode.com"]

    uniqes = []
    emails[0] -> at_ind = emails[0].index('@') = 15, curr = []
                 emails[0][0] is a char -> curr.append(emails[0][0])
                 emails[0][1] is a char -> curr.append(emails[0][1])
                 ...
                 emails[0][4] is a '.' -> continue
                 emails[0][5] is a char -> curr.append(emails[0][5])
                 ...
                 emails[0][9] is a char -> curr.append(emails[0][9])
                 emails[0][10] is a '+' -> break
                 uniques.append(''.join(curr) + emails[0][15:])
    emails[1] -> at_ind = emails[1].index('@') = 21, curr = []
                 emails[1][0] is a char -> curr.append(emails[1][0])
                 ...
                 <same as above>

P:
    uniques = []
    for e in email:
        local,domain = e.split('@')
        nlocal = []
        for c in local:
            if c == '.':
                continue
            elif c == '+':
                break
            else:
                nlocal.append(c)
        uniques.append(''.join(nlocal) + '@' + domain)

O:
    uniques = []
    for e in emails:
        at_ind = e.index("@")
        curr = []
        for i in range(at_ind):
            if e[i] == '.':
                continue
            if e[i] == '+':
                break
            curr.append(e[i])
        uniques.append(''.join(curr) + e[at_ind:])
    return len(uniques)
"""


def numUniqueEmails(emails: list[str]) -> int:
    uniques = set()
    for e in emails:
        at_ind = e.index("@")
        curr = []

        for i in range(at_ind):
            if e[i] == '.':
                continue
            if e[i] == '+':
                break
            curr.append(e[i])
        uniques.add(''.join(curr) + e[at_ind:])
    return len(uniques)


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

for (emails, exp) in cases:
    assert (
        got := numUniqueEmails(emails)
    ) == exp, f"Failed with ({emails}) - expecting ({exp}), got ({got})"
