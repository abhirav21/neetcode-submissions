class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        T = []
        i, j = 0, 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                T.append(nums1[i])
                i += 1
            else:
                T.append(nums2[j])
                j += 1
        
        while i < len(nums1):
            T.append(nums1[i])
            i += 1
        while j < len(nums2):
            T.append(nums2[j])
            j += 1
        
        if len(T)%2 == 0:
            return (T[len(T)//2] + T[len(T)//2 - 1]) / 2
        return T[len(T)//2]
        