class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        short_str=min(strs)

        for i, char in enumerate(short_str):
            for sub_str in strs:
                if sub_str[i]!=char:
                    return short_str[:i]

        return short_str

        