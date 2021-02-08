# this simple script shows a guessing game of the secrete word!

def guessing_game():
    trial = 3
    guess_count = 0
    secrete_word = 'open sesame'
    while guess_count < trial:
        guess = input("Tell me the secret word to open the cave: ")
        guess_count += 1
        if guess == secrete_word:
            print("The cave is opened !!!")
            break
        else:
            if trial -guess_count == 2:
                print("Wrong secret word! you have {} trial  more".format(trial -guess_count))
            elif trial -guess_count == 1:
                print("Wrong secret word! you have only {} trial more".format(trial -guess_count))
            else:
                print('You are not permitted anymore to enter the cave !!!')

guessing_game()