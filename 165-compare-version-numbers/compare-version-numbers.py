class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = [int(i) for i in version1.split(".")]
        version2 = [int(i) for i in version2.split(".")]
        len_v1 = len(version1) 
        len_v2 = len(version2) 
        i, j = 0, 0
        while i < len_v1 and j < len_v2:
            if version1[i] < version2[j]:
                return -1                
            elif version1[i] > version2[i]:
                
                return 1
            i += 1
            j += 1
        
        while i < len_v1:
            if version1[i] > 0:
                return 1
            i += 1
        while j < len_v2:
            if version2[j] > 0:
                return -1
            j += 1
        return 0