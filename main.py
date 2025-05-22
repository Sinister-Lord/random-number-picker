import random

numbers = [3, 7, 14, 21, 36, 42, 58, 63, 77, 89]
secret_number = random.choice(numbers)

print("Welcome, Harsh! Try to guess the number chosen by the judge.")
print(f"Here is the list: {numbers}")

guess = int(input("Enter your guess: "))

if guess == secret_number:
    print("Congratulations! You guessed the correct number.")
elif guess > secret_number:
    print("Too high! Try guessing a smaller number.")
else:
    print("Too low! Try guessing a larger number.")

