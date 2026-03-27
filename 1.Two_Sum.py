#1. Two Sum
#Easy

#Given an array of integers nums and an integer target, 
#return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, 
#and you may not use the same element twice.
#You can return the answer in any order.




#This function takes the list nums and int target
#The dictionary num_map holds each value of nums as the key and the index of ecach value as a value
#Then get the complement which would be the value that is needed to be found from subtracting a 
#number from nums and if that value exists in the nums list it is the second value needed
#Then the i and value from where complement is in is returned as a list 
def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        num_map[num] = i

    for i , num in enumerate(nums):
        complement = target - num
        if complement in nums and num_map[complement] != i:
            return [i, num_map[complement]]
    return []



#This the main function that tests the different examples from leetcode
#and prints the results
def main():
    nums = [2,7,11,15]
    target = 9
    print(two_sum(nums, target))

    nums2 = [3,2,4]
    target2 = 6
    print(two_sum(nums2, target2))

    nums3 = [3,3]
    target3 = 6
    print(two_sum(nums3, target3))
    return



if __name__ == '__main__':
    main()