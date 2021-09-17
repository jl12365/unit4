import random

def is_correct(guess,answer):
    return guess == answer

def check_guess(guess,answer):
    return abs(guess - answer)

def main(): 
    answer=random.randint(1,10)
    guess=int(input('Guess a number: '))
    result = check_guess(guess,answer)

    if result == 0:
        print('You are correct!')
    else:
        print('You were', result, 'away!')

if __name__ == "__main__":
    main()





