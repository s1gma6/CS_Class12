nums = int(input("Enter a num:"))
tmp = nums
rev = 0
while(nums > 0):
    d = nums % 10
    rev = rev*10+d
    nums = nums//10
if(tmp == rev):
    print("It is a Palindrome ")
else:
    print("It is not a Palindrome ")
