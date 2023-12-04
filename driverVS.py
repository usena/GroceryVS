from classmoduleVS import Place_OrderVS
def orderVS():
    foodItems={}
    while True:
        numItems=int(input("How many items will you order today?: "))
        if numItems >= 1:
            
            break
        else:
            print('Number of items must be at least 1.')
            
    for x in range(numItems):
        print(f'Item #{x+1}')
        itemName = input("Enter food: ")
        while True:
            itemAmount = float(input("Enter amount of pounds: "))
            if itemAmount > 0:
                break
            else:
                print('Amount of pounds must be greater than 0.')
        foodItems[itemName]=itemAmount
    return foodItems

def display_itemsVS(food):
    cost = []
    print("Here's a summary of  the items purchased: ")
    for x,y in food:
        item = Place_OrderVS()
        item.__init__(x,y)
        item.__PriceListVS()
        item.calculatedCostVS()
        print(f'Item: {item.__food} \n Amount ordered: {item.__amount} pounds \n Price per pound: {item.__price} \n Price of order: {item.__totalPrice}')
        cost.append(item.__totalPrice)

def totalCostVS(cost):
    cost = sum(cost)
    return f'Total cost: ${cost}'

def groceryVS():
    orderVS()
    display_itemsVS(foodItems)
    