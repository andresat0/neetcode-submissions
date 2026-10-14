class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        sorted_strs = []
        for index, i in enumerate(strs):
            if tuple(sorted(i)) not in dictionary:
                dictionary[tuple(sorted(i))] = []
            dictionary[tuple(sorted(i))].append(strs[index])
        for i in dictionary.values():
            sorted_strs.append(i)
        return sorted_strs