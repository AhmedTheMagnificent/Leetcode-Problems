class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = customers.count("Y")
        minPenalty = penalty
        bestHour = 0
        for i in range(len(customers)):
            if customers[i] == "Y": penalty -= 1
            else:                   penalty += 1
            if minPenalty > penalty:
                minPenalty = penalty
                bestHour = i + 1
        return bestHour