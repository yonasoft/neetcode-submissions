# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def quickSortImpl(arr,s,e):
            if e-s+1 <= 1:
                return arr
            left = s
            pivot = arr[e]

            for i in range(s,e):
                if arr[i].key < pivot.key:
                    arr[i], arr[left] = arr[left], arr[i]
                    left += 1
            arr[e] = arr[left] 
            arr[left] = pivot

            quickSortImpl(arr,s,left-1)
            quickSortImpl(arr,left+1,e)

            return arr
        return quickSortImpl(pairs,0,len(pairs)-1)
