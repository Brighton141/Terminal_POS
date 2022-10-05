def add_name():
    outfile = open("customer_names.txt", "w")
    customer_name = input("Please enter customer name: ")
    outfile.write(customer_name)
    outfile.close()
