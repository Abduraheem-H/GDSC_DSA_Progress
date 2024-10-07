class Solution:
    def frequencySort(self, s: str) -> str:
        hash_map={}
        for letter in s:
            if letter in hash_map:
                hash_map[letter]+=1
            else:
                hash_map[letter]=1
        sorted_hash=dict(sorted(hash_map.items(), key=lambda item: item[1], reverse=True))

        count=0
        ans=[]
        for key in sorted_hash.keys():
            ans.extend([key]*sorted_hash[key])
        return "".join(ans)

        