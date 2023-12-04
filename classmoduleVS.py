import math
class Place_OrderVS:
    def __init__(self,food,amount):
        self.__food = food
        self.__amount = amount
        self.__price = self.__PriceListVS()
        self.__totalPrice = self.calculatedCostVS()
    
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
        return self.__price
    
    def calculatedCostVS(self):
        return self.__amount*self.__price
    
    def getTotal(self):
        return self.__totalPrice
    
    def __str__(self):
        print(f'Item: {self.__food}')
        print(f'Amount ordered: {self.__amount} pounds')
        print(f'Price per pound: ${self.__price}')
        print(f'Price of order: ${self.__totalPrice}\n')
