import string

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for l in range(len(secretWord)):
        if (secretWord[l] not in lettersGuessed):
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedSoFar = []
    for l in range(len(secretWord)):
        if (secretWord[l] in lettersGuessed):
            guessedSoFar.append(secretWord[l])
        else:
            guessedSoFar.append("_ ")

    guessedWord = ""
    for char in range(len(guessedSoFar)):
        guessedWord+=str(guessedSoFar[char])

    return guessedWord

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters = string.ascii_lowercase
    availableLetters = []

    for l in letters:
        if l in lettersGuessed:
            pass
        else:
            availableLetters.append(l)

    letters = ""
    for char in range(len(availableLetters)):
        letters+=str(availableLetters[char])
    return letters
