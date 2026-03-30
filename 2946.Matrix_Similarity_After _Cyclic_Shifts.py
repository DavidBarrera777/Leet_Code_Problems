#rgba(22, 233, 82, 0.4), Matrix Similarity After Cyclic Shifts
#Easy

#You are given an m x n integer matrix mat and an integer k. 
#The matrix rows are 0-indexed.
#The following proccess happens k times:
#Even-indexed rows (0, 2, 4, ...) are cyclically shifted to the left.
#Odd-indexed rows (1, 3, 5, ...) are cyclically shifted to the right.
#Return true if the final modified matrix after k steps is identical to the original matrix, 
#and false otherwise.


#This function loops through the first list and goes within that list and tests if the individual 
#elements are in the same place after they have been looped.
#To prevent a false positive where the numbers are the same but not in the same position, I test the
#element next to them as well to make sure they are in the correct postion 
def are_similar(mat, k):

    for i in range(len(mat)):
        if len(mat[i]) == 1:
                return True
                break
        else:
            first_number = mat[i][0]
            second_element = mat[i][1]
            for n in range(k+1):
                index = n % len(mat[i])
                last_number = mat[i][index]
                index2 = (n+1) % len(mat[i])
                next_last_element = mat[i][index2]


    if first_number == last_number and second_element == next_last_element:
        return True
    else:
        return False
        




#This the main function that tests the different examples from leetcode
#and prints the results
def main():
    mat = [[2,2],[4,5],[3,2],[4,6],[1,9],[5,3],[3,5],[2,4],[3,9]]
    k = 7
    print(are_similar(mat,k))

    mat2 = [[1,2,3],[4,5,6],[7,8,9]]
    k2 = 4
    print(are_similar(mat2,k2))

    mat3 = [[1,2,1,2],[5,5,5,5],[6,3,6,3]]
    k3 = 2
    print(are_similar(mat3, k3))

    mat4 = [[2,2],[2,2]]
    k4 = 3
    print(are_similar(mat4, k4))


    return 

if __name__ == '__main__':
    main()

