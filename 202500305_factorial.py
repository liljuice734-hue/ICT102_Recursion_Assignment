# Factorial Calculator 
# Student Number: 202500305

def fact(n):
    # Validate input
    if n < 0:
        return "Invalid input: Number must be positive"
    
    # Base values
    if n == 0 or n == 1:
        return 1
    
    return n * fact(n - 1)


# Main program
if __name__ == "__main__":
    print("=== William's Factorial Calculator ===")
    
    try:
        # Get user input
        num = int(input("Enter a positive integer: "))
        
        # Calculate factorial
        result = fact(num)
        
        # Display result
        print(f"\nThe factorial of {num} is: {result}")
        
    except ValueError:
        print("Error: Please enter a valid integer")