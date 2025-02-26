def get_integer_input() -> int:
    while True:
        try:
            user_input = int(input("Enter an integer: "))
            return user_input
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def check_even_odd(number: int) -> str:
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."

if __name__ == "__main__":
    number = get_integer_input()
    result = check_even_odd(number)
    print(result)
