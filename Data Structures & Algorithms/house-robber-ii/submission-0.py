class Solution:

  def rob(self, nums: list[int]) -> int:
    if len(nums) == 1:
      return nums[0]

    # Helper function from House Robber I
    def rob_linear(houses: list[int]) -> int:
      p1, p2 = 0, 0
      for num in houses:
        p1, p2 = p2, max(p2, p1 + num)
      return p2

    # Return max of (excluding last house) vs (excluding first house)
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))