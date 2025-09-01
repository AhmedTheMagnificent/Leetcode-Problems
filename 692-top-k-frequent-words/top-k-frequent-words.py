class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashMap = {}
        for word in words:
            if word not in hashMap:
                hashMap[word] = 0
            hashMap[word] += 1

        d = dict(sorted(hashMap.items(), key=lambda item: (-item[1], item[0])))
        
        return [key for i, key in enumerate(d.keys()) if i < k]