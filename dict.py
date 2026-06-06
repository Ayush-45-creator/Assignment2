#1.	Create a dictionary to store a student's name, age, and city, and print the dictionary. 
student = {"name": "Ayush", "age": 20, "city": "Mumbai"}
print(student)

#2.	Write a program to print all the keys of a dictionary. 
student = {"name": "Ayush", "age": 20, "city": "Mumbai"}
for key in student:
    print(key)


#3.	Write a program to print all the values of a dictionary.
student = {"name": "Ayush", "age": 20, "city": "Mumbai"}
for value in student.values():
    print(value) 


#4.	Write a program to add a new key-value pair to an existing dictionary. 
student = {"name": "Ayush", "age": 20}
student["city"] = "Mumbai"
print(student)


#5.	Write a program to update the value of an existing key in a dictionary.
student = {"name": "Ayush", "age": 20}
student["age"] = 21
print(student) 


#6.	Write a program to check whether a given key exists in a dictionary. 
student = {"name": "Ayush", "age": 20}
if "name" in student:
    print("Key exists")
else:
    print("Key does not exist")


#7.	Write a program to remove a key-value pair from a dictionary. 
student = {"name": "Ayush", "age": 20, "city": "Mumbai"}
del student["city"]
print(student)


#8.	Write a program to count the total number of key-value pairs in a dictionary. 
student = {"name": "Ayush", "age": 20, "city": "Mumbai"}
print(len(student))


#9.	Write a program to iterate through a dictionary and print all keys and their corresponding values. 
student = {"name": "Ayush", "age": 20, "city": "Mumbai"}
for key, value in student.items():
    print(key, ":", value)


#10.	Create a dictionary of student names and marks, then find the student with the highest marks.
marks = {"Ayush": 85, "Rahul": 92, "Riya": 88}
top_student = max(marks, key=marks.get)
print("Highest Marks Student:", top_student)
print("Marks:", marks[top_student])
