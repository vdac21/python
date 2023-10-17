costprice=input("enter the cost price: ")
sellingprice=input("enter the selling price: ")
if(costprice-sellingprice>0):
    amount=costprice-sellingprice
    print("profit price")
elif(sellingprice-costprice):
    amount=sellingprice-costprice
    print("loss price")
else:
    print("no profit no loss")
