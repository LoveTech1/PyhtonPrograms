# Python Program to Find Numbers Divisible by Another Number

# making a list of numbers to check whether they are divisible by certain number

num = [234,56,90,77,33]

result = list(filter(lambda x: (x % 2 == 0),num))

print(f"The number divisible by 2 are {result}")
