from random import randint

number = randint(1, 99)

""" To set it manually """
number = number 

def game_prompt():
    num = 0
    index = 0
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!")
    print("")
    while True:
        print("What's your guess between 1 and 99?")
        num = input(">> ")
        if num == "exit":
            print("Goodbye!")
            exit(0)
        else:
            if num.isdigit():
                num = int(num)
            else:
                print("That's not a number.")
        if num == number:
            if number == 42:
                print("The answer to the ultimate question of life, the universe and everything is 42.")
            if index == 0:
                print("Congratulations! You got it on your first try!")
            else:
                print("Congratulations, you've got it!")
                print("You won in {n} attempts!".format(n=index))
            exit(0)
        index += 1


game_prompt()