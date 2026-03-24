def average_ratios(numbers):
    """
    Calculate the average of ratios (100 / number) for non-zero numbers.

    Args:
        numbers (list): List of numbers. Skips zero values.

    Returns:
        float: Average of the ratios, or 0 if no valid numbers.

    Raises:
        ValueError: If the input list is empty.
    """
    if not numbers:
        raise ValueError("List cannot be empty")
    
    # Filter out zero values to avoid division by zero
    valid_numbers = [num for num in numbers if num != 0]
    
    if not valid_numbers:
        return 0  # Return 0 if all numbers are zero
    
    total = sum(100 / num for num in valid_numbers)
    return total / len(valid_numbers)


# Test with the example data
if __name__ == "__main__":
    print(f"Result: {average_ratios([10, 5, 0])}")
    print("Success! No division by zero error.")
