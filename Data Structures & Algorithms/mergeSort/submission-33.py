# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def merge(arr,s,m,e):
            left =  arr[s:m+1]
            right = arr[m+1:e+1]
            lp, rp, ap = 0, 0, s
            while lp < len(left) and rp < len(right):
                if left[lp].key <= right[rp].key:
                    arr[ap] = left[lp]
                    lp += 1
                else:
                    arr[ap] = right[rp]
                    rp += 1
                ap += 1
            while lp < len(left):
                arr[ap] = left[lp]
                lp +=1
                ap += 1
            while rp < len(right):
                arr[ap] = right[rp]
                rp += 1
                ap += 1

        def mergeSortImpl(arr,s,e):
            if e-s+1 <= 1:
                return arr
            m = (e+s)//2
            mergeSortImpl(arr,s,m)
            mergeSortImpl(arr,m+1,e)
            merge(arr,s,m,e)
            return arr
        
        return mergeSortImpl(pairs,0,len(pairs)-1)