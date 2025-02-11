#main.py
#IS4010-001 Boilerplate

from dictionary_package.functions import *

if __name__ == "__main__":
    #Create and assign a dictionary
    #dictionary_name = {"key":"value"}
    myDictionary = {"Cincinnati":"Bearcats", "Xavier":"Musketeers", "NKU":"Norse", "UC Clermont":"Cougars"}
    print(myDictionary)
    print(type(myDictionary))

    iterate_over_dictionary(myDictionary) #Iterate function call

    key_I_want = "Xavier"
    my_value = search_by_key(key_I_want,myDictionary) #Search in a dictionary for a key
    print(my_value)

    add_element_to_dictionary("Ohio State", "Buckeyes", myDictionary) #Key, value, dictionary
    print(myDictionary)

    remove_by_key("Ohio State", myDictionary)
    print(myDictionary)