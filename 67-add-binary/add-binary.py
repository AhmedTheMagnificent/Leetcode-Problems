class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ret = ""
        a, b = a[::-1], b[::-1]
        for i in range(max(len(a), len(b))):
            digitA = ord(a[i]) - ord("0") if i < len(a) else 0
            digitB = ord(b[i]) - ord("0") if i < len(b) else 0
            total = digitA + digitB + carry
            char = str(total % 2)
            ret = char + ret
            carry = total // 2
        ret = "1" + ret if carry else ret
        return ret