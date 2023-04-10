import random

def modulo_testing():
    """Calculates the remainder of dividend divided by divisor."""
    x = int(input("Enter the dividend you want the remainder of: "))
    y = int(input("Enter the divider you want the remainder of: "))

    modulo = x % y #could have used z=x%y
    print(f"The remainder of {x} divided by {y} is {modulo}\n")
    return modulo

def integer_division_testing():
    """Calculate the integer quotient of dividend divided by divisor."""
    x = int(input("Enter the dividend you want the remainder of: "))
    y = int(input("Enter the divider you want the remainder of: "))

    result = x // y #main diff to use // in Py
    print(f"The result of {x} divided by {y} is {result}\n")
    return result

def float_cast_to_integer_division_testing():
    """Calculate the integer quotient of dividend divided by divisor.""" 
    x = float(input("Enter the dividend you want the remainder of: "))
    y = float(input("Enter the divider you want the remainder of: "))

    result = x / y
    int_result = int(result)
    print(f"The result of {x} divided by {y} is {result}, once cast to an int the result is {int_result}\n")
    return int_result

def for_loop_testing(): # Get values and parameters from user input
    """Count a variable up or down by an increment for a specified number of times."""
    counter = float(input("What should be the initial value of the counter? "))
    loop_count = int(input("How many times should the loop run? "))
    increment = float(input("How much should the counter increment by? "))
    is_positive = input("Should the counter decrement instead of incrementing? y / n: ") == 'n'
# If counter should decrement, make the increment negative
    if not is_positive:
        increment = increment * -1
# Loop times + counter
    for _ in range(loop_count):
        counter += increment

    print(f"The final value of the counter is {counter}\n")
    return counter

def integer_float_addition():
    """Add together a specified number of values."""
    x = int(input("Enter an integer you want summed: "))
    y = float(input("Enter an float you want summed: "))

    result = x + y #the FORMULA
    print(f"The result of {x} plus {y} is {result}\n")
    return result

def print_ascii_string_value():
    """Print the ASCII values of letters in a string."""
    string = input("Enter a string: ")
    # Generate ASCII values in str using ord() function
    ascii_values = [ord(char) for char in string]
    print(f"The ASCII values for {string} are {', '.join(str(v) for v in ascii_values)}")#Values are separated by ,

def change_machine():
    """Calculates the number of each type of coins in change."""
    amount = float(input("Enter the amount to return change for (example: $2.95): "))
    amount_cents = round(amount * 100)

    coins = [25, 10, 5] #arr for coins
    coin_counts = [0, 0, 0] #empty var arr

    for i, coin in enumerate(coins):
        coin_counts[i] = amount_cents // coin
        amount_cents %= coin

    print(f"Change for {amount}: {coin_counts[0]} quarters, {coin_counts[1]} dimes, and {coin_counts[2]} nickels\n")


def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"] #

    user_choice = int(input("Make a choice:\n 1. Rock\n 2. Paper\n 3. Scissors\n")) - 1 #Choose "0" it gets better odds 
    ai_choice = random.randint(0, 2)

    print(f"You chose {choices[user_choice]}, AI chose {choices[ai_choice]}")
#game logics
    if user_choice == ai_choice:
        print("It's a draw!")
    elif (user_choice + 1) % 3 == ai_choice: 
        print("AI wins!")
    else:
        print("You win!")

def mario_wins_level(): 
    stairs = int(input("How many stairs should Mario climb to finish the level?\n"))
    if stairs <= 0:  #Quality input control
        print("Invalid input. Please provide a positive integer.")
        return
    
    print(" " * (stairs) + "  |>") #I couldnt get this figured out and Denis showed me his so credit to him
    #"pyramid constractor", the only thing Ukranian stole from Russian
    for i in range(stairs):
        print(" " * (stairs - i - 1) + "#" * (i + 1) + "  |" )
#Main menu
def main():
    while True:
        print("Choose an option:")
        print("1. Modulo Testing")
        print("2. Integer Division Testing")
        print("3. Float cast to Integer Division Testing")
        print("4. For Loop Testing")
        print("5. Integer Float Addition")
        print("6. Print ASCII String Value")
        print("7. Change Machine")
        print("8. Rock Paper Scissors")
        print("9. Mario Wins a Level")
        print("10. Quit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            modulo_testing()
        elif choice == 2:
            integer_division_testing()
        elif choice == 3:
            float_cast_to_integer_division_testing()
        elif choice == 4:
            for_loop_testing()
        elif choice == 5:
            integer_float_addition()
        elif choice == 6:
            print_ascii_string_value()
        elif choice == 7:
            change_machine()
        elif choice == 8:
            rock_paper_scissors()
        elif choice == 9:
            mario_wins_level()
        elif choice == 10:
            print("Cheers!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__== "__main__": #Def to return to int main unless elif 10 Break!

    main()
