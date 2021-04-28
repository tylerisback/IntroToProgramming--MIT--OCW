# Problem Set 2, hangman.py
# Name: Emre
# Collaborators:
# Time spent: Some good time

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid  words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    for char in secret_word:
        if char not in letters_guessed:
            return False
        
    return True
            
        



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    new_word = ''
    for i in secret_word:
        new_word = new_word + i + ' '
    

    for j in secret_word:
        if j not in letters_guessed:
            new_word = new_word.replace(j, '_')
            
    return new_word
    



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    all_letters = string.ascii_lowercase
    for char in letters_guessed:
        if char in all_letters:
            all_letters = all_letters.replace(char, '')
            
    return all_letters
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    num_of_guess = 6
    av_letters = string.ascii_lowercase
    letters_guessed = []
    num_of_warnings = 3
    
    print('Welcome Beril, to the game of Hangman!')
    print('They say you are very proficient in Turkish version, Kelimelik. Hope you do great in this one as well!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    print('You have', num_of_warnings, 'left.' )
    print('----------------------------')
    
    
   
    
    while (num_of_guess != 0) and (num_of_warnings != 0) and not (is_word_guessed(secret_word, letters_guessed)): 
    
        print('You have', num_of_guess, ' guesses left')
        print('Available letters:', av_letters)
        
        print('Please guess a letter: ' , get_guessed_word(secret_word,letters_guessed), end = '    ' )
        user_input = input()
        av_letters = get_available_letters(letters_guessed)
        
        
        if (user_input in secret_word) and  (user_input not in letters_guessed):
            print('Good Guess:', get_guessed_word(secret_word,letters_guessed))
            
            
        elif (user_input in letters_guessed):
            num_of_warnings -= 1
            print('Opps! You have already guessed that letter. You have', num_of_warnings , 'warnings left.')
        
        elif user_input not in string.ascii_lowercase:
            num_of_warnings -= 1
            print('Oops! That letter is not a valid letter. You have', num_of_warnings, 'left.')
        
        else:
            num_of_guess -= 1
            print('Opps! that letter is not in my word.', )
            
        letters_guessed.append(user_input) 
        
        if (is_word_guessed(secret_word, letters_guessed)):
            print('Congrutalations, You correctly find the correct word: ', secret_word)
        
        if (num_of_guess == 0) and not (is_word_guessed(secret_word, letters_guessed)):
            print('You have no guess left and you could not found the word.', 'It was', secret_word, '.' )

        elif (num_of_guess == 0) and (is_word_guessed(secret_word, letters_guessed)):
            print('You correctly guessed the correct word:', secret_word)
        
        if num_of_warnings == 0:
            print('You are out of warnings. Please try again later.')
        print('----------------------------')
        print('\n')
            

    


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(' ', '' )
    count_letters = []
    if len(my_word) != len(other_word):
        return False
    elif len(my_word) == len(other_word):
        for i in range(len(my_word)):
            if my_word[i] == '_':
                continue
            elif my_word[i] != other_word[i]:
                return False
            else:
                count_letters.append(other_word[i])
                
        for i in range(len(my_word)):
            if my_word[i] == '_':
                if other_word[i] in count_letters:
                    return False
            
        return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    matching_words = []
    for word in wordlist:
        if match_with_gaps(my_word, word) == True:
            matching_words.append(word)
        
    if len(matching_words) < 1:
        print('No matches found')
        
    else:
        separator = ', '
        print(separator.join(matching_words))



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    num_of_guess = 6
    av_letters = string.ascii_lowercase
    letters_guessed = []
    num_of_warnings = 3
    
    print('Welcome Beril, to the game of Hangman!')
    print('They say you are very proficient in Turkish version, Kelimelik. Hope you do great in this one as well!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    print('You have', num_of_warnings, 'left.' )
    print('----------------------------')
    
    
   
    
    while (num_of_guess != 0) and (num_of_warnings != 0) and not (is_word_guessed(secret_word, letters_guessed)): 
        av_letters = get_available_letters(letters_guessed)
        print('You have', num_of_guess, ' guesses left')
        print('Available letters:', av_letters)
        
        print('Please guess a letter: ' , get_guessed_word(secret_word,letters_guessed), end = '    ' )
        user_input = input()
        #av_letters = get_available_letters(letters_guessed)
        
        if user_input == '*':
            show_possible_matches(get_guessed_word(secret_word,letters_guessed))
        else:


            if (user_input in secret_word) and  (user_input not in letters_guessed):
                letters_guessed.append(user_input)
                print('Good Guess:', get_guessed_word(secret_word,letters_guessed))
                
                
            elif (user_input in letters_guessed):
                num_of_warnings -= 1
                print('Opps! You have already guessed that letter. You have', num_of_warnings , 'warnings left.')
                letters_guessed.append(user_input)

            elif user_input not in string.ascii_lowercase:
                num_of_warnings -= 1
                print('Oops! That letter is not a valid letter. You have', num_of_warnings, 'left.')
                letters_guessed.append(user_input)

            else:
                num_of_guess -= 1
                print('Opps! that letter is not in my word.', )
                letters_guessed.append(user_input)

            
            if (is_word_guessed(secret_word, letters_guessed)):
                print('Congrutalations, You correctly find the correct word: ', secret_word)
            
            if (num_of_guess == 0) and not (is_word_guessed(secret_word, letters_guessed)):
                print('You have no guess left and you could not found the word.', 'It was', secret_word, '.' )

            elif (num_of_guess == 0) and (is_word_guessed(secret_word, letters_guessed)):
                print('You correctly guessed the correct word:', secret_word)
            
            if num_of_warnings == 0:
                print('You are out of warnings. Please try again later.')
            print('----------------------------')
            print('\n')
            



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
