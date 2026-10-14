class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary1 = {}
        dictionary2 = {}

        if len(s) != len(t):
            return False
        else:
            for i in s:
                if i not in dictionary1:
                    dictionary1[i] = 1
                    dictionary2[i] = 0
                else:
                    dictionary1[i] += 1

            for i in t:
                if i in dictionary2:
                    dictionary2[i] += 1
                else:
                    return False
            print(dictionary1)
            print(dictionary2)
            return dictionary1 == dictionary2


