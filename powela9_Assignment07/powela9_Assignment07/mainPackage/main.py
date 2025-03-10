# File Name: main.py
# Student Name: Jay Powell
# email: powela9@mail.uc.edu
# Assignment Number: Assignment 07
# Due Date: 3/06/2025
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: 
   # Analyzes energy consumption data by reading a CSV file, finding the highest recorded value, and extracting unique node names for data processing
# Brief Description of what this module does: 
   #  Initializes the CSVProcessor class to read and process energy consumption data from the node_power_dist.csv file
# Citations: 
# Anything else that's relevant: 

from energyProcessorPackage.butter_energy_processor import CSVProcessor

if __name__ == "__main__":
    processor = CSVProcessor("./Data/node_power_dist.csv")
