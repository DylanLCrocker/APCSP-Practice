def drink_price(size, extra) :
    price = 0
    if (size == "S") :
        price += 3
    elif (size == "M") :
        price += 4
    else :
        price += 5

    if (extra == "Y") :
        price += 1
    return price

def serve_customer(customer_number, drink_count) :
    bill = 0
    for i in range(0, drink_count, 1) :
        size = input("Size: ")
        extra = input("Extra: ")
        bill += drink_price(size, extra)
    print("Customer " + str(customer_number) + ": $" +str(bill))
    return bill

def main() :
    total_sales = 0
    total_customers = int(input("Total Customers: "))
    for i in range(1, total_customers + 1, 1) :
        drink_count = int(input( "Customer " + str(i) + " Drink Count: "))
        total_sales += serve_customer(i, drink_count)
    print("Total Sales: $" + str(total_sales))

main()