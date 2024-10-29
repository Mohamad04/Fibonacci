
# Fibonacci
# Create a program that prompts the user to enter a number n and generates the first n Fibonacci numbers.

# The Fibonacci sequence is a series of numbers in which each number (after the first two) is the sum of the two preceding ones. 
# It typically starts with 0 and 1. First Few Numbers: 0,1,1,2,3,5,8,13,21,34,55,89,144,…



user_input = int(input("Enter your number : "))
last_nb = 1
second_last_nb = 0
third_last_nb = 0

for i in range(user_input-1):
    third_last_nb = second_last_nb
    second_last_nb = last_nb
    last_nb = second_last_nb + third_last_nb
    
print(last_nb)