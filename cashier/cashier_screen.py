def cashier_screen(receive=0, r=0, change=0):
    r = r
    receive = receive
    change = change

    print("\n\n*****CASHIER*****\n")

    print("*****PRODUCTS*****")

    print("1.Minute Maid- 400ml---->80", "\n2.Afia- 400ml---->75", "\n3.Predator- 400ml-->50",
          "\n4.Del Monte---->400", "\n5.Cash Out", "\n6.Exit")
    cart = int(input("Choose:\n"))

    if cart == 1:

        d = int(input("Enter the quantity:\n"))
        r = r + 80 * d

    elif cart == 2:
        d = int(input("Enter the quantity:\n"))
        r = r + 75 * d

    elif cart == 3:
        d = int(input("Enter the quantity:\n"))
        r = r + 50 * d

    elif cart == 4:
        d = int(input("Enter the quantity:\n"))
        r = r + 400 * d

    elif cart == 5:
        print("total:", r)
        if r > 0:
            recieve = int(input("Input money received:\n"))
            print("Change:", recieve - r)
            print("*****Thank You Come Again!!!*****")

    elif cart == 6:
        quit()
    else:
        print("Invalid option")

    print("total:", r)
    if r > 0:
        recieve = int(input("Input money received:\n"))
        print("Change:", recieve - r)
        print("*****Thank You Come Again!!!*****")


