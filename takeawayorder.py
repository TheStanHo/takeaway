
print('Welcome to Eastern Express, please enter the number of the item you wish to order.\nOnce finished please type Finished to place the '
      'order. May I take your order?')
menu = {'1': 'Chicken Rice', '3': 'Chicken Balls'}
price = {'Chicken Rice': 3.51, 'Chicken Balls': 2.60}
total =[]
orderedFood = []
while True:
    order = input("What is the number of your order? ")

    if order == "Finished":
        break

    elif order not in menu:
        print('Menu Item not found ')
    else:
        orderedFood.append(menu.get(order))
        print ("Your order current order is: " )
        orderedFood.sort()
        for e in orderedFood:
            print(e + " £" + str(round(price.get(e),2)))
        total.append(price.get(menu.get(order)))

totalPrice = sum(total)

print("The total price of your order is £" + str(round(totalPrice,2)))


type(order)
