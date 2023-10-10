"""
Python3 used for this solution
"""

class Solution:
    """Create a funtion that accepts the pattern and string as params"""
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Create a dictionary that stores the mapping between characters and words.
        Why a dictionary? - Dictionaries cannot have two items with the same key
        (Duplicate values will overwrite existing values).
        """
        mapping_dict = {}

        """split the string into words and store them in an array"""
        words_arr = s.split()

        """
        First check is whether the length of the string equates to the length of the array.
        If not, return false.
        """
        if len(pattern) != len(words_arr):
            return False
        
        """iterate over the pattern and the words"""
        for i in range(len(pattern)):
            """start by checking if the character is already in the dictionary"""
            if pattern[i] in mapping_dict:
                """If it's present, check if the word in the array is the same as the one stored in the dictionary"""
                if mapping_dict[pattern[i]] != words_arr[i]:
                    return False
            else:
                """check if the word in the array is already in the dictionary"""
                if words_arr[i] in mapping_dict.values():
                    return False
                """If both the character and word are not in the dictionary, add them to the dictionary"""
                mapping_dict[pattern[i]] = words_arr[i]
        
        """return True if all the characters and words match"""
        return True