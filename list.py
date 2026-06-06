# 1. create a list of 10 numbers and print all the elements.
numbers = [1,2,3,4,5,6,7,8,9,10]
for num in numbers:
    print(num)
    
#2. write a program to find a largest element in a ist.
numbers = [18,7,45,33,93,17]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest =num
print(largest)

#3 write a program to find a smallest element in a ist.
numbers = [18,7,45,33,93,17]
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
print(smallest)

#4. write a program to calculate sum of elements in a list.
numbers = [12,45,76,87,34,55]
total = 0
for num in numbers:
    total += num
print(total)

#5. write a program to calculate average of elements in a list.
numbers = [12,45,76,87,34,55]
total = 0
for num in numbers:
    total += num
    average = total / len(numbers)
print(average)

#6. write a program to count how many prime numbers are present in a list.
numbers = [2,4,6,5,3,8,9,12,54,67,32,99,65]
count = 0
for num in numbers:
    if num % 2 == 0:
        count += 1
print("Even numbers:", count)

#7.Write a program to create a new list containing only the odd numbers from an existing list. 
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = []
for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)
print(odd_numbers)

#8.	Write a program to find whether a given element exists in a list. 
numbers = [10, 20, 30, 40, 50]
element = 30
if element in numbers:
    print("Element found")
else:
    print("Element not found")


#9.	Write a program to reverse a list without using built-in reverse functions. 
nums = [1, 2, 3, 4, 5]
rev = []
for x in nums:
    rev = [x] + rev
print(rev) 


#10.	Write a program to find the second largest element in a list.
nums = [12, 35, 1, 10, 34]
largest = max(nums)
nums.remove(largest)
second = max(nums)
print(second) # 34