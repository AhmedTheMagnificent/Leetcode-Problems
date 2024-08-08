class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in image:
            for j in range(len(i)//2):
                i[j], i[len(i) - j - 1] = i[len(i) - j - 1], i[j]
            for j in range(len(i)):
                if i[j] == 0:
                    i[j] = 1
                else:
                    i[j] = 0
        return image