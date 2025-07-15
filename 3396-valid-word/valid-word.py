class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        
        vowels = set('aeiouAEIOU')
        hasVowels = False
        hasConsonants = False
        for ch in word:
            if not ch.isalnum():
                return False
            if ch.isalpha():
                if ch in vowels:
                    hasVowels = True
                else:
                    hasConsonants = True
        return hasVowels and hasConsonants