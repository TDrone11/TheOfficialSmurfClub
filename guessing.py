score = 0
import random

while True:
    flag = True
    while flag:
        num = input('Type the max number!: ')
        
        if num.isdigit() :
            print('Let it start then!')
            num = int(num)
            flag = False
        else:
            print('Please enter a NUMBER ')
            
    secret = random.randint(1,num)

    guess = None
    count = 1 

    while guess != secret:
        guess = input('Please type a number between 1 and ' + str(num) + " : ")
        if guess.isdigit():
            guess = int(guess)
            
        if guess == secret:
            print("Nice job you get a point!")
            print(score + 1)
        else:
            print("Try again!")
            count += 1
            
    print("It took you ", count, " try's")