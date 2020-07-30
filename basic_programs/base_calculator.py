from functools import reduce

user_digi_no = input("How many numbers you want to calculate?\n")

if user_digi_no.isnumeric() == True:
	user_input = []
	for i in range(int(user_digi_no)):
		user_input.append(int(input(f"Enter {i+1} number\n")))
	print(f"List of Number is:{user_input}\n")
	user_operation = input("Which operation you want to do?\n")
	if user_operation == 'add' or user_operation =='+':
		result = reduce(lambda x,y: x+y , user_input)
	elif user_operation == 'minus' or user_operation =='-':
		result = reduce(lambda x,y: x-y , user_input)
	elif user_operation == 'multiply' or user_operation =='*':
		result = reduce(lambda x,y: x*y , user_input)
	elif user_operation == 'divide' or user_operation =='/':
		result = reduce(lambda x,y: x/y , user_input)
	if 'result' in locals() or 'result' in globals():
		print(f"Result of {user_operation} operation is {result}")
	else:
		print("Kindly perform correct operations.")
else:
	print("Invalid digit number.")
