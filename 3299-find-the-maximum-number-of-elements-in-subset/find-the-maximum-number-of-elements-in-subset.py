class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 1
        if 1 in freq:   ans = freq[1] if freq[1] % 2 else freq[1] - 1
        for x in freq:
            if x == 1:  continue
            curr = x
            length = 0
            while True:
                if freq[curr] >= 2:
                    length += 2
                    curr *= curr
                elif freq[curr] == 1:
                    length += 1
                    break
                else:
                    length -= 1
                    break
            ans = max(ans, length)
        return ans
                    
