def get_integer_input() -> int:
    """
    Handles user input to obtain a valid integer.
    Continuously prompts the user until a valid integer is entered.
    Returns:
        int: The integer entered by the user.
    """
    while True:
        try:
            return int(input("Enter an integer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def check_even_odd(number: int) -> str:
    """
    Determines if a given number is even or odd.
    
    Args:
        number (int): The integer to check.
    
    Returns:
        str: A formatted string indicating whether the number is even or odd.
    """
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."

def main():
    """
    Main program flow to get input, check even/odd status, and display the result.
    """
    number = get_integer_input()
    result = check_even_odd(number)
    print(result)

if __name__ == "__main__":
    main()
