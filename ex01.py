from random import randint


def guessing_game():
    guess_num = randint(0, 10)
    while True:
        guess = int(input('Input your guess:'))

        if guess > guess_num:
            print('A bit above')
        elif guess < guess_num:
            print('A bit below')
        else:
            print('Just right')
            break


guessing_game()
