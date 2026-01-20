#Task 1
# write a python code to calculate the factorial of a number without using functions.
number = int(input("Enter a number to calculate its factorial: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"The factorial of {number} is {factorial}")
 
 
 #Task 2
 # write a code Optimize the above code by removing unnecessary variables, simplifying the loop, and improving readability.
number = int(input("Enter a number to calculate its factorial: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"The factorial of {number} is {factorial}")


#Task 3
# write a python code on factorial with function
def factorial(n):
    """Calculate the factorial of a number n."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
# Example usage
number = 5
print(f"The factorial of {number} is {factorial(number)}")


#Task 4
#Write a program that compares an AI-written script that’s all in one block and a version that uses clear, well‑named functions, explaining which is better for understanding, reuse, debugging, big projects, and avoiding over‑reliance on AI, and show it in a small table.
def calculate_factorial(number):
    if number == 0:
        return 1
    else:
        return number * calculate_factorial(number - 1)

number = int(input("Enter a number to calculate its factorial: "))
result = calculate_factorial(number)
print(f"The factorial of {number} is {result}")


#Task 5
# write a program on create iterative version logic vs recursive version logic of factorial and explain their flow and compare readability, stack usage, performance, and when recursion should be avoided.

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

print("Iterative version:")
print(factorial_iterative(5))

print("Recursive version:")
print(factorial_recursive(5))