def modulo_calculator():
    """Calculates the remainder of dividend divided by divisor."""
    dividend = int(input("Enter first whole number: "))
    divisor = int(input("Enter the second whole number: "))
    remainder = dividend % divisor   #Should have used z=x%y 
    print(f"The remainder of {dividend} modulo by {divisor} is {remainder}.") #"print(f" for passing an argument


def integer_division_calculator():
    """Calculate the integer quotient of dividend divided by divisor."""
    dividend = int(input("Enter the dividend: "))
    divisor = int(input("Enter the divisor: "))
    quotient = dividend // divisor
    print(f"The integer quotient of {dividend} divided by {divisor} is {quotient}.")


def for_loop_counter():
    """Count a variable up or down by an increment for a specified number of times."""

    # Get values and parameters from user input
    initial_value = float(input("What should be the initial value of the counter? "))
    loop_count = int(input("How many times should the loop run? "))
    increment_amount = float(input("What should the increment amount be? "))
    should_increment = input("Should the counter increment instead of decrementing? (y/n)").lower() == 'y'

    # If counter should decrement, make the increment negative
    if not should_increment:
        increment_amount *= -1

    # Loop times + counter
    for i in range(loop_count):
        initial_value += increment_amount
    print(f"The final value of the counter is {initial_value}")



def float_addition():
    """Add together a specified number of values."""
    num_values = int(input("How many values do you want to add together?\n"))
    values = [float(input(f"Enter value {i+1}: ")) for i in range(num_values)]
    result = sum(values)
    print(f"The result of adding {', '.join(str(v) for v in values)} is {result}")
    return result


def print_ascii_values():
    """Print the ASCII values of letters in a string."""
    string = input("Enter a string: ")
    # Generate ASCII values in str using ord() function
    ascii_values = [ord(char) for char in string]
    print(f"The ASCII values for {string} are {', '.join(str(v) for v in ascii_values)}")#Values are separated by ,



def change_machine():
    """Calculates the number of each type of coins in change."""
    amount = float(input("Enter the amount of change you have: "))
    quarters = int(amount / 25)
    dimes = int((amount % 25) / 10)
    nickels = int(((amount % 25) % 10) / 5)
    pennies = int((((amount % 25) % 10) % 5) / 1)
    print(f"You have {quarters} quarters, {dimes} dimes, {nickels} nickels, and {pennies} pennies.")


def rock_paper_scissors():
    """Play RPS vs comp """
    valid_choices = ['rock', 'paper', 'scissors'] #these are the choices 
    player_choice = input("Choose rock, paper, or scissors: ").lower()

    if player_choice not in valid_choices:
        print("Invalid choice.")
        return

    import random
    computer_choice = random.choice(valid_choices)
    print("Computer chooses {computer_choice}")

    if player_choice == computer_choice:
        print("Tie!")
    elif (player_choice == 'rock' and computer_choice == 'scissors' or 
          player_choice == 'paper' and computer_choice == 'rock' or 
          player_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("Computer wins.")
def mario_wins():
    #Did not attempt to code this at all but get the idea
    stairs = int(input("How many stairs should Mario climb to finish the level? "))
    #prints blocks+flag
    print(" " * (stairs) + "  |>")
    #for i *#
    for i in range(stairs):
        print(" " * (stairs - i - 1) + "#" * (i + 1) + "  |" )
    
print("Choose one of the following options:")
print("1. Modulo Calculator")
print("2. Integer Division Calculator")
print("3. For Loop Counter")
print("4. Integer and Float Addition")
print("5. Print ASCII values of letters in a string")
print("6. Change Machine")
print("7. Rock Paper Scissors")
print("8. Mario wins a level")

#choice 1-8 starts the def function 
choice = int(input("Enter your choice (1-8): "))
if choice == 1:
    modulo_calculator()
elif choice == 2:
    integer_division_calculator()
elif choice == 3:
    for_loop_counter()
elif choice == 4:
    float_addition()
elif choice == 5:
    print_ascii_values()
elif choice == 6:
    change_machine()
elif choice == 7:
    rock_paper_scissors()
elif choice == 8:
    mario_wins()
else:
    print("Invalid choice. Please enter a number between 1 and 8.")