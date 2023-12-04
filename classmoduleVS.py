import math
class Place_OrderVS:
    def __init__(self,food,amount):
        self.__food = food
        self.__amount = amount
        self.__price = self.__price
        self.__totalPrice = 0
    
    def __PriceListVS(self):
        if self.__food == 'Dry Cured Iberian Ham':
            self.__price = 177.80
        elif self.__food == 'Wagyu Steaks':
            self.__price = 450.00
        elif self.__food == 'Matsutake Mushrooms':
            self.__price = 272.00
        elif self.__food == 'Kopi Luwak Coffee':
            self.__price = 306.50
        elif self.__food == 'Moose Cheese':
            self.__price = 487.20
        elif self.__food == 'White Truffles':
            self.__price = 3600.00
        elif self.__food == 'Blue Fin Tuna':
            self.__price = 3603.00
        elif self.__food == 'Le Bonnotte Potatoes':
            self.__price = 270.81
        else:
            self.__price = 0.00
    
    def calculatedCostVS(self):
        self.__totalPrice = self.__amount*self.__price
        return self.__totalPrice
    
