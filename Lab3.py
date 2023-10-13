#Task1
N = int(input("Enter a positive integer: "))
i = 2
while i <= N:
    print(i)
    i += 2

#Task2
N = int(input("Enter a positive integer: "))
factorial = 1
while N > 0:
    factorial *= N
    N -= 1
print("Factorial:", factorial)

#Task3
while True:
    number = int(input("Enter a number: "))
    if number == 42:
        print("Found 42! Terminating.")
        break

#Task4
string = input("Enter a string: ")
count = string.count("a")
print("Number of 'a's:", count)

# Task5
number = input("Enter a number: ")
digit_sum = sum(int(digit) for digit in number)
print("Sum of digits:", digit_sum)

# Task6
N = int(input("Enter a positive integer: "))
a, b = 0, 1
while N > 0:
    print(a)
    a, b = b, a + b
    N -= 1


#Task7
string = input("Enter a string: ")
reverse_string = string[::-1]
print("Reversed string:", reverse_string)

# Task8
sum_odd = 0
while True:
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        continue
    sum_odd += number
    print("Sum of odd numbers:", sum_odd)

# Task8
import random

target_number = random.randint(1, 100)
while True:
    guess = int(input("Guess the number (1-100): "))
    if guess < target_number:
        print("Too small")
    elif guess > target_number:
        print("Too large")
    else:
        print("You guessed it!")
        break

# Task9
string = input("Enter a string: ")
if string == string[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


    X = int(input("Enter the base (X): "))
Y = int(input("Enter the power (Y): "))
result = 1
while Y > 0:
    result *= X
    Y -= 1
print(f"{X} to the power {Y} is {result}")

Task
N = int(input("Enter a positive integer (N): "))
num = 2
while num <= N:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')
    num += 1

number = input("Enter a number: ")
reverse_number = number[::-1]
print("Reversed number:", reverse_number)


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
while True:
    if is_prime(number):
        print(f"{number} is prime.")
        break
    else:
        number += 1
        continue



def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = chr(((ord(char) - ord('A' if is_upper else 'a') + shift) % 26) + ord('A' if is_upper else 'a'))
        result += char
    return result

text = input("Enter a string: ")
shift = int(input("Enter the shift value (N): "))
encrypted_text = caesar_cipher(text, shift)
print("Encrypted string:", encrypted_text)
