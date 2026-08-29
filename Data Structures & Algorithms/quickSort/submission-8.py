# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def sort(arr, s, e):
            if e - s + 1 <= 1:
                return
            pivot = pairs[e]

            left = s
            for i in range(s, e):
                if arr[i].key < pivot.key:
                    arr[left], arr[i] = arr[i], arr[left]
                    left+=1
                
            arr[e] = arr[left]
            arr[left] = pivot

            sort(arr, s, left-1)
            sort(arr, left+1, e)

            return arr
        sort(pairs, 0, len(pairs)-1)
        return pairs
