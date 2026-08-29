class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        frequency_pair = [(-freq, n) for n,freq in frequency.items()]
        heapq.heapify(frequency_pair)
        return [heapq.heappop(frequency_pair)[1] for i in range(k)]