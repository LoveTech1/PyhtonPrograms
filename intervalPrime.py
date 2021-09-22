# python program to print the numbers in an interval

low = 200
high = 400
num = int(input("Enter the number: "))

for num in range(low,high):
    if num > 1:
        for i in range(2,num):
            if(num % i == 0):
                break
        else:
            print(num)

            

