fruit = "Banana"

color = input(f"What is the color of your {fruit}:")

if fruit == "Banana":
    if (color == "brown"):
        print(f"Your {fruit} is Overripe")
    elif (color == "green"):
        print(f"Your {fruit} is Underripe")
    elif (color == "yellow"):
        print(f"Your {fruit} is Ripe")
    else:
        print("Please a valid condition brown, green or yellow")

print("--------------------------------------------------------------------------")

password = "reans"

if len(password) < 3:
    print("Weak")
elif len(password) > 3 and  len(password) <=6 :
    print("medium")
else:
    print("Strong")

print("--------------------------------------------------------------------------")

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

positive_number_count = 0
for num in numbers:
    if num > 0:
        positive_number_count += 1
print("Final count of Positive number is: ", positive_number_count)

print("--------------------------------------------------------------------------")
n = 10
sum_even = 0

for i in range(1, n+1):
    if i%2 == 0:
        sum_even += 1

print("Sum of even number is: , ", sum_even)

print("--------------------------------------------------------------------------")

number = 3

for i in range(1, 11):
    if i == 5:
        continue
    print(number, 'x', i, '=', number * i)

print("--------------------------------------------------------------------------")
input_str = "Python"
reversed_str = ""

for char in input_str:
    reversed_str = char + reversed_str  

print(reversed_str)
print("--------------------------------------------------------------------------")

input_str = "teeteracdacd"

for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("Char is: ", char)
        break
print("--------------------------------------------------------------------------")
number = 5
factorial = 1

while number > 0:
    # factorial = factorial * number
    # number = number - 1
    factorial *= number
    number -= 1

print("Factorial: ", factorial)

print("--------------------------------------------------------------------------")
while True:
    number = int(input("Enter value b/w 1 and 10: "))
    if 1 <= number <= 10:
        print("Thanks")
        break
    else:
        print("Invalid number, try again")
print("--------------------------------------------------------------------------")
number = 28

is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break

print(is_prime)
print("--------------------------------------------------------------------------")
items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate: ", item)
        break
    unique_item.add(item)
print("--------------------------------------------------------------------------")
import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attempt", attempts + 1, "- wait time", wait_time, )
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
print("--------------------------------------------------------------------------")
