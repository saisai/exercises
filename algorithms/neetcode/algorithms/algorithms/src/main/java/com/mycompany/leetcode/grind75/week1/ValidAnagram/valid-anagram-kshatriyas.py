
class S:

    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        return sorted_s == sorted_t


s = "anagram"
t = "nagaram"
print(S().isAnagram(s, t))
