# avocado.py
# Jay Powell
# powela9@mail.uc.edu

#Model an avocado. Context: for sale in the produce aisle at a grocery store
class Avocado:
    '''
    Model an avocado for sale in the produce aisle of a grocery store
    '''
    #This constructor gets over written by the one at the bottom
    def __init__(self): #Constructor, invoked every time an object of this type is instantiated
        '''
        Right now, no parameters and it returns nothing
        '''
        print("I am the Avocado constructor")

    #Create a getter and a setter for the price property of the current object
    def set_price(self, price):
        '''
        Setter for the price property of the avocado
        @param price float: Price of the Avocado
        '''
        #Ensure the price of the avocado doesn't cost a negative amount
        if price <= 0 :
            raise ValueError("Price of an Avocado cannot be negative")
        self.__price = price #__ prefix is a convention to indicate an object variable

    def get_price(self):
        '''
        Getter for the price property of the avocado
        @return price of avocado
        '''
        return self.__price

    #Add a getter and a setter for the weight of the current object
    def set_weight(self,weight):
        '''
        Setter for the weight property of the Avocado
        @param weight float: Weight of the avocado
        '''
        #Ensure the price of the avocado doesn't cost a negative amount
        if weight <= 0 :
            raise ValueError("Weight of an Avocado cannot be negative")
        self.__weight = weight

    def get_weight(self):
        '''
        Getter for the weight property of the Avocado
        @return weight of avocado
        '''
        return self.__weight

    def __init__(self, price = None, weight = None): #To fix this constructor over writting the first one default the arguments
        '''
        @param price float: price of an avocado
        @param weight float: weight of an avocado
        '''
        self.__price = price
        self.__weight = weight

    #Require an __str__ in all classes we make
    def __str__(self):
        '''
        @return a string representation of the current object
        '''
        summary = "weight = " + str(self.__weight) + ", price = " + str(self.__price)
        return summary