# Dwayne Winn CIS261 Country

def main():
#set initinal data
    countries = {"AF": "Afganistan", "DE": "Germany", "US": "United States"}
    
    while True:
        #check input from user
        print()
        d_menu()
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
            print("Not a valid command. Pleasy try again.")
   
 #display menu
def d_menu():
       print("COMMAND MENU")
       print("view - View country name")
       print("add - Add a country")
       print("del - Delete a country")
       print("exit - Exit program")
       
def d_codes(countries):
    codes = list(countries.keys())
    codes.sort()
    c_line = "Country codes: "
    for code in codes:
       c_line += code + " "
    print(c_line)

# show the countries
def view(countries):
    d_codes(countries)
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print("Country name: ",name)
    else:
        print("There is no country with that code.\n")
        
#add country function
def add(countries):
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(name,"is already using this code.")
    else:
        name = input("Enter country name: ")
        name = name.title()
        countries[code] = name
        print(name," was added")
        print()
  #delete funtions  
def delete(countries):
    d_codes(countries)
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
       name = countries.pop(code)
       print(name," was deleted")
       print()
    else:
       print("There is no country with that code.")

if __name__ == "__main__":
    main()

       
