"""Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements
up front before implementing one. However, here is a list of characters that can be in a valid
decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature
accepts a const char * argument, please click the reload button to reset your code definition.
"""


class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def check_dec(x):
            if ' ' in x:
                return False
            try:
                float(x)
            except ValueError:
                return False
            return True

        def check_integ(x):
            if ' ' in x:
                return False
            try:
                int(x)
            except ValueError:
                return False
            return True

        s = s.strip()
        ss = s.split('e')
        print("ss: ", ss)
        if len(ss) > 2:
            return False

        if len(ss) == 1:
            # check as decimal
            return check_dec(ss[0])

        return check_dec(ss[0]) and check_integ(ss[1])


inps = [
    ("", False),
    ("0e0", True),
    ("0", True),
    (" 0.1 ", True),
    ("abc", False),
    ("1 a", False),
    ("2e10", True),
    (" -90e3   ", True),
    (" 1e", False),
    ("e3", False),
    (" 6e-1", True),
    (" 99e2.5 ", False),
    ("53.5e93", True),
    (" --6 ", False),
    ("-+3", False),
    ("-e+3", False),
    ("+e-3", False),
    ("+e-", False),
    ("+", False),
    ("-", False),
    (".", False),
    ("e", False),
    ("1e0", True),
    ("95a54e53", False),
    ("+1", True),
    ("-1", True),
    (".1", True),
    (".e0", False),
    ("+1e+1", True),
    ("+1e-1", True),
    ("-1e+1", True),
    ("-1e-1", True),
    ("1,000e-1", False),
    ("1e-1,000", False),
    ("96 e5", False),
]

sol = Solution()
for s, exp in inps:
    print(f"Checking if {s} is a number and asserting")
    assert sol.isNumber(s) == exp
print("*** PASSED! ***")
