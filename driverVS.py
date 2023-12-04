from classmoduleVS import Place_OrderVS
foodItems = dict()
def orderVS():
    while True:
        numItems=int(input("How many items will you order today?:"))
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

cost=list()
def display_itemsVS(food):
    print("\nHere's a summary of  the items purchased:")
    print("**********\n")
    for x,y in food.items():
        item = Place_OrderVS(x,y)
        item.__str__()
        cost.append(item.getTotal())
    return cost

def totalCostVS(cost):
    cost = sum(cost)
    print(f'TOTAL COST: ${cost}')

def groceryVS():
    orderVS()
    display_itemsVS(foodItems)
    totalCostVS(cost)

groceryVS()
