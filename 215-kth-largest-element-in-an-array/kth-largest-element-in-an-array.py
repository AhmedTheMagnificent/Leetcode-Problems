class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # Step 1: Build the max heap
        for i in range(len(nums) // 2 - 1, -1, -1):
            self.heapify(nums, i, len(nums))

        # Step 2: Extract the maximum k times
        maxi = 0
        for i in range(k):
            maxi = self.extractmax(nums, len(nums) - i)

        return maxi

    def heapify(self, arr: list[int], i: int, n: int):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if i != largest:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, largest, n)

    def extractmax(self, arr: list[int], n: int) -> int:
        if len(arr) == 0:
            return None
        if len(arr) == 1:
            return arr[0]
        
        # Swap the root (max element) with the last element
        max_element = arr[0]
        arr[0] = arr[n - 1]
        
        # Reduce the size of the heap and heapify the root element
        self.heapify(arr, 0, n - 1)
        
        # Return the extracted max element
        return max_element
