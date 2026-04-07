class Robot:

    def __init__(self, width: int, height: int):
        self.h = height
        self.w = width
        self.x = 0
        self.y = 0
        self.dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        self.dirNames = ["East", "North", "West", "South"]
        self.dirIndex = 0
        self.perimeter = 2 * (height + width) - 4

    def step(self, num: int) -> None:
        num %= self.perimeter
        if num == 0:
            if self.x == 0 and self.y == 0:
                self.dirIndex = 3  # South
            return
        while num > 0:
            dx, dy = self.dirs[self.dirIndex]
            nx = self.x + dx
            ny = self.y + dy
            
            if not (0 <= nx < self.w and 0 <= ny < self.h):
                self.dirIndex = (self.dirIndex + 1) % 4
                continue
            
            self.x = nx
            self.y = ny
            num -= 1

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.dirNames[self.dirIndex]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()