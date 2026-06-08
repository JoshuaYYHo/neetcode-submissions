class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # two most frequent

        d = {}

        # then my counter
        # I actually need to do it like this [7, 7] -> {2: 7}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        # swapping the dict to iterate over the counter
        d_2 = {}

        for i in d:
            d_2[d[i]] = i

        # Now we find the max
        sort = sorted(d, key=lambda x: d[x], reverse=True)
        return sort[:k]