#Mock Interview Question #1
#Given an array of distinct integers arr, find all pairs of elements with the minimum absolute 
#difference of any two elements.
#Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
#a, b are from arr
#a < b
#b - a equals to the minimum absolute difference of any two elements in arr



#This function first sorts the list arr then traverses through it looking for the minimum difference
#between the elements in the list
#Then it travarses through the list and compares each element pair to see if it is equal to the 
#minimum difference and if it is it adds to elements to the output array
#Once the list is fully traversed, it returns the output array
def minimumAbsDifference(arr):
    arr.sort()
        
    min_diff = float('inf')
    result = []
    
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i-1]
        min_diff = min(min_diff, diff)
                    
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] == min_diff:
            result.append([arr[i-1], arr[i]])
        
    return result 



#This the main function that tests the different examples from leetcode
#and prints the results
def main():
    arr = [4,2,1,3]
    print(minimumAbsDifference(arr))


    return 




if __name__ == '__main__':
    main()