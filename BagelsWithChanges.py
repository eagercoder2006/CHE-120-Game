import random

NUM_DIGITS = 3
MAX_GUESS = 10

def getSecretNum():
    # Returns a string of unique random digits that is NUM_DIGITS long.
    numbers = list(range(10)) #IA: Creates a list of the range of 10.
    random.shuffle(numbers) #IA: Shuffles randomly the items of the list.
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i]) #IA: This is making the random number
    return secretNum

def getClues(guess, secretNum):
    # Returns a string with the Pico, Fermi, & Bagels clues to the user.
    if guess == secretNum: #IA: Verifies if the guess is exactly the secret number
        return print('You got it! (And ate, crunch crunch!)')

    clues = []
   #IA: Set up new variables that will point to the amount of proper guesses and of properly guessed numbers that were not in the right placement. I also made a lists that will contain respectively the rightly guessed numbers and the rightly guessed numbers that were in the wrong place. 
    proper_guess=0
    proper_number=0
    misplaced_guess=[]
    rightly_placed_guess=[]
    
    for i in range(len(guess)):
        if guess[i] == secretNum[i]: #IA: Verifies if the some of the numbers are in the same psoition in the actual secret number.
            clues.append('Fermi')#IA: Add Fermi to the list of clues
            proper_guess+=1 #IA: I added this to add 1 to the value stored in proper_gues when something is properly guess (position and value)
            rightly_placed_guess.append(guess[i]) #IA: updates the list rightly_placed with the value of the correcly guessed number. 
        elif guess[i] in secretNum: #IA: Verifies if the number guessed is in the secret number.
            clues.append('Pico') #IA: Add Pico to the list of clues
            proper_number+=1 #IA: I added this to add 1 to the value stored in proper_gues when something is properly guess (value only)
            misplaced_guess.append(guess[i]) #IA: updates the list misplaced_guess with the value of the number that was correcly guess but wrongly placed.
    if len(clues) == 0:
        return 'Bagels' #IA: This is part of the original code, it verifies if there are any clues given and if not, it prints "bagels"
    
    clues.sort()
    
    if proper_number>2 and proper_number<len(secretNum)-1:
        return print(' '.join(clues), "\nYou properly guessed ", proper_number, " numbers, but they are not in the right position.\n Here\'s a hint, the numbers are ", misplaced_guess) #IA: Give a little hint to the player when they have more than two correcly guessed numbers and less correctly guessed numbers than 1 minus the length of the secret number. Also prints the clues.
    
    return ' '.join(clues) #IA: If the above condition is not satisfied, the function just returns just the clues.

def isOnlyDigits(num):
    # Returns True if num is a string of only digits. Otherwise, returns False.
    if num == '': #IA: verifies if the string inputted is blank
        return False

    for i in num: #IA: verifies if all the items in the argument are numbers, this coulld have been done with the method .isnumeric().
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True


if __name__=="__main__":
    number_opinion=input("How wamny digits do you want there to be in the secret number (between 1 and 9)?") #IA: For a fun twist, we ask the player how many numbers they want to gueess (they can make the game easier or harder for themselves)
    if number_opinion.isnumeric(): #IA: This will verify if the entry is valid and if the number is too big, the amont of numbers will be the default 3.
        NUM_DIGITS=int(number_opinion)
        if NUM_DIGITS > 9 or NUM_DIGITS < 1:
            NUM_DIGITS=3
    print('I am thinking of a %s-digit number. Try to guess what it is.' % (NUM_DIGITS))
    print('The clues I give are...')
    print('When I say:    That means:')
    print('  Bagels       None of the digits is correct.')
    print('  Pico         One digit is correct but in the wrong position.')
    print('  Fermi        One digit is correct and in the right position.') #IA: Print the rules of the game.

    while True:
        secretNum = getSecretNum() #While the file is rune, there will be an obtention of the secret number.
        print('I have thought up a number. You have %s guesses to get it.' % (MAX_GUESS)) #IA: Prints a statement that presents the situation and the amount of numbers.

        guessesTaken = 1
        while guessesTaken <= MAX_GUESS: #IA: While loop that runs the game
            guess = ''
            while len(guess) != NUM_DIGITS or not isOnlyDigits(guess): #Verifies if the length of the guess is not the same as the length of the secret number or if it is not only digits.
                print('Guess #%s: ' % (guessesTaken)) #IA: Prints the guess message again
                guess = input() #IA: The guess is the input of the user

            print(getClues(guess, secretNum)) #IA: Prints what is returned when running the function getClues() with the guess and secret number as arguments.
            guessesTaken += 1
 
            if guess == secretNum:
                break #IA: This loop only breaks when the guess is correct
            if guessesTaken > MAX_GUESS:
                print('You ran out of guesses. The answer was %s.' % (secretNum)) #IA: verifies if the guesses are more than the allowed amount, and prints the answer.

        print('Do you want to play again? (yes or no)')
        if not input().lower().startswith('y'): #IA: verifies if the player wants to play again and the loop is broken if they do not write soemthing that starts with y.
            break