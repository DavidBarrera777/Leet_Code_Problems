#9. Palindrome Number
#Easy
#Given an integer x, return true if x is a palindrome, and false otherwise.


#This function takes the int as x and converts it into a string 
#Then the value is reversed and stored in reversed_string_value
#The the values are compared
#If they are the same, True is returned otherwise False is returned
def isPalindrome(x):
    string_value = str(x)
    reversed_string_value = string_value[::-1]

    if string_value == reversed_string_value:
        return True
    else:
        return False


#This the main function that tests the different examples from leetcode
#and prints the results
def main():
    x = 121
    print(isPalindrome(x))

    y = -121
    print(isPalindrome(y))

    z = 10
    print(isPalindrome(z))
    return



if __name__ == '__main__':
    main()