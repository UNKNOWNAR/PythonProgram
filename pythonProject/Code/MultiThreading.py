import time
import threading

def calc_square(numbers):
    time.sleep(0.2)
    for number in numbers:
        print(f"Square: {number * number}")

def calc_cube(numbers):
    time.sleep(0.2)
    for number in numbers:
        print(f"Cube: {number * number * number}")

numbers = list(range(1, 6))
t = time.time()
calc_square(numbers)
calc_cube(numbers)
print("Before MultiThreading Done in:", time.time() - t)

t = time.time()
# Create threads for square and cube calculations
t1 = threading.Thread(target=calc_square, args=(numbers,))
t2 = threading.Thread(target=calc_cube, args=(numbers,))

# Start the threads
t1.start()
t2.start()

# Wait for both threads to complete
t1.join()
t2.join()

print("After MultiThreading Done in:", time.time() - t)