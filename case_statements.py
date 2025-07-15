import random
secret_nummber=random.randint(1,10)
guess= int(input("I'm thinking of a number between 1 and 10. Can you guess it?"))



if guess == secret_nummber: 
            print ("Congratulations, you guessed it!")
elif guess < secret_nummber: 
            print("Nope, your guess is a bit low. Give it another shot!")
elif guess > secret_nummber:
            print ("Oops, your guess is a bit high. Try again!")
            
            
play_again = input("Do you want to play again? (yes/no): ")
print("Thanks for playing!")

match guess:
    case _ if guess == secret_number:
        print("🎉 Congratulations, you guessed it!")
    case _ if guess > secret_number:
        print("⬆️ Oops, your guess is a bit high. Try again!")
    case _ if guess < secret_number:
        print("⬇️ Nope, your guess is a bit low. Give it another shot!")
