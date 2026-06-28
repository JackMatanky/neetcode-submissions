class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area: int = 0

        stack: list[tuple[int, int]] = []
        for i, h in enumerate(heights):
            start_index: int = i
            while stack and stack[-1][-1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start_index = index
            stack.append((start_index, h))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area
