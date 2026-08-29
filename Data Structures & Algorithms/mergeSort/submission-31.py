# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        
        def sort(arr, s, e):
            if e - s + 1 <= 1:
                return arr

            # The middle index of the array
            m = (s + e) // 2

            # Sort the left half
            sort(arr, s, m)

            # Sort the right half
            sort(arr, m + 1, e)

            # Merge sorted halfs
            merge(arr, s, m, e)
            
            return arr

        def merge(arr,s,m,e):
            L = arr[s:m+1]
            R = arr[m+1:e+1] 

            i,j,k = 0,0,s

            while i < len(L) and j < len(R):
                if L[i].key <= R[j].key:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

        return sort(pairs, 0, len(pairs)-1)

    