# Create a list of numbers
numbers = [10, 20, 30, 40, 50, 60]

target = 30

try:
    index = numbers.index(target)
    print(f"The index of {target} is: {index}")
except ValueError:
    print(f"{target} is not in the list.")
