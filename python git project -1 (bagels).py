import random as r

#printing basic rule

print('''I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.
I have thought up a number.
 You have 10 guesses to get it.''')

#geting a velue to guess

a=str(r.randint(100,999))
print("game is started guess the number of 3 digit")

#getting result of guess
    
def result(guess,a):
    if guess == a:
        return 'You got it!'

    clues = []

    for i in range(3):
        temp=str(guess)
        if temp[i] == a[i]:
            clues.append('Fermi')
        elif temp[i] in a:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels' 
    else:
        clues.sort()
        return ' '.join(clues)


#setting max guess

MAX_GUESSES=10

#main program of the game

while True: 
    print('I have thought up a number.')
    print(' You have 10 guesses to get it.')
    numGuesses = 1
    while numGuesses <= MAX_GUESSES:
        
        guess = int(input('guess'))

        clues = result(guess, a)
        print(clues)
        numGuesses += 1

        if guess == a:
            break
        elif numGuesses > MAX_GUESSES:
            print('You ran out of guesses.')
            print('The answer was .',a)

    #checking if user want to continu

    restart=input("do you want to continu (y/n)")
    if restart.lower()==n:
        break

