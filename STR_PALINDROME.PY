def palindrome(str):
    str = str[::-1]
    return(str)


string = input("Enter a string:")
str = palindrome(string)
if(string == str):
    print("It is a palindrome String")
else:
    print("It is not a palindrome String")
