class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        registry: dict[str, list[str]] = dict()
        for s in strs:
            sorted_str: str = str(sorted(s))
            if sorted_str not in registry:
                registry[sorted_str] = [s]
            else:
                registry[sorted_str].append(s)

        return list(registry.values())
        