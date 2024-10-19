class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = ["0"]
        for i in range(1, n):
            s.append(s[i-1] + "1" + self.reverse(self.invert(s[i-1])))

        return s[n-1][k-1]

    def reverse(self, string):
        return string[::-1]

    def invert(self, string):
        inverted = ""
        for i in range(len(string)):
            if string[i] == "1":
                inverted += "0"
            else:
                inverted += "1"

        return inverted