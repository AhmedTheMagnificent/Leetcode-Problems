class Solution:
    def wordBreak(self, s: str, wordDict: List[str], memo=None) -> bool:
        if memo is None:
            memo = {}
        
        if len(s) == 0:
            return True
        if s in memo:
            return memo[s]
        
        for word in wordDict:
            # Check if the word is a prefix of the current string
            if s.startswith(word):
                # Recursively check the rest of the string
                if self.wordBreak(s[len(word):], wordDict, memo):
                    memo[s] = True
                    return True
        
        # If no word can be matched, return False
        memo[s] = False
        return False
