#Given an array of integers nums and an integer target, return indices of the two
# numbers such that they add up to target.You may assume that each input would have
# exactly one solution, and you may not use the same element twice.You can return
# the answer in any order.Example 1:
#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
class TwoSum:
    def two_Sum(self,nums,target):
        dictionary = {}
        for idx,element in enumerate(nums):
            complement = target-element;
            if(complement in dictionary):
                return [dictionary[complement],idx]
            dictionary[element] = idx
if __name__=="__main__":
    sum = TwoSum()
    z= sum.two_Sum([1,3,4,9],7)
    for i in z:
        print(i)