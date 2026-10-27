cart=[]
cart.append({"item":"Book","price" :200})
cart.append({"item":"Pen","price":20})
total=sum(i["price"] for i in cart)
discount=total*0.1 if total>500 else 0
print(f"Items: {cart}")
print(f"Total {total} Discount {discount} Final {total-discount}")