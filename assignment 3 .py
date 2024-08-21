def calculate_bmi():
    try:
        # Input the weight in kilograms
        weight = float(input("Enter your weight in kilograms: "))
        # Input the height in meters
        height = float(input("Enter your height in meters: "))
        # Ensure that height and weight are positive
        if weight <= 0 or height <= 0:
            print("Error: Both weight and height must be positive numbers.")
            return
        # Calculate the BMI
        bmi = weight / (height ** 2)
        # Determine the BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"
        # Display the calculated BMI and category
        print(f"Your BMI is: {bmi:.2f}")
        print(f"BMI Category: {category}")

    except ValueError:
        # Handle non-numeric inputs
        print("Error: Please enter valid numeric values for weight and height.")
        # Call the function
calculate_bmi()