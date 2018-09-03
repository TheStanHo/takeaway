
print('Welcome to Eastern Express, please enter the number of the item you wish to order.\nOnce finished please type Finished to place the '
      'order. May I take your order?')
menu = {'1': 'Chicken Rice', '3': 'Chicken Balls'}
price = {'Chicken Rice': 3.50, 'Chicken Balls': 2.60}
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
        print("Your order current order is: " )
        print(orderedFood)
        total.append(price.get(menu.get(order)))

totalPrice = sum(total)

print("The total price of your order is £" + totalPrice)

type(order)
