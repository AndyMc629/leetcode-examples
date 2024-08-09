class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # V1
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i==j:
        #             pass
        #         elif nums[i]+nums[j]==target:
        #             return [i,j]
        # for i in range(len(nums)):
        #     for j in nums[i::]:
        #         if target-nums[j]==0:
        #             return [i,j]
        #V2 - didn't work
        #scaled_nums = target-nums
        # This happens in place ...
        # sorted_nums = nums.copy()
        # sorted_nums.sort()
        # #nums is sorted!
        # scaled_sorted_nums = [target - x for x in sorted_nums]
        # # for i in range(len(nums)):
        # #     for j in range(i,len(nums)):
        # #         if nums[j]==scaled_sorted_nums[i]:
        # #             return [i,j]
        # for i in range(len(sorted_nums)):
        #     for j in range(i, len(sorted_nums)):
        #         x = sorted_nums[i]
        #         y = sorted_nums[j]
        #         if x+y==target:
        #             values = [x,y]
        # indices = []
        # for i in range(len(nums)):
        #     if nums[i] == values[0] or nums[i] == values[1]:
        #         indices.append(i)
        # indices.sort()
        # return indices
        #V3 - works but is slow (48ms vs 21ms for brute force)
        #first pointer
        # i = 0
        # #second pointer
        # j = len(nums)-1
        # # This happens in place ...
        # sorted_nums = nums.copy()
        # sorted_nums.sort()
        # sorted_indices = None
        # sorted_values = None
        # while i<j:
        #     #If we have the pair 
        #     if sorted_nums[i] + sorted_nums[j] == target:
        #         sorted_indices = [i,j]
        #         sorted_values = [sorted_nums[i], sorted_nums[j]]
        #         break
        #     # if sum is less, move left pointer upwards
        #     elif sorted_nums[i] + sorted_nums[j] < target:
        #         i += 1 
        #     # if sum is greater, move right pointer downwards
        #     else:
        #         j -= 1
            
        # # find the unsorted number locations
        # result = []
        # for i in range(len(nums)):
        #     if nums[i]==sorted_values[0]:
        #         result.append(i)
        #         break
        # for j in range(len(nums)):
        #     if nums[j]==sorted_values[1] and j!=result[0]:
        #         result.append(j)
        # return result
        # V4 - Hash table (dict) --> runs in 49ms
        seen = {}
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[nums[i]] = i
