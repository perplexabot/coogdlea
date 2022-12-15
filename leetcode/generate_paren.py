# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    def genPar(curr, c, pL):
        if len(curr) == n*2:
            pL.append(curr)
        else:
            cL = c['(']
            cR = c[')']
            if cL < n:
                c['('] += 1
                genPar( ''.join( [ curr, '(' ] ), {'(':cL+1, ')':cR}, pL)
            if cL - cR > 0:
                c[')'] += 1
                genPar( ''.join( [ curr, ')' ] ), {'(':cL, ')':cR+1}, pL)

    curr = ''
    pL = []
    genPar(curr, { '(':0, ')':0 }, pL)
    return pL
