#main.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu

from ListProcessingPackage.listProcessing import *

if __name__ == "__main__":
    students = initializeStudents()
    print(students)
    # Print the data type of students
    print("The data type of students is", type(students))
    # Print the elements of the list one-at-a-time with a for/in loop
    print_students(students)
    # Add an element to the list (another student)
    new_list = add_student_to_list(["Powell", "Jay", "M1467365", "Business Analytics"], students)
    print_students(new_list)

    # Apply List Comprehension
    #Print the last names using List Comprehension
    print_last_names(students)
    #Print the first names of just students in IS
    print_first_names_of_students_in_IS(students)

    # Search the list
    
