# even_odd_checker_functions.py

def get_integer_input() -> int:
    """
    Prompts the user to enter an integer.
    Handles invalid input and keeps prompting until a valid integer is entered.
    
    Returns:
        int: The integer input by the user.
    """
    while True:
        try:
            user_input = int(input("Enter an integer: "))
            return user_input
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def check_even_odd(number: int) -> str:
    """
    Checks whether the provided integer is even or odd.
    
    Parameters:
        number (int): The number to check.
    
    Returns:
        str: A formatted string indicating if the number is even or odd.
    """
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."

# Main program
if __name__ == "__main__":
    # Get integer input from the user
    number = get_integer_input()
    
    # Check if the number is even or odd and print the result
    result = check_even_odd(number)
    print(result)
