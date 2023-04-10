import math
import random
import string

def modulo_testing():
    x = int(input("Enter the dividend you want the remainder of: "))
    y = int(input("Enter the divider you want the remainder of: "))

    modulo = x % y
    print(f"The remainder of {x} divided by {y} is {modulo}\n")
    return modulo

def integer_division_testing():
    x = int(input("Enter the dividend you want the remainder of: "))
    y = int(input("Enter the divider you want the remainder of: "))

    result = x // y
    print(f"The result of {x} divided by {y} is {result}\n")
    return result

def float_cast_to_integer_division_testing():
    x = float(input("Enter the dividend you want the remainder of: "))
    y = float(input("Enter the divider you want the remainder of: "))

    result = x / y
    int_result = int(result)
    print(f"The result of {x} divided by {y} is {result}, once cast to an int the result is {int_result}\n")
    return int_result

def for_loop_testing():
    counter = float(input("What should be the initial value of the counter? "))
    loop_count = int(input("How many times should the loop run? "))
    increment = float(input("How much should the counter increment by? "))
    is_positive = input("Should the counter decrement instead of incrementing? y / n: ") == 'n'

    if not is_positive:
        increment = increment * -1

    for _ in range(loop_count):
        counter += increment

    print(f"The final value of the counter is {counter}\n")
    return counter

def integer_float_addition():
    x = int(input("Enter an integer you want summed: "))
    y = float(input("Enter an float you want summed: "))

    result = x + y
    print(f"The result of {x} plus {y} is {result}\n")
    return result

def print_ascii_string_value():
    str_ = input("What string do you want to know the ASCII values of the letters of? ")
    str_size = len(str_)

    for i in range(str_size):
        ascii_val = ord(str_[i])
        print(f"The char at position {i} is {str_[i]} and the ASCII value is {ascii_val}\n")

def change_machine():
    amount = float(input("Enter the amount to return change for (example: 2.95): "))
    amount_cents = round(amount * 100)

    coins = [25, 10, 5]
    coin_counts = [0, 0, 0]

    for i, coin in enumerate(coins):
        coin_counts[i] = amount_cents // coin
        amount_cents %= coin

    print(f"Change for {amount}: {coin_counts[0]} quarters, {coin_counts[1]} dimes, and {coin_counts[2]} nickels\n")


def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]

    user_choice = int(input("Make a choice:\n 1. Rock\n 2. Paper\n 3. Scissors\n")) - 1
    ai_choice = random.randint(0, 2)

    print(f"You chose {choices[user_choice]}, AI chose {choices[ai_choice]}")

    if user_choice == ai_choice:
        print("It's a draw!")
    elif (user_choice + 1) % 3 == ai_choice:
        print("AI wins!")
    else:
        print("You win!")

def mario_wins_a_level():
    level = int(input("Enter the level number Mario just completed: "))
    print(f"Mario just completed level {level}! Congratulations!\n")

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
            mario_wins_a_level()
        elif choice == 10:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":

    main()
