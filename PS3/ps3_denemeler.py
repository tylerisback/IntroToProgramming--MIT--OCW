word = ' AhmetKimya '

word = word.strip()
word = word.lower()

print(word)

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """

    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

freq_dict = get_frequency_dict(word)
print(freq_dict)

#Second Component
n = 10
word_length = len(word)
sec_comp = max((7 * word_length - 3 *(n - word_length)), 1)
print(sec_comp)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

first_comp = 0
for char in freq_dict.keys():
    first_comp += SCRABBLE_LETTER_VALUES[char] * freq_dict[char]

word_score = first_comp * sec_comp
print(word_score)

def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """

    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()

def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """

    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    return hand

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

hand = deal_hand(7)
print(hand)
display_hand(hand)
#hand.pop(hand.keys()[0])
#hand.keys()[0]
#print(hand)


def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured).

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    #if (type(word) is dict) and (type(hand) is str):
    #    hand, word = word, hand
    word = word.strip()
    word = word.lower()

    word = get_frequency_dict(word)

    for char in word.keys():
        if hand[char] > 0:
            if hand[char] >= word[char]:
                hand[char] = hand[char] - word[char]
            else:
                hand[char].pop()

        else:
            continue

    return hand

def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    word = word.strip()
    word = word.lower()
    hand_copy = hand.copy()

    for char in word:
        if (char not in string.ascii_lowercase):
            return False
        if (hand_copy.get(char,0) == 0):
            return False

    if word not in word_list:
        return False

    return True

wordlist= load_words()


def deal_hand_wild(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """

    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels):
        if i == num_vowels - 1:
            x = '*'
            hand[x] = hand.get(x, 0) + 1
        else:
            x = random.choice(VOWELS)
            hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    return hand

def is_valid_word_wild(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    word = word.strip()
    word = word.lower()
    hand_copy = hand.copy()
    new_word = get_frequency_dict(word)


    if len(word) > sum(hand.values()):
        return False

    for char in word:
        if (char not in string.ascii_lowercase and char != '*'):
            return False
        if (hand.get(char,0) == 0) and (char not in VOWELS):
            return False

    for char in new_word.keys():
        if char in VOWELS:
            if new_word[char] > hand.get(char,0) + 1:
                return False
        else:
            if new_word[char] > hand.get(char,0):
                return False

    flag = False
    for j in VOWELS:
        news_word = word.replace('*', j)
        if news_word in word_list:
            flag= True

    if flag == False:
        return False
    else:
        return True

new_new_hand = get_frequency_dict('cows*z')
new_new_word = 'c*w'
print(new_new_hand)
print(new_new_word)
print(is_valid_word_wild(new_new_word, new_new_hand, wordlist))

print('cow' in wordlist)
print(deal_hand_wild(7))
print(sum(hand.values()))