num1 = input("What is the First Number " , end="" )
num2 = input("what is the Second Number ", end="")

print("1.Addition(+)")
print("2.Subtraction(-)")
print("3.Multiplication(*)")
print("4.Division(/)")

opperation = input("")

if opperation is "+":
	Addition = (int(num1) + int(num2))
	print("The Answer is " + str(Addition))
elif opperation is "-":
	Subtraction = (int(num1) - int(num2))
	print("The Answer is " + str(Subtraction))
elif opperation is "*":
	Multiplication = (int(num1) * int(num2))
	print("The Answer is " + str(Multiplication))
elif opperation is "/":
	Division = (int(num1) / int(num2))
	print("The Answer is " + str(Division))
else:
	print("Please provide a valid input")

print("Thank you")

