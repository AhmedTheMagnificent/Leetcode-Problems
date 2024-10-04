class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        teams = []
        chem = 0
        skill.sort()
        i, j = 0, len(skill) - 1
        number = skill[i] + skill[j]
        while i < j:
            if(skill[i] + skill[j] == number):
                teams.append((skill[i], skill[j]))
                i += 1
                j -= 1
            else:
                return -1

        for (x, y) in teams:
            chem += x*y
        
        return chem

