"""You're given a string consisting solely of (, ), and *. * can represent either a (, ),
or an empty string. Determine whether the parentheses are balanced.

For example, (()* and (*) are balanced. )*( is not balanced.
"""
from random import randint
from functools import lru_cache


@lru_cache(maxsize=1024)
def isBalanced(s, ind, cnt=0):
    if s.count('*') == len(s):
        return True
    if s[-1] == '(':
        return False

    i = ind
    while i < len(s):
        if s[i] == '*':
            if i + 1 < len(s):
                if cnt - 1 >= 0:
                    v = isBalanced(s, i + 1, cnt - 1)
                    if v:
                        return True
                v = isBalanced(s, i + 1, cnt + 1)
                if v:
                    return True
                v = isBalanced(s, i + 1, cnt)
                return True if v else False
            else:
                return True if cnt in [0, 1] else False
        elif s[i] == '(':
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                return False
        i += 1
    return True if not cnt else False


inps = [
    ('(()*', True),
    ('(*)', True),
    (')*(', False),
    ('()', True),
    ('', True),
    ('(', False),
    (')', False),
    ('*', True),
    ('****', True),
    ('***(', False),
    ('****(*', True),
    ('*)(*', True),
    (')**(', False),
    ('(())', True),
    ('()()(())(()())', True),
    (')****', False),
    (
        '(**))()*)((()))(*(*(**)(())(*(())(*****(****(*(*()*))**()**)*(*)**)**(*((*(((*((**(())*)(((***)(*)*(**))(()(*()))(*)(*)(()(*(*)**))***())((()(**((***)((((**)***))((*)))(*))(**(*(*()((*(*)*)**(())*)(()((*)()(*)())***((*)(*((())))()*)(*)****((**))*)(((*',
        False,
    ),
]

for s, exp in inps:
    print(f"Checking if {s} is balanced and asserting...")
    assert isBalanced(s, 0, 0) == exp
