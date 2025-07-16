product_id = int(input("Enter Product ID: "))
product_name = input("Enter Product Name: ")
price = float(input("Enter Product Price (₹): "))
categories = input("Enter Categories (comma-separated): ").split(",")
available_stock = int(input("Enter Stock Available: "))
sold_stock = int(input("Enter Units Sold: "))
stock_details = (available_stock, sold_stock)
discount = float(input("Enter Discount Percentage: "))
features = set(input("Enter Product Features (comma-separated): ").split(","))
seller_name = input("Enter Seller Name: ")
seller_contact = input("Enter Seller Contact Number: ")
seller_location = input("Enter Seller Location: ")
seller_details = {
    "name": seller_name,
    "contact": seller_contact,
    "location": seller_location
}
print("\n Flipkart Product Info ")
print("Product ID, Name, Price:", product_id, product_name, price, sep=",")
print("Product Discount: %.2f%%" % discount) 
print(f"Product: {product_name}")
print(f"Price: ₹{price}")
print(f"Discount: {discount}%")
print(f"Stock Available: {stock_details[0]} units")
print(f"Stock Sold:{stock_details[1]} units")
print("Seller Info: Name - {}, Contact - {}, Location - {}".format(
    seller_details["name"],
    seller_details["contact"],
    seller_details["location"]
))
