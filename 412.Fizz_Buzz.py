#412. Fizz Buzz
#Easy

#Given an integer n, return a string array answer (1-indexed) where:
#answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#answer[i] == "Fizz" if i is divisible by 3.
#answer[i] == "Buzz" if i is divisible by 5.
#answer[i] == i (as a string) if none of the above conditions are true.


#This the function that runs all the logic
#It does exactly what the problem wants by checking if each 
#number is divisible by a certain number and appending that string to a list
#It check if its divisible by using modulo and checking if it has a remainder
def fizzBuzz(n):
    output = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            output.append('FizzBuzz')
        elif i % 3 == 0:
            output.append('Fizz')
        elif i % 5 == 0:
            output.append('Buzz')
        else:
            output.append(str(i)) 

    return output


#This the main function that runs the examples that are on leetcode
def main():
    n = 3
    print(fizzBuzz(n))

    n2 = 5
    print(fizzBuzz(n2))

    n3 = 15
    print(fizzBuzz(n3))
    return




if __name__ == '__main__':
    main()