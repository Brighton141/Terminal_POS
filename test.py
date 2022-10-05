from cashier.cashier_screen import cashier_screen


def welcome_scrn():
    print("\n\n*****WELCOME*****\n")

    print("1.Cashier", "\n2.Customer", "\n3.Management", "\n4.Procurement", "\n5.Exit")

    c = int(input("Choose:\n"))

    if c == 1:
        print("*****Redirecting to Cashier Screen !!!*****")
        cashier_screen()

    elif c == 2:
        print("*****Screen is under management!!!*****")
        quit()

    elif c == 3:
        print("*****Screen is under management!!!*****")
        quit()

    elif c == 4:
        print("*****Screen is under management!!!*****")
        quit()

    elif c == 5:
        print("*****Thank You Come Again!!!*****")
        quit()

    else:
        print("Invalid option")


welcome_scrn()
