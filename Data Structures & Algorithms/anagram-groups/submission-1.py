class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        registry: dict[str, list[str]] = {}
        for word in strs:
            key: str = "".join(sorted(word))
            if key not in registry:
                registry[key] = []
            
            registry[key].append(word)

        return list(registry.values())
        