products = {
    "Rice": 50,
    "Sugar": 40,
    "Oil": 120
}

bill_items = []


def add_item():
    name = input("Add item: ").strip().title()

    if name not in products:
        print("Invalid product. Available: Rice, Sugar, Oil")
        return

    try:
        quantity = int(input("Quantity: "))
    except ValueError:
        print("Invalid quantity")
        return

    if quantity <= 0:
        print("Invalid quantity")
        return

    amount = products[name] * quantity
    bill_items.append((name, quantity, amount))
    print(f"{name} x{quantity} added | Amount: {amount}")


def generate_bill():
    if not bill_items:
        print("No items in bill")
        return

    subtotal = sum(item[2] for item in bill_items)
    gst = subtotal * 0.05
    grand_total = subtotal + gst

    bill = []
    bill.append("========== BILL ==========")

    for name, quantity, amount in bill_items:
        bill.append(f"{name} x{quantity} = {amount:.2f}")

    bill.append(f"Subtotal: {subtotal:.2f}")
    bill.append(f"GST (5%): {gst:.2f}")
    bill.append(f"Grand Total: {grand_total:.2f}")
    bill.append("=========================")

    output = "\n".join(bill)
    print(output)

    with open("bill.txt", "w") as file:
        file.write(output)

    print("Bill saved to bill.txt")


while True:
    add_item()
    choice = input("Add another item? (yes/no): ").strip().lower()

    if choice != "yes":
        break

generate_bill()