# Token Tactics: A simple text-based token management game.
# Players start with 100 tokens and can roll to win or lose tokens, or spend tokens in a shop to buy upgrades.
# The goal is to manage tokens wisely and avoid running out. Good luck!

# imports
import random

# variables
increase1 = 0  # placeholder for variable at line 44
increase2 = 0  # placeholder for variable at line 50
t = 100  # token amount
tokens = f'Tokens left: {t}'  # token amount as string data-type
print(tokens)  # prints tokens to terminal
numerals = list(range(1, 100))  # list for the numbers needed to randomize the producted number at line 21
wntens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  # numbers needed for win
wnfives = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]  # numbers needed for win
# main functions
while True:
    x = input('press \"r\", \"e\", or \"s\": ')  # variable for inputs: "r" for roll number, "e" for exit and "s" for shop

    if t == 0:  # checks if token value is at 0
        print("You have run out of tokens. Game over!")
        break  # breaks the while loop, thus ending the program

    if x == "r":  # rolls number
        n = random.choice(numerals)  # generates random number (see line 10)

        if n in wntens or n in wnfives:  # numbers for win (see lines 11 and 12)
            gained_tokens = 20 + int(20 * increase1)  # base tokens received on win, plus multiplier from shop
            t += gained_tokens
            print(n)  # prints the number generated
            print(f'You gained {gained_tokens} tokens!')  # winning amount
        else:  # lose values
            lost_tokens = 5 + increase2
            t -= lost_tokens
            print(n)  # prints number generated
            print(f'You lost {lost_tokens} tokens.')  # losing amount

        tokens = f'Tokens left: {t}'  # update tokens string
        print(tokens)  # prints new token amount

    elif x == "s":  # enter shop
        s = input("You have opened the shop. What would you like to buy?\n"
                  "1. 10% increase in money received (Press 1 to buy): 20 tokens\n"
                  "2. 1 less token decrease (Press 2 to buy): 50 tokens\n"
                  "Press 1 or 2 to buy anything: ")

        # buying upgrade 1
        if s == "1":
            if t >= 20:  # check if enough tokens are available
                t -= 20
                increase1 += 0.1  # increases the amount of tokens received by 10% (can stack)
                if increase1 > 5:  # allows this upgrade to be bought only 50 times
                    increase1 = 5
                    print("You have reached the limit for this specific upgrade.")
                else:
                    print("Upgrade purchased: 10% increase in money received.")
            else:
                print("Not enough tokens to buy this upgrade.")

        # buying upgrade 2
        elif s == '2':
            if t >= 50:  # check if enough tokens are available
                t -= 50
                increase2 -= 1
                if increase2 <= -5:  # can only buy this upgrade 5 times (when maxed, token deduction = 0)
                    increase2 = -5
                    print('You have reached the limit for this specific upgrade.')
                else:
                    print("Upgrade purchased: 1 less token decrease.")
            else:
                print("Not enough tokens to buy this upgrade.")

        tokens = f'Tokens left: {t}'  # update tokens string
        print(tokens)  # prints new token amount

    elif x == "e": # exiting the program
        print("Exiting the game. Goodbye!") # goodbye message
        break # breaks the loop, thus ending the program.
