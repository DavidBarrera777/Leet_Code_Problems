#2465. Number of Distinct Averages
#Easy

#You are given a 0-indexed integer array nums of even length.
#As long as nums is not empty, you must repetitively:
#Find the minimum number in nums and remove it.
#Find the maximum number in nums and remove it.
#Calculate the average of the two removed numbers.
#The average of two numbers a and b is (a + b) / 2.
#For example, the average of 2 and 3 is (2 + 3) / 2 = 2.5.
#Return the number of distinct averages calculated using the above process.
#Note that when there is a tie for a minimum or maximum number, any can be removed.


#This function does exactly what description specifies
#It takes the max and mins gets the average and adds the average to a list then remove the min and max
#Then once the list is empty, it checks the output list turns it into a set to remove duplicates, then
#back into a list then it gets the length of that list and stores it in a variable and returns that variable 
def distinct_averages(nums):
    output = []
    while nums:
        min_num = min(nums)
        max_num = max(nums)
        average = (min_num + max_num)/2
        output.append(average)
        nums.remove(min_num)
        nums.remove(max_num)
    
    actual_output = len(list(set(output)))
    return actual_output



#This the main function that tests the different examples from leetcode
#and prints the results
def main():
    nums = [4,1,4,0,3,5]
    print(distinct_averages(nums))

    nums2 = [1,100]
    print(distinct_averages(nums2))


    return 

if __name__ == '__main__':
    main()