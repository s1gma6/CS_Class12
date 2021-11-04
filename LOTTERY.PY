from random import randint
user = randint(1, 6)
lottery = randint(1, 6)
print(user)
print(lottery)
if(user == lottery):
    print("You have won the lottery")
else:
    print("Lottery Lost, Please Try Again Later")
