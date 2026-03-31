#2839. Check if Strings Can be Made Equal With Operations I
#Easy 

#You are given two strings s1 and s2, both of length 4, consisting of lowercase English letters.
#You can apply the following operation on any of the two strings any number of times:
#Choose any two indices i and j such that j - i = 2, then swap the two characters at those indices
#in the string.
#Return true if you can make the strings s1 and s2 equal, and false otherwise.


#This function compares the indicies at a specific location to see if they are the same despite 
#the order in which they are swapped
def can_be_equal(s1, s2):
    return (sorted([s1[0], s1[2]]) == sorted([s2[0], s2[2]]) and
                sorted([s1[1], s1[3]]) == sorted([s2[1], s2[3]]))



#This the main function that tests the different examples from leetcode
#and prints the results
def main():
    s1 = 'abcd'
    s2 = 'cdab'
    print(can_be_equal(s1,s2))

    s1_2 = 'abcd'
    s2_2 = 'dacb'
    print(can_be_equal(s1_2,s2_2))
    return 



if __name__ == '__main__':
    main()