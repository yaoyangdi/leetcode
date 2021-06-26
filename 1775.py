# 1775. Equal Sum Arrays With Minimum Number of Operations
from queue import PriorityQueue
from typing import List

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        max = 6
        min = 1
        operations = 0
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        diffs = abs(sum1-sum2)

        # define lists with larger sum and smaller sum
        if (sum1>sum2):
            larger_list = nums1
            smaller = nums2
        else:
            larger_list = nums2
            smaller = nums1

        comp = sorted([x-min for x in larger_list]+[max-x for x in smaller], reverse=True)  # the list for compensating diffs
        for i in range(len(comp)):
            if(diffs>0):
                diffs -= comp[i]
                operations+=1

        if diffs>0:
            return -1
        else:
            return operations