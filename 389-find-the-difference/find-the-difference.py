class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dictionary = {}
        for i in t:
            if i not in dictionary:
                dictionary[i] = 1
            else:
                dictionary[i] += 1
        for i in s:
            if i in dictionary.keys():
                dictionary[i] -= 1
        for key,value in dictionary.items():
            if value == 1:
                return key
