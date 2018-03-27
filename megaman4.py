# MEGA MAN 4 - Mini Game by @acideater - March 2018
robotMasters = ["Bright Man", "Dive Man", "Drill Man", "Dust Man", "Pharaoh Man", "Ring Man", "Skull Man", "Toad Man" ]

print("#########################################")
print("Let's play MEGA MAN 4 mini game! \nENJOY!")
print("##########################################\n\n")

def start():
	input("Press Enter to start...\n\n")
	print("AD 200X \nDr Cossack, a mysterious scientist, \nhas invented eight powerful robots \nand sent then after Mega Man.")
	print("Mega Man starts for the battle again, \nthis time equipped with the powerful \nnew Mega Buster!\n\n")
	input("Press Enter to see the instructions...\n\n")
	print("##################")
	print("Instructions: \n  You have a weapon. Choose which Robot \n  Master you can most effectively kill \n  with that weapon.")
	print("##################\n\n")
	startGame = input("Do you want to start? Yes or No?\n")

	if startGame == "Yes":
		goFirstStage()
		
def goFirstStage():
	print("\n##################FIRST STAGE####################### \n8 of 8 robot masters left - weapon: *MEGA BUSTER*\n")
	print(robotMasters)
	firstBoss = input("Choose a Robot Master to fight against:\n")
	if firstBoss == "Toad Man":
		goSecondStage()
	else:
		print("\nMEGA BUSTER is not effective against " + firstBoss + "\nYou lost! \n#######Game over#######")

def goSecondStage():
	print("You use MEGA BUSTER. You beat Toad Man! \nYou got ****RAIN FLUSH****! \n")
	input("Press Enter to continue...\n")
	print("##################SECOND STAGE####################### \n7 of 8 robot masters left - weapon: *RAIN FLUSH*\n")
	print(robotMasters[0 : 7])
	secondBoss = input("Choose a Robot Master to fight against:\n")
	if secondBoss == "Bright Man":
		goThirdStage()
	else:
		print("\nRAIN FLUSH is not effective against " + secondBoss + "\nYou lost! \n#######Game over#######")           

def goThirdStage():
	print("You use RAIN FLUSH. You beat Bright Man! \nYou got ****FLASH STOPPER****! \n")
	input("Press Enter to continue...\n")
	print("##################THIRD STAGE####################### \n6 of 8 robot masters left - weapon: *FLASH STOPPER*\n")
	print(robotMasters[1 : 7])
	thirdBoss = input("Choose a Robot Master to fight against:\n")
	if thirdBoss == "Pharaoh Man":
		goFourthStage()
	else:
		print("\nFLASH STOPPER is not effective against " + thirdBoss + "\nYou lost! \n#######Game over#######")  
		
def goFourthStage():
	print("You use FLASH STOPPER. You beat Pharaoh Man! \nYou got ****PHARAOH SHOT****! \n")
	input("Press Enter to continue...\n")
	print("##################FOURTH STAGE####################### \n5 of 8 robot masters left - weapon: *PHARAOH SHOT*\n")
	robotMasters4 = ["Dive Man", "Drill Man", "Dust Man", "Ring Man", "Skull Man"]
	print(robotMasters4)
	fourthBoss = input("Choose a Robot Master to fight against:\n")
	if fourthBoss == "Ring Man":
		goFifthStage()
	else:
		print("\nPHARAOH SHOT is not effective against " + fourthBoss + "\nYou lost! \n#######Game over#######")  		
		
def goFifthStage():
	print("You use PHARAOH SHOT. You beat Ring Man! \nYou got ****RING BOOMERANG****! \n")
	input("Press Enter to continue...\n")
	print("##################FIFTH STAGE####################### \n4 of 8 robot masters left - weapon: *RING BOOMERANG*\n")
	robotMasters5 = ["Dive Man", "Drill Man", "Dust Man", "Skull Man"]
	print(robotMasters5)
	fifthBoss = input("Choose a Robot Master to fight against:\n")
	if fifthBoss == "Dust Man":
		goSixthStage()
	else:
		print("\nRING BOOMERANG is not effective against " + fifthBoss + "\nYou lost! \n#######Game over#######")  	
		
def goSixthStage():
	print("You use RING BOOMERANG. You beat Dust Man! \nYou got ****DUST CRUSHER****! \n")
	input("Press Enter to continue...\n")
	print("##################SIXTH STAGE####################### \n3 of 8 robot masters left - weapon: *DUST CRUSHER*\n")
	robotMasters6 = ["Dive Man", "Drill Man", "Skull Man"]
	print(robotMasters6)
	sixthBoss = input("Choose a Robot Master to fight against:\n")
	if sixthBoss == "Skull Man":
		goSeventhStage()
	else:
		print("\nDUST CRUSHER is not effective against " + sixthBoss + "\nYou lost! \n#######Game over#######")  	

def goSeventhStage():
	print("You use DUST CRUSHER. You beat Skull Man! \nYou got ****SKULL BARRIER****! \n")
	input("Press Enter to continue...\n")
	print("##################SEVENTH STAGE####################### \n2 of 8 robot masters left - weapon: *SKULL BARRIER*\n")
	print(robotMasters[1 : 3])
	seventhBoss = input("Choose a Robot Master to fight against:\n")
	if seventhBoss == "Dive Man":
		goEighthStage()
	else:
		print("\nSKULL BARRIER is not effective against " + seventhBoss + "\nYou lost! \n#######Game over#######")  			

def goEighthStage():
	print("You use SKULL BARRIER. You beat Dive Man! \nYou got ****DIVE MISSILE****! \n")
	input("Press Enter to continue...\n")
	print("##################EIGHT STAGE####################### \n1 of 8 robot masters left - weapon: *DIVE MISSILE*\n")
	print(robotMasters[2])
	eighthBoss = input("Use DIVE MISSILE to beat Drill Man? Yes or No?\n")
	if eighthBoss == "Yes":
		goFinalStage()
	else:
		print("\nYou lost! \n#######Game over#######")  	
		
def goFinalStage():
	print("\n\nCongratulations! \nYou beat the game!\n")

	print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
	print("░░░░░░░░░░░░░░░▄▄▄▄░░░░░░░░░░░░░░░")
	print("░░░░░░░░░░░░▄███░░███▄░░░░░░░░░░░░")
	print("░░░░░░░░░░▄█████▄▄█████▄░░░░░░░░░░")
	print("░░░░░░░░░░██████░░██████░░░░░░░░░░")
	print("░░░░░░░░░█░█▀░░▀██▀░░▀█░█░░░░░░░░░")
	print("░░░░░░░░░█░█░░██░░██░░█░█░░░░░░░░░")
	print("░░░░░░░░░░▀█░░▄▄▄▄▄▄░░█▀░░░░░░░░░░")
	print("░░░░░░░░░░░░▀▄▄▀▀▀▀▄▄▀░░░░░░░░░░░░")
	print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
	print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
	print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
	print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
	print(".▀█▀.█▄█.█▀█.█▄.█.█▄▀　█▄█.█▀█.█─█")
	print("─.█.─█▀█.█▀█.█.▀█.█▀▄　─█.─█▄█.█▄█")
	
start()
