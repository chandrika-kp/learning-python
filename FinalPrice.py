itemNames = ["Tv","Mobile","Fridge"]
itemPrices = [12000,7000,18000]
itemDiscounts = [ 20,10,15 ]

selectItem = input("Enter item name: ")
# print("selected item is: " + selectItem)

if selectItem in itemNames:
    quantity = input("Enter the quantity: ")
    itemIndex = itemNames.index(selectItem)
    itemPrice = itemPrices[itemIndex]
    itemDiscount = itemDiscounts[itemIndex]
    totalPrice = itemPrice * int(quantity)
    discount = float(totalPrice) * (itemDiscount/100)
    finalPrice = float(totalPrice)-float(discount)
    print("Final price of '" + str(selectItem) + "' with "+ str(quantity) + " units of quantity = RS " +str(finalPrice))
else:
    print("oops! out of stock ")