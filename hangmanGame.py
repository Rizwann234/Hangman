import random

# Unknown word generator
def wordGenerator() :
    words = ["dog", "cat", "electric", "surreal", "apple", "phone", "herring", "dog"]
    unknown_word = words[random.randint(0,len(words)-1)]
    return unknown_word

word = wordGenerator()

#Initialise game
def hangman(word) :
    hidden = []
    while len(hidden) != len(word) :
        hidden.append("_")
    print(f"Guess this {len(word)}-letter word : \n" + str(hidden))
    counter = 10 
    while counter != 0 :
        guess = input("Please input a letter : ")
        if len(guess) > 1 :
            print("Please input a single letter")
        elif guess not in word :
            counter -= 1
            print(f"oops, you have {counter} guesses left.")
        elif guess in word :
            for i in range(0,len(word)) :
                if guess == word[i] :
                    hidden[i] = word[i]
                    print("\n" + str(hidden))
        if counter == 0 :
            print("Game Over.")
            break
        if "_" not in hidden :
            print(f"Congratulations! The word was {word}.")
            break
        
hangman(word)
        

