def discountCalc(price, discount):
    if(discount > 1):
        #if the discount is in %
        return (price - (price * (discount / 100)))
    else:
        #if the discount was given in decimal
        return price - (price * discount)
newPrice = discountCalc(100, 20)
print(newPrice)
newPrice = discountCalc(50, .40)
print(newPrice)