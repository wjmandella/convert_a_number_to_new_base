#Convert any decimal number to a number in a different base (up to and including BASE 36).

active = True
active_2 = True

while active == True:
	base_system = int(input("Enter the base of the number system (2 - 36) you would like to use for the conversion: "))
	bs = base_system
	remainder_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J','K','L','M','N','O','P','Q','R', 'S','T','U','V','W','X','Y','Z']

	while not(2 <= bs <= 36):
		bs = int(input("Invalid response.\nPlease enter a number from 2 to 36 (inclusive): "))
	
	bs_digits = []
	for i in range(0, bs):
		bs_digits.append(remainder_list[i])
	bs_digits = ', '.join(bs_digits)
	print("NOTE: The digits in BASE " + str(bs) + " are: " + bs_digits)
	
	deci_number = int(input("\nEnter a decimal number to be converted to the new base system number (BASE " + str(bs) + "): " ))

	while active_2 == True:
		deci_number_original = deci_number
		i = 0


		if (deci_number/bs) < 1:
			base_number = remainder_list[deci_number%bs]
			#print(base_number)
			print("The decimal number " + str(deci_number_original) + " is represented in BASE " + str(bs) + " by the number " + str(base_number)+ ".")			
			
			answer = input("\n\nWould you like to try another number in BASE " + str(bs) +"? (y/n): ").lower()
			while not(answer == 'y' or answer == 'n' or answer == 'yes' or answer == 'no'):
				answer = input("Invalid response.\nWould you like to try another number in BASE " + str(bs) + "? (y/n): ").lower()
			if (answer == 'y' or answer == 'yes'):
				deci_number = int(input("Enter the decimal number to be converted to BASE " + str(bs) + ": "))
					
			elif (answer == 'n' or answer == 'no'):
				answer = input("\nWould you like to try a number in a different base? (y/n): ").lower()

				while not(answer == 'y' or answer == 'n' or answer == 'yes' or answer == 'no'):
					answer = input("Invalid response.\nWould you like to try another number and/or base? (y/n): ").lower()
				if answer == (answer == 'y' or answer == 'yes'):
					break
					active == True
				elif (answer == 'n' or answer == 'no'):
					print("\nOkay. Goodbye for now.")
					active_2 = False
					active = False			
		else:
			quotient = 1.1
			while quotient > 1:
				quotient = deci_number/((bs)**i)
				i +=1
			#print(i)
			base_digit_list = [] 
			if deci_number%(bs) == 0:
				for	n in range((i-1), -1, -1):
			#	for	n in range((i-2), -1, -1):
					digit = deci_number//(bs**n)
					digit = remainder_list[digit]
					base_digit_list.append(str(digit))
					deci_number = deci_number%(bs**n)
				if base_digit_list[0] == '0':
					del base_digit_list[0]
				base_number = ''.join(base_digit_list)
				print("The decimal number " + str(deci_number_original) + " is represented in BASE " + str(bs) + " by the number " + str(base_number)+ ".")	
			else:
				for	n in range((i-2), -1, -1):
					digit = deci_number//(bs**n)
					digit = remainder_list[digit]
					base_digit_list.append(str(digit))
					deci_number = deci_number%(bs**n)
				base_number = ''.join(base_digit_list)	
				#print(base_number)
				print("The decimal number " + str(deci_number_original) + " is represented in BASE " + str(bs) + " by the number " + str(base_number)+ ".")	
			
			answer = input("\nWould you like to try another number in this base? (y/n): ").lower()

			while not(answer == 'y' or answer == 'n' or answer == 'yes' or answer == 'no'):
				answer = input("Invalid response.\nWould you like to try another number in BASE " + str(bs) +"? (y/n): ").lower()
			if (answer == 'y' or answer == 'yes'):
				deci_number = int(input("Enter the decimal number to be converted to BASE " + str(bs) + ": "))
			elif (answer == 'n' or answer == 'no'):
				answer = input("Would you like to try a number in a different base? (y/n): ").lower()
				while not(answer == 'y' or answer == 'n' or answer == 'yes' or answer == 'no'):
					answer = input("Invalid response.\nWould you like to try another number and/or base? (y/n): ").lower()
				if (answer == 'y' or answer == 'yes') :
					print()
					break
					active == True
				elif (answer == 'n' or answer == 'no'):
					print("\nOkay. Goodbye for now.")
					active_2 = False
					active = False
				
				
				


			
