class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        l=[]
        freq={}
        for i in nums:
            if i in freq.keys():
                freq[i]+=1
            else:
                freq[i]=1
        arr = sorted(freq, key=freq.get, reverse=True)

        for i in range(k):
            l.append(arr[i])
        return l
