#Task1
#write a Python function filter non negative that returns a new list with only values greater than or equal to 0, without modifying the original list, for cleaning invalid negative IoT sensor readings.
def filter_non_negative(sensor_readings):
    return [reading for reading in sensor_readings if reading >= 0]
#Example usage:
sensor_data = [23, -5, 12, -1, 0, 45, -10]
cleaned_data = filter_non_negative(sensor_data)
print("Original sensor data:", sensor_data)
print("Cleaned sensor data (non-negative):", cleaned_data)


#Task2
# write a Python function that takes a text string and returns how many vowels, consonants, and digits it contains, treating upper and lower case letters the same.
def count_characters(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    digit_count = 0
    for char in text:
        if char in vowels:
            vowel_count += 1
        elif char.isalpha():
            consonant_count += 1
        elif char.isdigit():
            digit_count += 1
    return vowel_count, consonant_count, digit_count
#Example usage:
input_text = "Hello World! 123"
vowels, consonants, digits = count_characters(input_text)
print(f"Input text: {input_text}")
print(f"Vowels: {vowels}, Consonants: {consonants}, Digits: {digits}")


#Task3
#write a simple, readable Python function is palindrome that returns True if a string reads the same forwards and backwards ignoring case and spaces and False otherwise.
def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]
#Example usage
test_string = "A man a plan a canal Panama"
result = is_palindrome(test_string)
print(f'Is the string "{test_string}" a palindrome? {result}')


#Task4
#Python function either a prime checker or palindrome checker and explain it line by line in simple, student friendly language, as if teaching a beginner.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
#Example usage:
number_to_check = 29
is_number_prime = is_prime(number_to_check)
print(f'Is the number {number_to_check} prime? {is_number_prime}')
