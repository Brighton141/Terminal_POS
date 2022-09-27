class terminal_pos:

    def __init__(self, a=0, r=0, receive= 0, change=0, temp=0):

        print("\n\n*****WELCOME*****\n")

        self.a = a
        self.r = r
        self.receive = receive
        self.change = change
        self.temp = temp

    def welcome_screen(self):

        print("1.Cashier", "\n2.Customer", "\n3.Management", "\n4.Procurement", "\n5.Exit")

        while 1:

            c = int(input("Choose:\n"))

            if c == 1:
                print("*****Redirecting to Cashier Screen !!!*****")
                self.cashier_screen()

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

    def cashier_screen(self):
        print("\n\n*****CASHIER*****\n")

        print("*****PRODUCTS*****")

        print("1.Minute Maid- 400ml---->80", "\n2.Afia- 400ml---->75", "\n3.Predator- 400ml-->50",
              "\n4.Del Monte---->400", "\n5.Cash Out", "\n6.Exit")
        cart = int(input("Choose:\n"))

        if cart == 1:

            d = int(input("Enter the quantity:\n"))
            self.r = self.r + 80 * d

        elif cart == 2:
            d = int(input("Enter the quantity:\n"))
            self.r = self.r + 75 * d

        elif cart == 3:
            d = int(input("Enter the quantity:\n"))
            self.r = self.r + 50 * d

        elif cart == 4:
            d = int(input("Enter the quantity:\n"))
            self.r = self.r + 400 * d

        elif cart == 5:
            print("total:", self.r)
            if self.r > 0:
                recieve = int(input("Input money received:\n"))
                print("Change:", recieve - self.r)
                print("*****Thank You Come Again!!!*****")
                quit()
        elif cart == 6:
            quit()
        else:
            print("Invalid option")


def main():
    a = terminal_pos()

    while 1:
        a.welcome_screen()


main()
