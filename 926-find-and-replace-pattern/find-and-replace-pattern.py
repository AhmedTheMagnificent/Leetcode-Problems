class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        output = []
        for word in words:
            hashMap = {}
            reverseMap = {}
            signal = True
            for i in range(len(word)):
                if word[i] in hashMap and hashMap[word[i]] != pattern[i]:
                    signal = False
                    break
                if pattern[i] in reverseMap and reverseMap[pattern[i]] != word[i]:
                    signal = False
                    break
                hashMap[word[i]] = pattern[i]
                reverseMap[pattern[i]] = word[i]
            if not signal:
                continue
            output.append(word)
        return output
