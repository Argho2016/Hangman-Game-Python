import random

def hangman():
    word = random.choice(["superman", "dog", "goku", "cat", "pokemon", "digimon", "algorithm", "phobia", "Jack", "money"])
    validletters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''

    while len(word) > 0:
        main = ""
        missed = 0

    for letter in word:
        if guess in guessmade:
            main = main + letter
        else:
            main = main + "_" + " "
        if main == word:
            print(main)
            print("You win!!\n You saved the innocent man from certain death! \nYou are now the hero of the town.")
            break

        print("Guess the word:", main)
        guess = input()


        if guess in validletters:
                guessmade = guessmade + guess
        else:
                print("Enter a valid Character")
                guess = input()

        if guess not in word:
                turns = turns -1
                if turns == 9:
                    print("9 turns left")
                    print(" ---------- ")

                if turns == 8:
                    print("8 turns left")
                    print(" ---------- ")
                    print("      O     ")

                if turns == 7:
                    print("7 turns left")
                    print(" ---------- ")
                    print("      O     ")
                    print("      |     ")

                if turns == 6:
                    print("6 turns left")
                    print(" ---------- ")
                    print("      O     ")
                    print("      |     ")
                    print("     /      ")


                if turns == 5:
                    print("5 turns left")
                    print(" ---------- ")
                    print("      O     ")
                    print("      |     ")
                    print("     / \    ")


                if turns == 4:
                    print("4 turns left")
                    print(" ---------- ")
                    print("     \O     ")
                    print("      |     ")
                    print("     / \    ")


                if turns == 3:
                    print("3 turns left")
                    print(" ---------- ")
                    print("     \O/    ")
                    print("      |     ")
                    print("     / \    ")

                if turns == 2:
                    print("2 turns left")
                    print(" ---------- ")
                    print("     \O/ |  ")
                    print("      |     ")
                    print("     / \    ")


                if turns == 1:
                    print("1 turns left")
                    print("Last chance. He is praying to God right now!")
                    print(" ---------- ")
                    print("     \O|/   ")
                    print("      |     ")
                    print("     / \    ")

                if turns == 0:
                    print("You are a loser. You let a kind man die. Shame on you.")
                    print(" ---------- ")
                    print("      O_|   ")
                    print("     /|\    ")
                    print("     / \    ")
                    break

name = input("Enter your name\n")
print("\nWelcome", name )

print("\nTry to guess the word within 10 tries or an innocent man will die")
hangman()
print()
