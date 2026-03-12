
# Day 1: Printing, Commenting, Debugging, String Manipulation
print("Welcome to the Band Name Generator!")

city_name = input("What's the name of the city you grew up in? ").strip().title()
pet_name = input("What's your pet's name? ").strip().title()

print(f"Your band name could be: {city_name} {pet_name}")

# Day 2: Day 2: Data Types, Numbers, Operations, Type Conversion, f-Strings
print("Welcome to the Tip Calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("Tip Percentage (10, 12, or 15): "))
people = int(input("How many people to split the bill? "))

tip_percent = tip / 100
total_tip = bill * tip_percent
total_bill = bill + total_tip
total_per_person = total_bill / people

print(f"Each person should pay: ${total_per_person:.2f}")

# Day 3: Conditional Statements, Logical Operators, Scope
print("Welcome to Treasure Island: Your mission is to find the treasure!")

side_move = input('You\'re at a crossroad. Where do you want to go? "Left" or "Right": ').strip().lower()

if side_move == "left":
    swim_wait = input('You\'ve come to a lake. There is an island in the middle.\nType "Wait" to wait for a boat or "Swim" to swim across: ').strip().lower()

    if swim_wait == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors: red, yellow, blue. Which colour do you choose? ").strip().lower()

        if door == "red":
            print("Burned by fire. Game Over!")
        elif door == "blue":
            print("Eaten by beast. Game Over!")
        elif door == "yellow":
            print("You Win! 🎉")
        else:
            print("Invalid door choice. Game Over!")

    elif swim_wait == "swim":
        print("Attacked by trout. Game Over!")
    else:
        print("Invalid choice. Game Over!")

elif side_move == "right":
    print("You fell into a hole. Game Over!")
else:
    print("Invalid direction. Game Over!")

# Day 4: Randomisation and Python List
import random       # Random number generator
import my_module    # Custom module for favorite number

# Random Numbers Examples
print("Random Numbers Examples:")

# Random integer between 1 and 10
rand_int = random.randint(1, 10)
print("Random integer (1-10):", rand_int)

# Access favorite number from my_module
print("Favorite number from my_module:", my_module.favNumber)

# Random float between 0 and 10
random_float = random.random() * 10
print("Random float (0-10):", random_float)

# Random float in a range 1-10
uniform_num = random.uniform(1, 10)
print("Random uniform number (1-10):", uniform_num)

# Coin toss example
coin = random.randint(0, 1)
print("Coin toss result:", coin)
if coin == 0:
    print("Tails")
else:
    print("Heads")

# Lists and Nested Lists
print("\nLists Examples:")

# Provinces in Calabarzon
calabarzon = ["Cavite", "Laguna", "Batangas", "Quezon Province"]
calabarzon.append("Isabela")  # Add a single item
calabarzon.extend(["Pangasinan", "Pampanga", "Tarlac"])  # Add multiple items

# Cities in NCR
ncr = ["Quezon City", "Makati City", "Taguig City", "City of Manila", "Pasig City"]

# Nested list of cities and provinces
city_province = [ncr, calabarzon]
print("Nested list of regions:", city_province)
print("Second province in Calabarzon:", city_province[1][1])

# Random friend selector
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print("Randomly selected friend:", random.choice(friends))

# Another random selection using index
random_index = random.randint(0, len(friends)-1)
print("Random friend by index:", friends[random_index])

# Rock-Paper-Scissors Game
print("\n🪨 Rock-Paper-Scissors")
print("0 = Rock, 1 = Paper, 2 = Scissors")

user_choice = int(input("Enter your choice: "))
computer_choice = random.randint(0, 2)

options = ["Rock", "Paper", "Scissors"]
print(f"You chose: {options[user_choice]}")
print(f"Computer chose: {options[computer_choice]}")

# Determine the winner
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")
