class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}

        for i in strs:
            if tuple(sorted(i)) not in dictionary:
                dictionary[tuple(sorted(i))] = []
            dictionary[tuple(sorted(i))].append(i)

        return list(dictionary.values())