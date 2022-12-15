"""Given an array of words and a width maxWidth, format the text such that each line has exactly
maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each
line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on
a line do not divide evenly between words, the empty slots on the left will be assigned more spaces
than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:
A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

Example 1:
Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:
Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.

Example 3:
Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
"""


class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        lines = [words[0]]
        for s in words[1:]:
            if len(lines[-1]) + len(s) + 1 <= maxWidth:
                lines[-1] = ' '.join([lines[-1], s])
            else:
                lines.append(s)

        lind = 0
        while lind < len(lines) - 1:
            sp_needed = maxWidth - len(lines[lind])
            wrds = lines[lind].split()
            sp_cnt = 0
            i = 0
            while sp_cnt < sp_needed:
                wrds[i] = ''.join([wrds[i], ' '])
                sp_cnt = sp_cnt + 1
                i = (i + 1) % (len(wrds) - 1) if len(wrds) > 1 else 0
            lines[lind] = ' '.join(wrds)
            lind += 1

        sp_needed = maxWidth - len(lines[-1])
        lines[-1] = ''.join([lines[-1], ' ' * sp_needed])
        return lines


inps = [
    (
        ["This", "is", "an", "example", "of", "text", "justification."],
        16,
        ["This    is    an", "example  of text", "justification.  "],
    ),
    (
        ["What", "must", "be", "acknowledgment", "shall", "be"],
        16,
        ["What   must   be", "acknowledgment  ", "shall be        "],
    ),
    (
        [
            "Science",
            "is",
            "what",
            "we",
            "understand",
            "well",
            "enough",
            "to",
            "explain",
            "to",
            "a",
            "computer.",
            "Art",
            "is",
            "everything",
            "else",
            "we",
            "do",
        ],
        20,
        [
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  ",
        ],
    ),
    (
        '12345 67891 12345 67891 12345 67891'.split(),
        5,
        ['12345', '67891', '12345', '67891', '12345', '67891'],
    ),
    (
        '12345 67891 12345 67891 12345 67891'.split(),
        6,
        ['12345 ', '67891 ', '12345 ', '67891 ', '12345 ', '67891 '],
    ),
    (
        '1234 67891 12345 67891 12 67891'.split(),
        6,
        ['1234  ', '67891 ', '12345 ', '67891 ', '12    ', '67891 '],
    ),
    (
        '1234 67891 12345 67891 1 67891'.split(),
        7,
        ['1234   ', '67891  ', '12345  ', '67891 1', '67891  '],
    ),
    ('hello'.split(), 5, ['hello']),
    ('hello'.split(), 15, ['hello          ']),
    (
        'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(),
        51,
        ['a b c d e f g h i j k l m n o p q r s t u v w x y z'],
    ),
    (
        'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(),
        50,
        ['a  b c d e f g h i j k l m n o p q r s t u v w x y', 'z' + ' ' * 49],
    ),
    (
        'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(),
        60,
        ['a b c d e f g h i j k l m n o p q r s t u v w x y z' + ' ' * 9],
    ),
    (
        'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(),
        1,
        'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(),
    ),
]

sol = Solution()
for words, maxWidth, exp in inps:
    print(f"Justifying words {words} with maxWidth of {maxWidth} and asserting... ")
    ans = sol.fullJustify(words, maxWidth)
    print(" got: ", ans)
    print(" exp: ", exp)
    assert ans == exp
