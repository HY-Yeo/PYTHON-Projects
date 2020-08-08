import random

print('H A N G M A N')
play_game = input('Type "play" to play the game, "exit" to quit: ')

while play_game == 'play':
    # create the word list
    word_list = ['python', 'java', 'kotlin', 'javascript']

    # ASCII lowercase alphabet letters
    lowercase_ASCII_alphabets = 'abcdefghijklmnopqrstuvwxyz'

    # store the variable that the user typed
    typed_letter = []

    # choose a word from the list randomly
    randomise_word = random.choice(word_list)
    # print(randomise_word)

    # total num of attempts for the game
    attempts = 8

    # length of randomised word converted to hyphens
    hyphen_str = '-' * len(randomise_word)

    # while loop for the number of tries
    while attempts > 0:
        # check if the word is guessed correctly
        if hyphen_str == randomise_word:
            break
        print()  # formatting
        print(hyphen_str)
        letter = input('Input a letter: ')
        # update list with the letter for checking
        typed_letter.append(letter)

        # corner case 1: check if user printed exactly one letter
        if len(letter) != 1:
            print('You should input a single letter')
            continue  # move on to the next iteration
        # corner case 2: check if user prints an English lowercase letter or not
        elif letter not in lowercase_ASCII_alphabets:
            print('It is not an ASCII lowercase letter')
            continue  # move on to the next iteration
        # corner case 3: check if user enters the same letter twice
        elif typed_letter.count(letter) > 1:
            print('You already typed this letter')
            continue  # move on to the next iteration

        # from here -> letter is not used before
        # check if letter is found in the word but not used before
        if letter in randomise_word:
            for index in range(len(randomise_word)):
                if letter == randomise_word[index]:  # replace the hyphen at the index with the letter
                    hyphen_str = hyphen_str[:index] + letter + hyphen_str[index+1:]
        # letter is not in the word
        else:
            print('No such letter in the word')
            attempts -= 1

    # test using the num of attempts left
    if attempts > 0:  # break off while loop with at least 1 attempt left
        print('You guessed the word ' + randomise_word + '!')
        print('You survived!')
    else:  # use up all the attempts
        if hyphen_str == randomise_word:
            print('You guessed the word ' + randomise_word + '!')
            print('You survived!')
        else:
            print('You are hanged!')

    print()  # formatting
    # update while loop to continue or end game
    play_game = input('Type "play" to play the game, "exit" to quit: ')
