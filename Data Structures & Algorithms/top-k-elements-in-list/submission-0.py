class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1 - iterate thru nums. create dict using num as name and freq as value
            # dict = {1:1, 2:2, 3:3}, l = 3
        # 1a - note largest count so we can use to initialize buckets array
        # 2 - iterate thru dict. Add dict name to appropriate bucket
            # bucket[0] = 0
            # bucket[1] = 1
            # bucket[2] = 2
            # bucket[3] = 3
        # 3 - iterate through bucket array backwards stopping at k

        # O(3n) -> O(n)


        dict = {}
        res = []
        largest = val = 0

        for num in nums:
            dict[num] = 1 + dict.get(num, 0)
            largest = max(dict[num],largest)
        
        bucket = [[] for i in range(largest + 1)]
        for num, cnt in dict.items():
            bucket[cnt].append(num)

        for i in range(len(bucket)-1,k-1,-1):
            if len(bucket[i]) > 0:
                for num in bucket[i]:
                    res.append(num)
        return res
