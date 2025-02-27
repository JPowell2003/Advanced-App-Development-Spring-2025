# data_utilities.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu

import csv

def read_car_price_dataset():
    """
    Load the car_price_dataset from Kaggle into a list of dictionaries.
    https://www.kaggle.com/datasets/asinow/car-price-dataset/data
    @return list: the list of dictionaries
    """
    data = []
    filename = "Data/car_price_dataset.csv"
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data
