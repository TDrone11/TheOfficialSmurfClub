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
    points = 0
    
    while guess != secret:
        guess = input('Please type a number between 1 and ' + str(num) + " : ")
        if guess.isdigit():
            guess = int(guess)
        if guess == secret:
            points += 1
            if num >= 10:
                points += 1
            if num >= 25:
                points += 2
            if num >= 50:
                points += 5
            if count <= 5:
                points += 1
            print("Nice job you get ", points, " points!")
        if guess > secret:
            print("Lower")
        if guess < secret:
            print("Higher")
        if guess != secret:
            print("Tries: ", count)
            count += 1
    print("It took you", count, "try's")
    score += points
    print("Current Score = ",points,)