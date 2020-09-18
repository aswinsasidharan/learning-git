def sqfunc():
	while True:
		try:
			num = int(input("Enter an integer :"))
		except TypeError:
			print("Error!! Please enter a number")
			continue
		else:
			sqrd = num**2
			print(f"The square of {num} is {sqrd}")
			break	