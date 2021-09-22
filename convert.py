# convert the decimal num to binary , hex and octal 

while True:
    try:
        ans = input("Do you want to find binary: 'yes' or 'no': ")
        if ans == "yes":
            dec = int(input("enter the number in decimal: "))
            convert = bin(dec)
            print(f"The decimal {dec} value in binary is {convert}")
        else:
            print("Invalid input")
            break
    except ValueError:
        print("Exiting...")
        continue
    


