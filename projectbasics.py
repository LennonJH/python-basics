#Variables and Types
name = "Lennon Jambo Habeenzu"
age = 37
city = "Lusaka"
print(f"My name is {name}, I am {age}, from {city}.")

#Conditions: Write a program that takes a score and print a grades
above_90 = "A"
above_75 = "B"
above_60 = "C"
below_60 = "F"
score = 78
if score >= 90:
    print("A")
elif score >= 75:
    print("B")

#Loops: Print the first 10 even numbers using a loop.
for i in range(1,21):
    if i%2 == 0:
        print(i)

#Challenge: Ask the user for a number and print its multiplication table
import math 
num = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{num}x{i}={num*i}")
