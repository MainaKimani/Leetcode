"""
Python3 used for this solution
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # create a dictionary to store the mapping between characters and words
        d = {}
        # split the string into words
        words = s.split()
        # check if the number of characters in the pattern matches the number of words in the string
        if len(pattern) != len(words):
            return False
         # iterate over the pattern and the words
        for i in range(len(pattern)):
            # check if the character is already in the dictionary
            if pattern[i] in d:
                # check if the word is the same as the one stored in the dictionary
                if d[pattern[i]] != words[i]:
                    return False
            else:
                # check if the word is already in the dictionary
                if words[i] in d.values():
                    return False
                # add the character and word to the dictionary
                d[pattern[i]] = words[i]
        # return True if all the characters and words match
        return True