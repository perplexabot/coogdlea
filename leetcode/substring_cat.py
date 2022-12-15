# You are given a string, s, and a list of words, words, that are all of the same length. Find all 
# starting indices of substring(s) in s that is a concatenation of each word in words exactly once 
# and without any intervening characters.
# 
# Example 1:
#     Input:
#         s = "barfoothefoobarman",
#         words = ["foo","bar"]
#         Output: [0,9]
#         Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
#         The output order does not matter, returning [9,0] is fine too.

# Example 2:
#     Input:
#         s = "wordgoodstudentgoodword",
#         words = ["word","student"]
#         Output: []
# 
class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        from collections import Counter

        if not words or not s:
            return []
        
        wLn = len(words[0])
        wordsLen = len( words )
        comboSize = wLn*wordsLen
        def checkForCombo(ind):
            cnt = Counter(words)
            i = ind

            while all( [ ind+wLn <= len(s), cnt[ s[ ind : ind+wLn ] ] > 0] ):
                cnt[ s[ ind : ind+wLn ] ] -= 1
                ind += wLn

            return ind - i == comboSize
        
        index = 0
        indexList = []
        while index < len(s) - (comboSize-1):
            if checkForCombo(index):
                indexList.append(index)
            index += 1
        
        return indexList

sList = [   "barfoothefoobarman", 
            "wordgoodstudentgoodword",
            "",
            "wordgoodgoodgoodbestword",
            "foobarfoobar"]

wordsLists = [  ["foo","bar"],
                ["word","student"],
                [],
                ["word", "good", "best", "good"],
                ["foo","bar"] ]

expectedOutput = [  [0,9],
                    [],
                    [],
                    [8],
                    [0,3,6] ]

sol = Solution()
for i in range( len(sList) ):
    ans = sol.findSubstring( sList[i], wordsLists[i] )
    print( "=============================================")
    print( "s = ", sList[i])
    print( "words = ", wordsLists[i] )
    try: 
        assert ans == expectedOutput[i]
    except AssertionError:
        print(" [!] Failed. Expected: ", expectedOutput[i], " but found: ", ans)
        exit()

print('--------------')
print('|   PASSED   |')
print('--------------')

