class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map={}
        for num in nums:
            if num in hash_map:
                hash_map[num]+=1
            else:
                hash_map[num]=1
        sorted_hash=dict(sorted(hash_map.items(), key=lambda item: item[1], reverse=True))
        ans=[]
        for key in sorted_hash.keys():
            ans.append(key)
            k-=1
            if k==0:
                return ans



        