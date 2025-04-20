import Classes as cl
from Classes import Checkout


def menu():
    while True:
        print("Which Item do you want to purchase")
        print("""
        1. Candy
        2. Cookie
        3. Ice Creame
        4. Sundae
        5. Add Items in cash Register
        6. get number of Items in cash register
        7. Display Items in cash register
        8. get total cost of Items
        9. clear cash Register
        0. Exit """)
        choice = int(input("Enter your choice : "))


        if choice == 1:
            name = input("Enter Name of Candy : ")
            weight = int(input("Enter Weight of Candy : "))
            candy = cl.Candy(name, weight)
            candy.display_name()

        elif choice == 2:
            name = input("Enter Name of Cookie : ")
            units = int(input("Enter units of Cookie : "))
            cookie = cl.Cookie(name, units)
            print(cookie.display_name())
            print(cookie.cost_of_item())

        elif choice == 3:
            name = input("Enter Name of Ice Creame : ")
            ice = cl.Icecreame(name)

        elif choice == 4:
            name = input("Enter Name of Sundae : ")
            sundae = cl.Sundae(name)

        elif choice == 5 :          # Add Items in cash Register
            check = Checkout(cookie, ice, sundae)

        elif choice == 6 :
            break

        elif choice == 7 :
            break

        elif choice == 8 :
            break

        elif choice == 9 :
            break

        elif choice == 0 :
            break
