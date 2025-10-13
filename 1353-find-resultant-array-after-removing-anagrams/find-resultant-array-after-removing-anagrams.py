class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        output = []
        for word in words:
            if not output or sorted(word) != sorted(output[-1]):
                output.append(word)
        return output