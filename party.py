count = 0
cont = 'y' or 'Y'
while cont.lower() == 'y' or cont.upper() == 'Y':
    name = input("Enter Name: ")
    print(name, "has now been invited!")
    count+=1
    cont = input("Do you want to invite anyone else? (y/n)")
    if cont == "n":
        break
print(count, "people are coming for the party.")
