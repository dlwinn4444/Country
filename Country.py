# Dwayne Winn CIS261 Country

def main():
    countries = {"AF": "Afganistan", "DE": "Germany", "US": "United States"}
    c_menu()
    while True
        c_choice = input("Command: ")
        if c_choice == "view":
            view(countries)
        elif c_choice == "add":
            add(countries)
        elif c_choice == "del":
            delete(countries)
        elif c_choice == "exit":
            break
        else:
            print("Not a valid command. Pleasy try again.)"
                  
def display_menu():
       print("COMMAND MENU")
       print("view - View country name")
       print("add - Add a country")
       print("del - Delete a country")
       print("exit - Exit program")
       print()