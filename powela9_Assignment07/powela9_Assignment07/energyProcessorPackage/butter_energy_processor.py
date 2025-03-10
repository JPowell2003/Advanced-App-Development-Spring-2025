# File Name: butter_energy_processor.py
# Student Name: Jay Powell
# email: powela9@mail.uc.edu
# Assignment Number: Assignment 07
# Due Date: 3/06/2025
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: 
   # Analyzes energy consumption data by reading a CSV file, finding the highest recorded value, and extracting unique node names for data processing
# Brief Description of what this module does: 
   # Processes energy consumption data from a CSV file, extracts the maximum recorded value, and identifies unique computing nodes
# Citations:
    # Find max using list comprehension: https://stackoverflow.com/questions/71435200/python-list-comprehension-find-largest-number-in-sublist-using-list-comprehensi
# Anything else that's relevant: 
    # Data set: https://catalog.data.gov/dataset/butter-e-energy-consumption-data-for-the-butter-empirical-deep-learning-dataset
    # My columns:
        # - node: The name of the computing node where the measurement was taken.
        # - count: The number of experimental runs recorded for this node.
        # - min: The minimum power consumption recorded for the node.
        # - p000001, p00001, p0001, ..., p999999: Percentile-based power consumption values (e.g., p50 represents the median power consumption).
        # - max: The maximum power consumption recorded for this node.

import csv

class CSVProcessor:
    """
    A class for processing energy consumption data from a CSV file.
    """

    def __init__(self, file_name):
        """
        Initializes the CSVProcessor by reading the dataset and performing data analysis.
        Reads and stores CSV data.
        Finds the maximum value in the last column using a loop.
        Finds the maximum value in the last column using list comprehension.
        Extracts unique values from the 'node' column and prints their count and first 5 values.

        @param file_name (str): The path to the CSV file.
        """
        self.data = self.read_CSV_file(file_name)

        # Find max value using a loop
        max_value = None
        for row in self.data:
            value = float(row[-1])  # 'max' column is the last column in the dataset
            if max_value is None or value > max_value:
                max_value = value
        print(f"Maximum value in the last column: {max_value}")

        # Find max value using list comprehension
        max_value_lc = max([float(row[-1]) for row in self.data])
        print(f"Maximum value in the last column (list comprehension): {max_value_lc}")

        # Extract unique values from the 'node' column
        unique_nodes = {row[0] for row in self.data}
        print(f"Number of unique nodes: {len(unique_nodes)}")
        print(f"First 5 unique nodes: {list(unique_nodes)[:5]}")

    def read_CSV_file(self, file_name):
        """
        Reads a CSV file and returns its data as a list of lists.

        @param file_name (str): The path to the CSV file. 
                                The file should have a header row, which is skipped.

        @return list: A list of lists containing the dataset (excluding the header row).
        """
        csv_data = []
        with open(file_name, newline='', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=',')
            header = next(reader)  # Skip the header row
        #   csv_data.append(header)  # Commented out: we don't want the header row.
            for row in reader:
                csv_data.append(row)

        return csv_data
