#Reverse a string (without slicing [::-1])
def rev_string():
    str = "Akshata"
    rev_str = ""
    for i in range(len(str)-1, -1, -1):
        rev_str += str[i]
    print(rev_str)
#rev_string()

#Check if string is palindrome
def palindrome():
    str = "MADAMM"
    org_str = str
    rev_str = ""
    for i in range(len(str)-1, -1, -1):
        rev_str += str[i]
    if(org_str == rev_str):
        print("Palindrome")
    else:
        print("Not palindrome")
#palindrome()

#Count vowels and consonants
def vowel_consonants():
    s = "Akshata"
    vowels = 0
    consonants = 0

    for ch in s.lower():
        if ch.isalpha():
            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1
    print("Vowels", vowels)
    print("Consonents", consonants)
#vowel_consonants()

#Count frequency of each character
def frequency():
    s = "Akshata".lower()
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] =1
    print(freq)
#frequency()

#Remove spaces from string
def remove_spaces():
    s = "A k s h a t a"
    str = ""
    for ch in s:
        if ch!=" ":
            str += ch
    print(str)
#remove_spaces()

#Strings are anagrams or not

def anagrams():
    s1 = "silent"
    s2 = "listenn"
    if sorted(s1) == sorted(s2):
        print("Anagrams")
    else:
        print("Not anagrams")
anagrams()