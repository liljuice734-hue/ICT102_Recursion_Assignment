"""
Fibonacci Sequence Calculator
Sstudent Number: 202500305
Description: This program calculates the nth Fibonacci number using recursive approach
"""

def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursion
    
    """
    # Validate input
    if n < 0:
        return "Error: Fibonacci is not defined for negative positions"
    
    # Base case 1
    if n == 0:
        return 0
    
    # Base case 2
    if n == 1:
        return 1
    
    # Recursive case: F(n) = F(n-1) + F(n-2)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def display_sequence(n):
    """
    Display the Fibonacci sequence up to position n
    
    """
    print(f"\nFibonacci sequence (first {n+1} numbers):")
    sequence = []
    for i in range(n + 1):
        sequence.append(fibonacci(i))
    
    print(", ".join(map(str, sequence)))


def main():
    """
    Main function to run the Fibonacci calculator
    """
    print("=" * 50)
    print("          WILLIAM'S FIBONACCI CALCULATOR")
    print("=" * 50)
    
    try:
        # Get user input
        position = int(input("\nEnter the position in Fibonacci sequence: "))
        
        # Calculate Fibonacci number
        result = fibonacci(position)
        
        # Display result
        if isinstance(result, str):
            print(f"\n{result}")
        else:
            print(f"\nThe Fibonacci number at position {position} is: {result}")
            print(f"F({position}) = {result}")
            
            if position <= 20:  # Limit to prevent long computation
                display_sequence(position)
        
    except ValueError:
        print("\nError: Please enter a valid integer!")
    except RecursionError:
        print("\nError: Position too large! Recursion limit exceeded.")
        print("Try a smaller number (recommended: less than 30)")
    
    print("\n" + "=" * 50)


# Run the program
if __name__ == "__main__":
    main()