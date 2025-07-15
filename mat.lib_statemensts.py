#number1 = 10 
#number2 = 5
#Addition= number1 + number2
#subtraction= number1 - number2
#Multiplation= number2 * number1

#print(f"Addition of {number1} and {number2} is {Addition}")
#print(f"Subtraction of {number1} and {number2} is {subtraction}")
#print(f"Multiplication of {number2} and {number1} is {Multiplation}")\
    
# Mad Libs Story Generator with Conditional Twists

# Ask the user for input
day_adj = input("Enter an adjective to describe the day: ")
monkey_adj = input("Enter an adjective to describe the monkey: ")
lion_adj = input("Enter an adjective to describe the lion: ")
experience_adj = input("Enter an adjective to describe the whole experience: ")

# Basic story template
story = f"\nOn a beautiful {day_adj} day, I went to the zoo. "
story += f"I saw a funny {monkey_adj} monkey swinging from the trees. "
story += f"Then, I spotted a majestic {lion_adj} lion lounging in the sun. "
story += f"What a wild and {experience_adj} experience!"

# Conditional twist based on the final adjective
if experience_adj.lower() == "exciting":
    story += " I even took a selfie with the lion… safely behind glass, of course!"
elif experience_adj.lower() == "scary":
    story += " I ran for cover when the monkey threw a banana at me!"
else:
    story += " Definitely a day to remember."

# Display the full story
print("\nYour Mad Libs Zoo Adventure:")
print(story)

