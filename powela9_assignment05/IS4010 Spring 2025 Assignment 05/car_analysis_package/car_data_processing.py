# File Name : car_data_processing.py
# Student Name: Jay
# email: powela9@mail.uc.edu
# Assignment Number: Assignment 05
# Due Date: 2/20/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Reads a dataset containing various car attributes then performs multiple analyses
# Brief Description of what this module does: Functions for analyzing car data
# Citations: 
    #ChatGPT prompt: I have a function I need to write. Can you walk me through it step by step?
    #Then I gave what I wanted to do, the inputs, and the return.
    #Used ChatGPT to write a function to find average price of cars owned by different number of previous owners, it also generated the test case
# Anything else that's relevant:

def get_count_by_model(car_data, desired_model):
    """
    Count the number of rows in the dataset with the desired model
    @param car_data list: The list of dictionaries to process. One key in the dictionary must be "Model"
    @param desired_model String: The desired model
    @return tuple: A tuple with (count of model, list of dictionaries with that model)
    """
    count = 0
    matching_cars = []
    for car in car_data: #Iterates through whole list of dictionaries
        if car.get("Model") == desired_model:
            count += 1
            matching_cars.append(car)
    return count, matching_cars


def get_average_price_by_model(car_data, desired_models):
    """
    Calculate the average price of a list of models
    @param car_data list: The list of dictionaries to process. Must contain the keys "Model" and "Price"
    @param desired_models List of Strings: The desired models or None if all models
    @return int: The average price
    """
    filtered_prices = [
        int(car["Price"]) for car in car_data #Extract price from each car dictionary
        if desired_models is None or car["Model"] in desired_models] # Include all cars if desired_models = None, otherwise filter by model
    if not filtered_prices:
        return 0 #Avoids division by 0
    return int(sum(filtered_prices)/len(filtered_prices))
# Would not work when not turning Price into an int

def get_models_by_make(car_data, desired_make):
    """
    Calculate the models for a given make
    @param car_data list: The list of dictionaries to process. Must contain the keys "Model" and
    "Brand"
    @param desired_make String: The desired make to process
    @return set: The models for desired_make
    """
    models = {car["Model"] for car in car_data if car["Brand"] == desired_make}
    return models

def get_filtered_car_data(car_data, filters):
    """
    Filter the car data by a set of filters
    @param car_data list: The list of dictionaries to process. Must contain the keys in the filters
    paramater
    @param filters list: The desired keys in car_data
    @return list of dictionaries: rows in car_data reduced to just the columns in the filters paramater
    """
    # Create a new list of dictionaries with only the specified keys
    filtered_data = [
        {key: car[key] for key in filters if key in car}  # Keep only keys that exist in car
        for car in car_data
    ]
    return filtered_data

def average_price_by_owner_count(car_data):
    '''
    Calculate the average price of cars by the number of previous owners.
    @param car_data list: The list of dictionaries with car details.
    @return dict: A dictionary with the number of owners as keys and average prices as values.
    '''
    owner_price_totals = {}
    owner_counts = {}

    for car in car_data:
        owner_count = car["Owner_Count"]  # Ensure correct key name (case-sensitive)
        price = int(car["Price"])  # Convert price to integer

        owner_price_totals[owner_count] = owner_price_totals.get(owner_count, 0) + price
        owner_counts[owner_count] = owner_counts.get(owner_count, 0) + 1

    return {owner: round(owner_price_totals[owner] / owner_counts[owner]) for owner in owner_price_totals}