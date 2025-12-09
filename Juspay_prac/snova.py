# class Solution:
#     def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
#         ans = 0
#         n = len(arr)
#         total = [0] * 1001
#         for j in range(n):
#             for k in range(j + 1, n):
#                 if abs(arr[j] - arr[k]) <= b:
#                     lj, rj = arr[j] - a, arr[j] + a
#                     lk, rk = arr[k] - c, arr[k] + c
#                     l = max(0, lj, lk)
#                     r = min(1000, rj, rk)
#                     if l <= r:
#                         ans += total[r] if l == 0 else total[r] - total[l - 1]
#             for k in range(arr[j], 1001):
#                 total[k] += 1

#         return ans

# def specialTriplets(self, A: List[int]) -> int:
#     n = len(A)
#     left, right = Counter(), Counter(A)
#     res = 0
#     for a in A:
#         right[a] -= 1
#         res += left[a * 2] * right[a * 2]
#         left[a] += 1
#     return res % (10 ** 9 + 7)


# class Solution(object):
#     def arithmeticTriplets(self, nums, diff):
#         """
#         :type nums: List[int]
#         :type diff: int
#         :rtype: int
#         """
#         count = 0
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 for k in range(j+1,len(nums)):
#                     if (nums[j] - nums[i]) == diff and (nums[k] - nums[j]) == diff:
#                         count += 1
#         return count

def minimumMountainTriplets(nums):
    n = len(nums)
    smallest_sum = float('inf')  # Track the smallest sum found
    
    # Try each number as the peak (middle of the mountain)
    for j in range(1, n-1):  # Skip first and last since they can't be peaks
        peak = nums[j]
        
        # Look for a smaller number on the left
        has_left = False
        for i in range(j):
            if nums[i] < peak:
                has_left = True
                break
        
        # Look for a smaller number on the right
        has_right = False
        for k in range(j+1, n):
            if nums[k] < peak:
                has_right = True
                break
        
        # If we found smaller numbers on both sides, we have a mountain
        if has_left and has_right:
            # Find the smallest number on the left that's less than peak
            smallest_left = min(nums[i] for i in range(j) if nums[i] < peak)
            # Find the smallest number on the right that's less than peak
            smallest_right = min(nums[k] for k in range(j+1, n) if nums[k] < peak)
            # Calculate the sum of this triplet
            current_sum = smallest_left + peak + smallest_right
            # Update smallest sum if this one is smaller
            smallest_sum = min(smallest_sum, current_sum)
    
    # If we found a valid sum, return it; otherwise, return -1
    return smallest_sum if smallest_sum != float('inf') else -1


print(minimumMountainTriplets([8,1,3,2]))