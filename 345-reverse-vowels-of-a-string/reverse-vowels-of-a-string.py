class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        f = 0
        l = len(s) - 1
        s_list = list(s)
        
        while f < l:
            if s_list[f] not in vowels:
                f += 1
            elif s_list[l] not in vowels:
                l -= 1
            else:
                s_list[f], s_list[l] = s_list[l], s_list[f]
                f += 1
                l -= 1
        
        return "".join(s_list)
