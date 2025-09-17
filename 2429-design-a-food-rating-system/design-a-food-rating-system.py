class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = {food: (cuisine, rating) for food, cuisine, rating in zip(foods, cuisines, ratings)}

        self.cuisines = {}
        for f, c, r in zip(foods, cuisines, ratings):
            if c not in self.cuisines:
                self.cuisines[c] = []
            heapq.heappush(self.cuisines[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        c, _ = self.foods[food]
        self.foods[food] = (c, newRating)
        heapq.heappush(self.cuisines[c], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisines[cuisine]
        while heap:
            r, f = heap[0]
            if -r == self.foods[f][1]:
                return f
            else:
                heapq.heappop(heap)


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)