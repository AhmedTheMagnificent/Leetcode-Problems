class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        totalApples = sum(apple)
        capacity.sort(reverse=True)
        current = 0
        count = 0

        for c in capacity:
            current += c
            count += 1
            if current >= totalApples:  return count
        return count