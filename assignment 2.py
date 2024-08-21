def calculate_rectangle_area():
    try:
        # Input the length of the rectangle
        length = float(input("Enter the length of the rectangle: "))
        # Input the width of the rectangle
        width = float(input("Enter the width of the rectangle: "))
        # Check if length and width are positive
        if length <= 0 or width <= 0:
             print("Error: Both length and width must be positive numbers.")
        else:
            # Calculate the area of the rectangle
            area = length * width

            # Display the result
            print(f"The calculated area of the rectangle is: {area}")
    except ValueError:
        # Handle non-numeric inputs
        print("Error: Please enter valid numeric values for length and width.")
        # Call the function
calculate_rectangle_area()