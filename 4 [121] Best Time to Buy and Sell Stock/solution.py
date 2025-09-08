# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Input: prices = [7,1,5,3,6,4]
# Output: 5


class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        min_value = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            profit = prices[i] - min_value
            if prices[i] < min_value:
                min_value = prices[i]
            if profit > max_profit:
                max_profit = profit
        return max_profit


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit([7, 6, 4, 3, 1]))
print(s.maxProfit([1, 7, 2, 8]))
