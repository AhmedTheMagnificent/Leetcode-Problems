class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashTable = dict()
        mapped = set()
        for a, b in zip(s, t):
            if a not in hashTable:
                if b in mapped:
                    return False
                mapped.add(b)
                hashTable[a] = b
            elif hashTable[a] != b:
                return False
        return True
