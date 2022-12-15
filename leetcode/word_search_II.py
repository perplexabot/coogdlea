"""Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells
are those horizontally or vertically neighboring. The same letter cell may not be used more than
once in a word.

Example:
    Input:
    words = ["oath","pea","eat","rain"] and board =
    [
      ['o','a','a','n'],
      ['e','t','a','e'],
      ['i','h','k','r'],
      ['i','f','l','v']
    ]
    Output: ["eat","oath"]

Note:
    You may assume that all inputs are consist of lowercase letters a-z.
"""


class Solution:
    def findWords(self, board: 'List[List[str]]', words: 'List[str]') -> 'List[str]':
        if not words or not board or not board[0]:
            return []

        def dfs(curr_loc, nd, word):

            if nd[1]:
                output.add(word)

            r, c = curr_loc[0], curr_loc[1]
            if not (r > -1 and r < len(board) and c > -1 and c < len(board[0])):
                return

            if board[r][c] in nd[0]:
                adjs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

                ch = board[r][c]
                nd = nd[0][ch]

                board[r][c] = None
                for adj in adjs:
                    dfs(adj, nd, word + ch)
                board[r][c] = ch

        def add_to_trie(word):
            curr = Trie['root']
            index = 0
            while index < len(word):
                if word[index] not in curr[0]:
                    curr[0][word[index]] = [{}, False]
                curr = curr[0][word[index]]
                index += 1
            curr[1] = True

        rows = len(board)
        cols = len(board[0])
        words = set([word for word in words if len(word) <= rows * cols])

        Trie = {'root': [{}, False]}
        for word in words:
            add_to_trie(word)

        output = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs((row, col), Trie['root'], '')

        return list(output)


inps = [
    (
        ["oath", "pea", "eat", "rain"],
        [['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'], ['i', 'h', 'k', 'r'], ['i', 'f', 'l', 'v']],
        ["eat", "oath"],
    ),
    (['a', 'a'], [['a']], ['a']),
    (['a', 'b', 'c', 'd'], [['a', 'b'], ['c', 'd']], ['a', 'b', 'c', 'd']),
    ([], [['a', 'b'], ['c', 'd']], []),
    (['a', 'b', 'c', 'd'], [], []),
    (['a', 'b', 'c', 'd'], [[]], []),
    (['afro', 'jack'], [['a', 'f'], ['o', 'r']], ['afro']),
    (['afro', 'jack'], [['a', 'f'], ['r', 'o']], []),
    (['eeee'], [['e', 'e'], ['e', 'e']], ['eeee']),
    (['eeeee'], [['e', 'e'], ['e', 'e'], ['f', 'f']], []),
    (['e'], [['e']], ['e']),
    (['packapunch'], [list('packapunch')], ['packapunch']),
    (['packapunch'], [[c] for c in 'packapunch'], ['packapunch']),
    (['packapunch'], [list('packzpunch')], []),
    (['packapunch'], [[c] for c in 'packiunch'], []),
]

sol = Solution()
for index, (words, board, exp) in enumerate(inps):
    print(f"Attempting to find words in board for case {index} and asserting...")
    ans = sol.findWords(board, words)
    assert set(ans) == set(exp), f"Got: {ans}, exp: {exp}"
