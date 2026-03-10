# Day 1: Printing, Commenting, Debugging, String Manipulation
print("Welcome to the Band Name Generator.")

city_name = input("What's the name of the city you grew up in: ").strip()
pet_name = input("What's your pet's name: ").strip()

print(f"Your band name could be {city_name} {pet_name}")


# Day 2: Data Types, Numbers, Operations, Type Conversion, f-Strings
print("Welcome to the tip calculator!")

bill = float(input("What was the total bill: $"))
tip = int(input("Tip Percentage: 10, 12, or 15\nHow much tip would you like to give: "))
people = int(input("How many people to split the bill: "))

tip_percent = tip / 100
total_tip = bill * tip_percent
total_bill = bill + total_tip
total_per_person = total_bill / people

print(f"Each person should pay: ${total_per_person:.2f}")



# Day 3: Conditional Statements, Logical Operators, Scope
print("Welcome to Treasure Island: Your mission is to find the treasure!")

side_move = input('You\'re at a crossroad. Where do you want to go?\nType "Left" or "Right": ').strip().lower()

if side_move == "left":
    swim_wait = input('You\'ve come to a lake. There is an island in the middle.\nType "Wait" to wait for a boat. Type "Swim" to swim across: ').strip().lower()

    if swim_wait == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue. Which colour do you choose? ").strip().lower()

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
