#1894. Find the Student that Will Replace the Chalk
#Medium

#There are n students in a class numbered from 0 to n - 1.
#The teacher will give each student a problem starting with the student number 0,
#then the student number 1, and so on until the teacher reaches the student number n - 1.
# After that, the teacher will restart the process, starting with the student number 0 again.

#You are given a 0-indexed integer array chalk and an integer k.
#There are initially k pieces of chalk. When the student number i is given a problem to solve,
#they will use chalk[i] pieces of chalk to solve that problem.
#However, if the current number of chalk pieces is strictly less than chalk[i], then the student
#number i will be asked to replace the chalk.
#Return the index of the student that will replace the chalk pieces.


#This function takes the modulo of k and the sum of the chalk list in order to find the remaineder
#because that would indicate a new cycle has started at student zero.
#Then if k is less than the value of chalk[i] that would indicate that particular student 
#would need to refill the chalk otherwise subtract that value from k and go to the next student.
def Chalk_replacer(chalk, k):
    total = sum(chalk)

    k %= total
    for i in range(len(chalk)):
        if k < chalk[i]:
            return i
        else:
            k -= chalk[i]
    return


#This the main function that tests the different examples from leetcode
#and prints the results
def main():
    chalk = [5,1,5]
    k = 22
    print(Chalk_replacer(chalk, k))

    chalk2 = [3,4,1,2]
    k2 = 25
    print(Chalk_replacer(chalk2, k2))
    return


if __name__ == '__main__':
    main()