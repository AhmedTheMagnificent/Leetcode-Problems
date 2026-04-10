class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        count = {}
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = []
            count[nums[i]].append(i)

        min_distance = float("inf")

        for num, counts in count.items():
            if len(counts) < 3:
                continue

            for i in range(len(counts) - 2):
                val = 2 * (counts[i+2] - counts[i])
                if val < min_distance:
                    min_distance = val

        return min_distance if min_distance != float("inf") else -1