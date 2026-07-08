shopping_cart = [
    ['apple', 'banana', 'orange'],
    ["milk", "cheese", "butter"],
    ["chicken", "beef", "pork"]
]
print(f"First item in the dairy: {shopping_cart[1][0]}")
shopping_cart[2].append("turkey")
print(f"Updated item in the meat section: {shopping_cart[2][3]}")
print("\n---My Shopping Cart---")
for department in shopping_cart:
    for item in department:
        print(f"- {item}")