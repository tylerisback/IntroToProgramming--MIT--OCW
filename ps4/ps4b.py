# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    #>>> is_word(word_list, 'bat') returns
    True
    #>>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'
WORDS_ALL = load_words(WORDLIST_FILENAME)

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = WORDS_ALL.copy()


    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.

        Returns: a COPY of self.valid_words
        '''
        return self.valid_words

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        assert 0 <= shift <= 26, "The shift must be between 0 and 26."
        shift_dict = {}

        for let in string.ascii_letters:
            if string.ascii_letters.index(let) <= 25:
                shift_dict[let] = (string.ascii_letters.index(let) + shift) % 26
            else:
                shift_dict[let] = ((string.ascii_uppercase.index(let) + shift) % 26) + 26

        return shift_dict



    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        new_mes = ''
        shifted_dict = self.build_shift_dict(shift)

        for el in self.get_message_text():
            if el in shifted_dict:
                new_mes= new_mes + string.ascii_letters[shifted_dict[el]]
            else:
                new_mes = new_mes + el

        return new_mes




class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object

        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)
        self.message_text = text
        self.shift = shift

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class

        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class

        Returns: a COPY of self.encryption_dict
        '''
        return build_shift_dict(self.shift)


    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class

        Returns: self.message_text_encrypted
        '''
        return self.apply_shift(self.shift)

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other
        attributes determined by shift.

        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self,text)


    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create
        the maximum number of valid words, you may choose any of those shifts
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        new_dict = {}
        index_dict = {}

        if  string.whitespace not in self.get_message_text():
            for i in range(26):


                new_text = self.apply_shift(i)
                new_list = new_text.split(' ')
                count = 0
                for word in new_list:
                    if word in self.get_valid_words():
                        if word not in new_dict:
                            new_dict[word] = 1
                            index_dict[i] = 1
                        else:
                            new_dict[word] += 1
                            index_dict[i] += 1


            best_text = max(new_dict)
            best_number = max(index_dict)
            return (best_number, best_text)

        else:
            new_word = ''
            new_list = self.get_message_text().split(' ')
            for word in new_list:
                for i in range(26):
                    new_text = word.apply_shift(i)
                    count = 0
                    if word in self.get_valid_words():
                        if word not in new_dict:
                            new_dict[word] = 1
                            index_dict[i] = 1
                        else:
                            new_dict[word] += 1
                            index_dict[i] += 1

                best_text = max(new_dict)
                new_word = new_word + best_text + ' '
            return new_word









if __name__ == '__main__':


#    #Example test case (PlaintextMessage)
    plaintext = PlaintextMessage('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())

    #Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE
    plaintext2 = PlaintextMessage('baby', 5)
    print("Output for", plaintext2.message_text, 'is', plaintext2.get_message_text_encrypted())

    ciphertext2 = CiphertextMessage('gfgd')
    print("Output: ", ciphertext2.decrypt_message())

    #TODO: best shift value and unencrypted story
    #messagetext = Message(get_story_string())
#
    #print("Output:", messagetext.get_message_text())
#
    #new_mes = messagetext.apply_shift(5)
    #print(new_mes)
#
    #plaintext3 = PlaintextMessage(messagetext.get_message_text(), 5)
    #print('Output: ', plaintext3.get_message_text_encrypted())
#
    #ciphertext3 = CiphertextMessage(plaintext3.get_message_text())
    #print("Output:", ciphertext3.decrypt_message())
#
    #print(get_story_string())
    #pass #delete this line and replace with your code here
#
