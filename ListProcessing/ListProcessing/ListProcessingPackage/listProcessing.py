# listProcessing.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu

def print_first_names_of_students_in_IS(students):
    '''
    Print the first names of students in the Information Systems major
    @param students list: the existing list of students to process
    @return none
    '''
    print([student[1] for student in students if student[3] == "Information Systems"])

def print_last_names(students):
    '''
    Print the last name of all the students
    @param students list: the existing list of students to process
    @return none
    '''
    print([student[0] for student in students])

def add_student_to_list(new_student, students):
    '''
    Add a student to existing list
    @param new_student: The new student to add
    @param students list: the existing list of students
    @return the new list with the student added
    '''
    students.append(new_student)
    return students

def print_students(students):
    '''
    Print the elements in the list one-by-one
    @parameters students list: The list of things to process
    @return None
    '''
    for student in students:
        print(students)

def initializeStudents():
    """
    Create a dataset of students to work with.
    @return list: The initialized list. Actually, a list of lists
    """
    data = []    # An empty list
    student = ["Smith", "Bob", "M02635916", "Information Systems"]
    data.append(student)
    student = ["Miller", "Mary", "M02635922", "Information Systems"]
    data.append(student)
    student = ["Burlew", "Cecelia", "M02635987", "BANA"]
    data.append(student)
    student = ["Cheaney", "Calbert", "M04435987", "Computer Science"]
    data.append(student)
    return data

if __name__ == "__main__":
    print(initializeStudents())