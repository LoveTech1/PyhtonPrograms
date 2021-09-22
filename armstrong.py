# python program to find the armstrong number 

num = int(input("Enter the number: "))

sum  = 0    # initialize the sum variable to 0

temp = num # assigning the num value user entere to temporary variable

while temp > 0:             # if entered value is more than 0
    digit = temp % 10       # takes out each digit in each loop
    sum += digit ** 3       # finds cube of each digit taken out
    temp //= 10             # condition to end the loop

if sum == num:      
    print("It is armstrong")
else:
    print("It is not armstrong")


