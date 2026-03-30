#Plus One
#Easy 

#You are given a large integer represented as an integer array digits, where each digits[i] is the
#ith digit of the integer. The digits are ordered from most significant to least significant in 
#left-to-right order. The large integer does not contain any leading 0's.
#Increment the large integer by one and return the resulting array of digits.


#This function turns the digits list into a single string then that combined string into a int and add 1
#Then traverse through the string of the int in order to add it back to a list then returns the list
def plus_one(digits):
    output = []
    single_number =int(''.join(map(str,digits)))+1
    for i in str(single_number):
        output.append(int(i))

    return output


#This the main function that tests the different examples from leetcode
#and prints the results
def main():
    digits = [1,2,3]
    print(plus_one(digits))

    digits2 = [4,3,2,1]
    print(plus_one(digits2))

    digits3 = [9]
    print(plus_one(digits3))
    return 

if __name__ == '__main__':
    main()