#28. Find the Index of the First Occurrence in a String
#Easy

#Given two strings needle and haystack, return the index of the first occurrence of needle in
#haystack, or -1 if needle is not part of haystack.


#Just return the index if found and -1 if not found
def str_str(haystack, needle):
        return haystack.find(needle)


#This the main function that tests the different examples from leetcode
#and prints the results
def main():
    haystack = 'sadbutsad'
    needle = 'sad'

    print(str_str(haystack, needle))

    haystack2 = 'leetcode'
    needle2 = 'leeto'
    print(str_str(haystack2, needle2))

    return

if __name__ == '__main__':
    main()