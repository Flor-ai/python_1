def calculate_simple_interest():
    try:
        # Input the principal amount
        principal = float(input("Enter the principal amount: "))
        # Input the interest rate
        rate = float(input("Enter the interest rate (in percentage): "))
        # Input the time period in years
        time = float(input("Enter the time period (in years): "))
        # Calculate the simple interest
        simple_interest = (principal * rate * time) / 100
        # Display the result
        print(f"The calculated simple interest is: {simple_interest}")
    except ValueError:
        # Handle non-numeric inputs
        print("Error: Please enter valid numeric values for principal, rate, and time.")
# Call the function
calculate_simple_interest()