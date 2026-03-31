#2840. Check if Strings Can be Made Equal With Operations II
#Medium

#You are given two strings s1 and s2, both of length n, consisting of lowercase English letters.
#You can apply the following operation on any of the two strings any number of times:
#Choose any two indices i and j such that i < j and the difference j - i is even, then swap the two 
#characters at those indices in the string.
#Return true if you can make the strings s1 and s2 equal, and false otherwise.


#This function is checking both even and odd indcies between s1 and s2 in order to determine 
#whether the combination of the letters are the same therefore they can be swithced 
def check_strings(s1,s2):
    return (sorted(s1[::2]) == sorted(s2[::2]) and sorted(s1[1::2]) == sorted(s2[1::2]))


#This the main function that tests the different examples from leetcode
#and prints the results
def main():
    s1 = 'abcdba'
    s2 = 'cabdab'
    print(check_strings(s1,s2))


    return 


if __name__ == '__main__':
    main()