import time
while True:
	x=int(input("                                   enter your pin - "))
	if x == 75977:
		print("Press 1 - For Mini-Statement ")
		print("press 2 - For Money Withdrawal")
		print("Press 3 - For Balance Enquiry")
		print("press 4 - For Pin Change")
		print("press 5 - For Generating Pin")
		print("press 6 - To Get Out Of The Menu")

		y=int(input("                                  Plz enter your choice - "))
		if y== 1:
			print("Plz wait,the system is in under process")
			time.sleep(2)
			print("PLZ collect your mini-statement")
			break
		elif y==2:
			a=int(input("                                  Enter the amount - "))
			print("Plz wait while the system is processing")
			time.sleep(5)
			print("Plz collect your money ")
			time.sleep(3)
			print("                                  Do you want to know whats your remaining balance?")
			print("                                  Press 1 -for Yes")
			print("                                  Press 2 -for No ")
			q=int(input("Enter your choice"))
			if q==1:
				print("                                  Your remaining balance is - ",72000-a)
			else:
				print("                                  Have A Nice Day Sir/Mam ")
			break
		elif y==3:
			print("                                  Your balance is - 72,000")
			break
		elif y==4:
			print("                                  Sending an OTP to your RMN")
			z=int(input("                                           Enter the OTP - "))
			if z== 123:
				print("PIN CHANGED SUCCESSFULLY")	
			else:
				print("You have enterd the wrong OTP")
			break
		elif y==5:
			print("NEW PIN has been sent to your RMN")
			break
		elif y==6:
			break
		else:
			print("You've entered a wrong choice.")
			break
	else:
		print("                                   You have entered the wrong pin")