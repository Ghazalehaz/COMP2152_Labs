#Q1
grades = [85, 92, 78, 95, 88]
grades.append(90)
grades.sort()
print(f"sorted grades: {grades}")
print(f"sorted grades: ", grades)
print(f"Highest grade: {grades[-1]}")
print(f"Lowest grade: {grades[0]}")
print(f"Total number of grades: {len(grades)}")


#Q2
cart = ["apple", "banana","milk","bread","apple","eggs"]
apple_count = cart.count("apple")
print(f"Number of apples: {apple_count}")
milk_position = cart.index("milk")
print(f"Position of milk:{milk_position}")
cart.remove("apple") #using remove 
remove_item = cart.pop()
print(f"Removed item using pop : {remove_item}")
print ("Is banana in cart? ", "banana" in cart)



#Q3
point1 = (3, 5) 
point2 = (7, 2)
x1, y1 = point1
x2, y2= point2
print(f"X1 = {x1},y1= {y1}")
print(f"X2 = {x2},y1= {y2}")
distance = ( (x2 - x1) ** 2 + (y2 - y1) ** 2) **0.5
print("Distance between points:", distance)


#Q4 
monday_class = {"Alice", "Bob", "charlie","Diana"}
wedensday_class = { "Bob", "Diana","Eve","Frank"}
monday_class.add("Grace")
print(f"Monday class: {monday_class}")
print(f"Wedensday class: {wedensday_class}")
print(f"Attended both classes: {monday_class & wedensday_class}") 
print(f"Attended either classes: {monday_class | wedensday_class}") 
print(f"only monday: {monday_class - wedensday_class}") 
print(f"only one: {monday_class ^ wedensday_class}") 
allStudent = monday_class | wedensday_class
print ("Is monday subset of all students", monday_class <= allStudent)



#Q5
contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}

print(f"Alice's number: {contacts['Alice']}")

contacts["Diana"] = "555-4321"
print(f"Contacts after adding Diana: {contacts}")

contacts["Bob"] = "555-0000"
print(f"Contacts after updating Bob: {contacts}")

del contacts["Charlie"]
print(f"Contacts after deleting Charlie: {contacts}")

print(f"All names {contacts.keys()}")
print(f"All numbers {contacts.values()}")
print(f"Total contacts {len(contacts)}")