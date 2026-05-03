# TWO SUM

# Brute force: O(n^2)Problem statement:
#     Given an array of integers `nums` and an integer `target`,
#     return indices of the two numbers that add up to target.
#     Exactly one solution exists. You may not use the same element twice.

# Example:
#     Input:  nums = [2, 7, 11, 15], target = 9
#     Output: [0, 1]  because nums[0] + nums[1] = 2 + 7 = 9
# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
    

# Hash map: O(n)
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

# ── Tests (run with: python solution.py) ───────────────────
if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    print("All tests passed.")