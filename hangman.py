import random
word_list = [
    'wares',
    'soup',
    'mount',
    'extend',
    'brown',
    'expert',
    'tired',
    'humidity',
    'backpack',
    'crust',
    'dent'
    ]

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_ " * len(word)
    guessed = False
    check=[]
    guessed_letters = []
    fills=[]
    guessed_words = []
    wrongs = 6

    print("Let's play Hangman!")
    print(hangmanpics(wrongs))
    print(word_completion)
    guess = input()

    while wrongs>0 and guessed==False:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha(): # isalpha() determines if its alphabets or not
            if guess in guessed_letters:
                print("You already guessed the letter ", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                wrongs -= 1
                guessed_letters.append(guess)
        elif len(guess)!=1 and guess!=word:
            print("that is not the word")
            wrongs -=1
        else:
            print("you guessed the word")




def hangmanpics(wrongs):
    stages = [
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,

                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[wrongs]









