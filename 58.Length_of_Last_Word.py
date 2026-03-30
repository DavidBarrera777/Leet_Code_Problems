#58. Length of Last Word
#Easy

#Given a string s consisting of words and spaces, return the length of the last word in the string.
#A word is a maximal substring consisting of non-space characters only.





#This function reverses the string strips the string of any outer spaces and then traverses through
#reversed string until it hits a space and returns the length of that string
#If the string has no spaces, it will just return the lenght of the string
def length_of_last_word(s):
    reverse_word = s[::-1]
    output = []
    reverse_word = reverse_word.lstrip()
    if ' ' not in reverse_word:
        return len(reverse_word)
    for i in range(len(reverse_word)):
        if reverse_word[i] == ' ':
            return len(output)
        output.append(reverse_word[i])



#This the main function that tests the different examples from leetcode
#and prints the results
def main():
    s = 'Hello World'
    print(length_of_last_word(s))

    s2 = '   fly me   to   the moon  '
    print(length_of_last_word(s2))

    s3 = "luffy is still joyboy"
    print(length_of_last_word(s3))

    s4 = 'day'
    print(length_of_last_word(s4))

    return

if __name__ == '__main__':
    main()