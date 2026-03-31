#Mock Interview Question #1
#Given an array of distinct integers arr, find all pairs of elements with the minimum absolute 
#difference of any two elements.
#Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
#a, b are from arr
#a < b
#b - a equals to the minimum absolute difference of any two elements in arr




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


def main():
    arr = [4,2,1,3]
    print(minimumAbsDifference(arr))


    return 




if __name__ == '__main__':
    main()