class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        registry: dict[str, list[str]] = defaultdict(list)
        for word in strs:
            key: str = "".join(sorted(word))
            registry[key].append(word)
        return list(registry.values())
