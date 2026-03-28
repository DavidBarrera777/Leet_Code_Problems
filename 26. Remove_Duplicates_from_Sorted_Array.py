#26. Remove Duplicates from Sorted Array
#Easy

#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place
#such that each unique element appears only once. The relative order of the elements should 
#be kept the same.
#Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, 
#return the number of unique elements k.
#The first k elements of nums should contain the unique numbers in sorted order. 
#The remaining elements beyond index k - 1 can be ignored.


#This array the nums array and vraverses through it and checks the two elements next to each other
#are not duplicates then it traverses to the next iteration
#If the numbers are duplicates it makes that number equal to the next number which be a no duplicate 
def remove_duplicates(nums):

    k = 1
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            nums[k] = nums[i]
            k+=1

    return k




#This the main function that tests the different examples from leetcode
#and prints the results
def main():
    nums = [1,1,2]
    print(remove_duplicates(nums))
    return 



if __name__ == '__main__':
    main()