def display_menu():
    """Displays the program's menu options."""
    print("\nMenu:")
    print("1. Greet User")
    print("2. Check Even/Odd")
    print("3. Exit")

def greet_user():
    """Prints a greeting message."""
    print("Hello! Welcome!")

def get_integer_input():
    """Handles user input to obtain a valid integer."""
    while True:
        try:
            return int(input("Enter an integer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def check_even_odd(number: int) -> str:
    """Determines whether a number is even or odd."""
    return f"{number} is an Even number." if number % 2 == 0 else f"{number} is an Odd number."

def even_odd_checker_action():
    """Handles the even/odd check by obtaining input and displaying the result."""
    number = get_integer_input()
    print(check_even_odd(number))

def handle_menu_choice(choice: int) -> bool:
    """Executes the corresponding action based on the user's menu choice."""
    if choice == 1:
        greet_user()
    elif choice == 2:
        even_odd_checker_action()
    elif choice == 3:
        print("Exiting program. Goodbye!")
        return True  # Signal to terminate the program loop
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
    return False  # Continue the loop

def main():
    """Main program loop to display menu and process user choices."""
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-3): "))
            if handle_menu_choice(choice):
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
