# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.performSort(pairs, 0, len(pairs)-1)
        return pairs
    
    def performSort(self, arr, s, e):
        if e-s+1 <= 1:
            return
        
        pivot = arr[e]
        l = s

        for i in range(s, e):
            if arr[i].key < pivot.key:
                arr[l], arr[i] = arr[i], arr[l]
                l+=1
        
        arr[e] = arr[l]
        arr[l] = pivot

        self.performSort(arr, s, l-1)
        self.performSort(arr, l+1, e)

        return arr
    