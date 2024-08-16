class Solution:
    def sortSentence(self, s: str) -> str:
        hash_map={}
        new_list=[]
        for subStr in s.split(" "):
            hash_map[subStr[-1]]=subStr[:-1]
        #print(len(hash_map))
        for key in sorted(hash_map.keys()):
            new_list.append(hash_map[key])
        return " ".join(new_list)

