# Python Program to Convert Decimal to Binary, Octal and Hexadecimal
age = 18

while True:
    try: 
        age = int(input("Enter the age: "))
        if age < 20:
            print("Y0u are less than 20 years old")
            break
        elif age == 20:
            print("YOu are 20 years old")
            break
        else:
            print("The age is incorrect")

    except ValueError:
        print("Invalid input")
        continue


    