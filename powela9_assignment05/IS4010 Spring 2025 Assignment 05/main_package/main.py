# File Name : main.py
# Student Name: Jay
# email: powela9@mail.uc.edu
# Assignment Number: Assignment 05
# Due Date: 2/20/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Reads a dataset containing various car attributes then performs multiple analyses
# Brief Description of what this module does: Reads a dataset of car prices, performs various analyses, and prints the results.
# Citations: Used ChatGPT to write a function to find average price of cars owned by different number of previous owners, it also generated the test case
# Anything else that's relevant:


from data_utilities_package.data_utilities import *
from car_analysis_package.car_data_processing import *

if __name__ == "__main__":
    cars = read_car_price_dataset()
    print(len(cars), "rows read.")
    print("First:", cars[0])
    print("Last:", cars[-1])
    print("------------------------") 
    desired_model = "Camry"
    result = get_count_by_model(cars, desired_model)
    print(desired_model, "count:", result[0])
    print("------------------------")

    average_price_of_all_models = get_average_price_by_model(cars, None)
    print("Average price of all models:", average_price_of_all_models)
    print("------------------------")

    desired_models = ["Camry"]
    average_price_of_camry = get_average_price_by_model(cars, desired_models)
    print("Average price of ", desired_models, ":", average_price_of_camry)
    print("------------------------")
    
    desired_models = ["Camry", "RAV4"]
    average_price_of_camry = get_average_price_by_model(cars, desired_models)
    print("Average price of ", desired_models, ":", average_price_of_camry)
    print("------------------------")

    desired_make = "Toyota" 
    models_of_toyota = get_models_by_make(cars, desired_make)
    print("All models for", desired_make, ":", models_of_toyota)
    print("------------------------")
    
    desired_filters = ["Brand", "Model", "Price"]
    result = get_filtered_car_data(cars, desired_filters)
    # Just print the first and last row to be reasonably sure we are correct
    print("Car Data with reduced columns:", desired_filters)
    print("First:", result[0])
    print("Last:", result[-1])

    # Implement function to see how number of owners affects car price
    print("------------------------")
    average_price_by_owner = average_price_by_owner_count(cars)
    print("Average price based on number of previous owners:")
    for owners, price in sorted(average_price_by_owner.items()):
        print(owners, "owners:", price)


