# --------------
# Code starts here

# Create the lists 
class_1 = ['Geoffrey Hilton', 'Andrew Ng', 'Sebastian Raschka', 'Yoshua Bengio']
class_2 = ['Hilary Mason', 'Carla Gentry', 'Corinna Cortes']

# Concatenate both the strings
new_class = class_1 + class_2
print("Concetaned List: ", new_class)

# Append the list
new_class.append('Peter Warden')

# Print updated list
print("Updated List: ", new_class)

# Remove the element from the list
new_class.remove('Carla Gentry')
# Print the list
print("Updated List: ", new_class)


# Create the Dictionary
courses = {'Math':65, 'English':70, 'History':80, 'French':70, 'Science':60}
print(courses)

# Slice the dict and stores  the all subjects marks in variable
value = courses.values()
print("Marks in each subj: ", value)
# Store the all the subject in one variable `Total`
Total = sum(value)
# Print the total
print("Total: ", Total)
# Insert percentage formula
percentage = Total*100/500
# Print the percentage
print("Percentage: ", percentage)



# Create the Dictionary
mathematics = {'Geoffrey Hinton':78, 'Andrew Ng':95, 'Sebastian Raschka':65, 'Yoshua Benjio':50, 'Hilary Mason':70, 'Corinna Cortes':66, 'Peter Warden':75} 

topper = max(mathematics,key=mathematics.get)
print("Highest Marks in Maths: ",topper)

# Given string


# Create variable first_name 
first_name = topper.split()[0]
print("First Name: ",first_name)
# Create variable Last_name and store last two element in the list
last_name = topper.split()[1]
print("Last Name: ",last_name)
# Concatenate the string
full_name = last_name + ' ' + first_name
# print the full_name
print("Full Name: ",full_name)
# print the name in upper case
certificate_name = full_name.upper()
print("Certificate Name: ",certificate_name)
# Code ends here


