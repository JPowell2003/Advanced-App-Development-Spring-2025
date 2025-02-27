# File Name: mainDishes.py
# Student Name: Jay Powell
# email: powela9@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date: 2/27/2025
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: 
   # This assignment develops a Python project to model a fast-food order with a main meal, side, and drink
# Brief Description of what this module does: 
   # The MainDish class models a main dish item in a fast-food order, storing its name, quantity, and calculating the total price based on a shared price list
# Citations: 
# Anything else that's relevant: 

class RestaurantOrder:
    """
    Models a Main Course Meal in a fast-food order.
    """

    def __init__(self, main_course=None, quantity=1):
        """
        Initialize a restaurant order with a main course and quantity.
        @param main_course String: The selected main course (Burger, Chicken Sandwich, Sliders)
        @param quantity int: The number of items ordered (must be at least 1)
        @raises ValueError: If the main course is not in the menu.
        @raises ValueError: If quantity is less than 1.
        """
        
        self.menu = {
            "Burger": 10.99,
            "Chicken Sandwich": 9.99,
            "Sliders": 8.99
        }
        
        if main_course is None or main_course not in self.menu:
            raise ValueError("A valid main course must be selected.")
        
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        
        self._main_course = main_course
        self._quantity = quantity 

        self.set_main_course(main_course)  
        self.set_quantity(quantity)  
    
  
    
    def get_main_course(self):
       """
       Retrieve the current main course selection.
       @returns String: The name of the selected main course.
       """       
       return self._main_course
    
   
    
    def set_main_course(self, value):
        """
        Update the main course selection.
        @param value String: The new main course selection.
        @raises ValueError: If the selected main course is not in the menu.
        """
                
        if value not in self.menu:
            raise ValueError("Invalid main course selection.")
        self._main_course = value
    
    
    
    def get_quantity(self):
        """
        Retrieve the current quantity of the main course ordered.
        @returns int: The number of main courses ordered.
        """       
        
        return self._quantity
    
    
    
    def set_quantity(self, value):
        """
        Update the quantity of the main course ordered.
        @param value int: The new quantity value.
        @raises ValueError: If the quantity is less than 1.
        """        
        if value < 1:
            raise ValueError("Quantity must be at least 1.")
        self._quantity = value
    
    
    def calculate_total(self):
        """
        Calculate the total price of the order.
        @returns float: The total price of the order.
        """        
        return self.menu[self._main_course] * self._quantity
    
    def __str__(self):
        """
        Generate a string representation of the order.
        @returns String: A formatted string showing the order details, including main course, quantity, and total price.
        """
        return f"Order: {self._quantity} x {self._main_course} - Total: ${self.calculate_total():.2f}"