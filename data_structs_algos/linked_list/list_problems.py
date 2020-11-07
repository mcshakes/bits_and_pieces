from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left_pointer = 0
        right_pointer = len(height) - 1

        for idx in range(len(height)):
            width = abs(right_pointer - left_pointer)

            if height[left_pointer] < height[right_pointer]:
                poss_water = width * height[left_pointer]
                left_pointer += 1
            else:
                poss_water = width * height[right_pointer]
                right_pointer -= 1

            if poss_water > max_area:
                max_area = poss_water

        return max_area


my_input = [1, 8, 6, 2, 5, 4, 8, 3, 7]

sol = Solution()
sol.maxArea(my_input)


# need to multiply the largest constraints
