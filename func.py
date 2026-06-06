#1.Write a function to check whether a number is positive, ngative or zero.
n = int(input("Enter number: "))
def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"
print(check_number(n)) 

#2. Write a function to check whether a number is even or odd.
n = int(input("Enter number: "))
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_even_odd(n)) 

#3. Write a function that accepts two numbers and return the greater number.
int1 = int(input("Enter first number:"))
int2 = int(input("Enter second number:"))
def greater_number(int1,int2):
    if int1 > int2:
        return int1
    else:
        return int2
print(greater_number(int1,int2))

#4. write a function to check a person is eligible to vote(age >=18).
age = int(input("Enter age: "))
def check_voting_eligibility(age): 
    if age >= 18:
        return "Eligible to vote"
    else:
        return "Not eligible to vote"
print(check_voting_eligibility(age))


#5. write a function to check whethera number is divisible by 5.
n = int(input("Enter number: "))
def check_divisible_by_5(n):
    if n % 5 == 0:
        return "Divisible by 5"
    else:
        return "Not divisible by 5"
print(check_divisible_by_5(n))

#6. write a function to check whether a given year is a leap year or not.
year = int(input("Enter year: "))
def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Leap year"
    else:
        return "Not a leap year"
print(check_leap_year(year))

#7. write a function to check whether a character is a vowel or consonant.
char = input("Enter character: ")
def check_vowel_consonant(char):
    if char.lower() in ['a', 'e', 'i', 'o', 'u']:
        return "Vowel"
    else:
        return "Consonant"
print(check_vowel_consonant(char))

#8. write a function to find a lagest among three numbers.
int1 = int(input("Enter first number: "))
int2 = int(input("Enter second number: "))
int3 = int(input("Enter third number: "))
def find_largest(int1, int2, int3):
    if int1 >= int2 and int1 >= int3:
        return int1
    elif int2 >= int1 and int2 >= int3:
        return int2
    else:
        return int3
print(find_largest(int1, int2, int3))


#9. write a funcction to calculate the sum of numbers from 1 to 100.
def sum_of_numbers(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s
print(sum_of_numbers(100))

#10. write a funcion that prints the multiplication table of a given number.
n = int(input("Enter number: "))
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
multiplication_table(n)

#11. write a function to calculate and return the square of a number.
n = int(input("Enter number: "))
def calculate_square(n):
    return n ** 2
print(calculate_square(n))

#12.write a function to calulate the factorial of a number using loop.
n = int(input("Enter number: "))
def calculate_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
print(calculate_factorial(n))

#13. write a function to check whether a number is prime.
n = int(input("Enter number: "))
def check_prime(n):
    if n <= 1:
        return "Not a prime number"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "Not a prime number"
    return "Prime number"
print(check_prime(n))

#14 .write a function to calculate the sum of digits of a number.
n = int(input("Enter number: "))
def sum_of_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s
print(sum_of_digits(n))

#15. write a function that accepts a number n and reurn the sum of all numbers from 1 to n.
n = int(input("Enter number: "))
def sum_of_numbers(n):
    s = 0
    for i in range(1, n + 1):
        s += i
        return s
print(sum_of_numbers(n))