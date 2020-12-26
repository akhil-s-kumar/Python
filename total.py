total = 0
for i in range(5):
    a = int(input("Enter number: "))
    yorn = input("Do you want to include that number (y/n): ")
    if yorn == 'y' or yorn == 'Y':
        total+=a
    else:
        continue
print(total)
