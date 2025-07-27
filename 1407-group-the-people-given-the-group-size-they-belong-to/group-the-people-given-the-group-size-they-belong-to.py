class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        bucket = {}

        for i in range(len(groupSizes)):
            if groupSizes[i] not in bucket:
                bucket[groupSizes[i]] = []
            bucket[groupSizes[i]].append(i)
        groups = []
        for key, value in bucket.items():
            if len(value) > key:
                i = 0
                while i < len(value):
                    groups.append(value[i: i + key])
                    i += key
            else:
                groups.append(value)
        return groups