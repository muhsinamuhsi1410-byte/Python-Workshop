print("***Bill Calculator***")
item=input("Enter the item name:")
price=float(input("enter the item price"))
quantity=int(input("Enter quantity"))
total=price*quantity
gst=total*0.05
grand_total=total+gst
print("\n--------BILL-----")
print("item :",item)
print("Price:",price)
print("Quantity:",quantity)
print("Total:",total)
print("GST(5%):",gst)
print("Grand Total:",grand_total)
if grand_total>=1000:
 print("You are eligible for a discount")
else:
 print("No discount available")
print("Thank you for shopping")