#functions.py

#Iterate
def iterate_over_dictionary(my_dictionary):
    """
    Use iteration to process the elements in the dictionary and print them
    @param my_dictionary dict: the data to process
    @return None (default)
    """
    for element in my_dictionary:
        print(element) #Prints just the keys
        print(element, my_dictionary[element]) #Print the key and the associated value

    #Another strategy to iterate over a dictionary
    for key, value in my_dictionary.items(): #Populates both of those, prints both the key and the associated value
        print(key,value)


#Search/lookup
def search_by_key(desired_key, my_dictionary):
    """
    Use a key to look up a value in a dictionary
    @param desired_key string: the key to use
    @param my_dictionary dict: the data to process
    @return String: The value associated with desired_key, or None on exception
    """
    #Code Bill used
    try:
       return my_dictionary[desired_key] #Will fail if the key doesn't exist
    except:
        return None

    #Code I used:
    #Source: https://www.w3schools.com/python/ref_dictionary_get.asp
    #dictionary.get(keyname, value), value is what returns if the key doesn't exist in this case None
    # return my_dictionary.get(desired_key, None)

#Add value to dictionary
def add_element_to_dictionary(addedKey, addedValue, my_dictionary):
    """
    Add a new key and value to a dictionary
    @param addedKey string: The key to add
    @param addedValue string: The value to add
    @param my_dictionary dict: The data to process
    @return None
    """
    #Source: https://stackoverflow.com/questions/52466372/adding-key-and-value-to-a-dictionary-within-a-function-in-python
    #I took the second comment
    try:
        my_dictionary[addedKey] = addedValue  # Add the new key-value pair
    except:
        pass

#Remove a value to dictionary
def remove_by_key(key, my_dictionary):
    """
    Remove a key and value from a dictionary by the key
    @param key string: The key to remove
    @param my_dictionary dict: The data to process
    @return None
    """
    #Source: https://www.w3schools.com/python/gloss_python_remove_dictionary_items.asp
    try:
       del my_dictionary[key]
        #my_dictionary.pop(key, None) will also delete the item, but return none if the value doesn't exist
    except:
       pass