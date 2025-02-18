#main.py

from avocadoPackage.Avocado import *

if __name__ == "__main__":
    '''
    #Commented out due to breaking after adding a new constructor
    #Instantiate an object of type avocado
    myAvocado = Avocado() #Implicitly invokes the constructor
    print(type(myAvocado))

    myAvocado.set_price(0.96)
    print("Price of our Avocado is ", myAvocado.get_price(), " cents")

    myAvocado.set_weight(0.33)
    print("The average weight of an Avocado is roughly ", myAvocado.get_weight(), " pounds")

    #Instantiate another avocade called tjAvocado. It cost 4.00 and weighs .98 grams
    tjAvocado = Avocado()
    tjAvocado.set_price(4.00)
    tjAvocado.set_weight(0.98)
    print("Trader Joes Avocado: ", tjAvocado.get_weight(), tjAvocado.get_price())
    '''
    # At this point we realize we have a problem: we can have avocados with no price 
    # and no weight. To fix this let's add another constructor that accepts weight and price
    newAvocado = Avocado(1.50, 0.80) #New constructor
    print("New Avocado: ", newAvocado.get_weight(), newAvocado.get_price())

    print(newAvocado.__str__())