class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq: dict[int, int] = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        buckets: list[list[int]] = [[] for i in range(len(nums) + 1)]
        for num, count in freq.items():
            buckets[count].append(num)

        top_k: list[int] = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                top_k.append(num)
                print(top_k)
                if len(top_k) == k:
                    return top_k
