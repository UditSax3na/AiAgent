def add_two_numbers(a, b):
    """
    This function adds two numbers together.

    Parameters:
    a (float): The first number.
    b (float): The second number.

    Returns:
    float: The sum of a and b.
    """
    return a + b

def main():
    # Ask the user for two numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Call the function and print the result
        result = add_two_numbers(num1, num2)
        print(f"The sum of {num1} and {num2} is: {result}")
    except ValueError:
        print("That's not a valid number!")

if __name__ == "__main__":
    main()