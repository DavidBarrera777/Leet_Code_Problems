def smallestNumber(n):

        for x in range(n, 100):
            binary_digits =  bin(x)[2:]

            if all(y == '1' for y in binary_digits):

                return x



n=10
print(smallestNumber(n))