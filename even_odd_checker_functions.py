# even_odd_checker_functions.py

def get_integer_input() -> int:
    """
    Prompts the user to enter an integer.
    Keeps prompting until a valid integer is entered.
    
    Returns:
        int: The valid integer entered by the user.
    """
    while True:
        try:
            user_input = int(input("Enter an integer: "))
            return user_input
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def check_even_odd(number: int) -> str:
    """
    Determines whether the given number is even or odd.
    
    Args:
        number (int): The number to check.
    
    Returns:
        str: A message indicating if the number is even or odd.
    """
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."

if __name__ == "__main__":
    number = get_integer_input()
    result = check_even_odd(number)
    print(result)
