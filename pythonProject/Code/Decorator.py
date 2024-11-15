import time

# Decorator function to measure execution time
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()  # Start time
        result = func(*args, **kwargs)  # Execute the function
        end = time.time()  # End time
        print(f"{func.__name__} took {str((end - start) * 1000)} ms")  # Print time taken in ms
        return result
    return wrapper

# Function to calculate square of numbers
@time_it
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number * number)
    return result

# Function to calculate cube of numbers
@time_it
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number * number * number)
    return result

if __name__ == "__main__":
    numbers = list(range(1,1000000))
    squares = calc_square(numbers)  # This will print the time taken to calculate squares
    cubes = calc_cube(numbers)  # This will print the time taken to calculate cubes