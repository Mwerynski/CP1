import random
roll = (int((random.uniform(1, 7))))
#print(roll) #test
guess = int(input())
if guess == roll:
    print("True")
else: 
    print("False")