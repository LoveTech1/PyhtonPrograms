# to check whether the number is prime or not

num = int(input("Enter the number to check prime: "))

value = False

if num > 1:
    for i in range(2,num):
        if (num % i == 0):
            value = True
            break

if value:
    print(f"{num} is not prime Number.")
else:
    print(f"{num} is prime number.")