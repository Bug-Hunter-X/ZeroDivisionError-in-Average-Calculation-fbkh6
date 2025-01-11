def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers) 

# Example usage (add more robust testing)
my_numbers = [10, 20, 30]
avg = calculate_average(my_numbers)
print(f"The average is: {avg}")

empty_list = []
avg_empty = calculate_average(empty_list)
print(f"The average of an empty list is: {avg_empty}") 