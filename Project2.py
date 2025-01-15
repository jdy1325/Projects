import math

itemQuan = 5
price = 1.98
totalSale = (itemQuan * price)
totalTax = totalSale * 0.04
totalCost = totalSale + totalTax


print("The total cost of the 5 items with sales tax is: " , "%.2f"%totalCost)
