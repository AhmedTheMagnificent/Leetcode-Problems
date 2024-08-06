class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.length = 0
        self.array = []

    def push(self, x: int) -> None:
        if self.length < self.maxSize:
            self.array.append(x)
            self.length += 1

    def pop(self) -> int:
        if self.length == 0:
            return -1
        else:
            self.length -= 1
            return self.array.pop()
        

    def increment(self, k: int, val: int) -> None:
        limit = min(k, self.length)
        for i in range(limit):
            self.array[i] += val
        return self.array


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)