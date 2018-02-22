print("What is the First Number " )
num1 = input()
print("what is the Second Number " )
num2 = input()

print("1.Addition(+)")
print("2.Subtraction(-)")
print("3.Multiplication(*)")
print("4.Division(/)")

opperation = input("")

if opperation is "+":
	Addition = (int(num1) + int(num2))
	print("The Answer is " + str(Addition))
elif opperation is "-":
	Subaction = (int(num1) - int(num2))
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