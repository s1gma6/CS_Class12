num = int(input("Enter a num:"))
t = num
reverse = 0
while(num > 0):
    d = num % 10
    reverse = reverse*10+d
    num = num//10
if(t == reverse):
    print("It is a Palindrome Number")
else:
    print("It isn't a Palindrome number")
