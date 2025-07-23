welcome_page = print("""

	Your 
		NOKIA
			menu map



LIST OF MENU FUNCTIONS

	1 -> Phone book
	2 -> Messages
	3 -> Chat
	4 -> Call register
	5 -> Tones
	6 -> Settings
	7 -> Call divert
	8 -> Game
	9 -> Calculate
	10 -> Reminder
	11 -> Clock
	12 -> Profiles
	13 -> SIM services

""")
menu = int(input("Press any number for options   "))
match menu :
	case 1:
			print("""

			PHONE BOOK

		1 -> Search
		2 -> Service Nos
		3 -> Add name
		4 -> Erase
		5 -> Edit
		6 -> Assign tone
		7 -> Send b'card
		8 -> Options *
		9 -> Speed dials
		10 -> Voice tags
	""")

			search = int(input("Press keys for options   "))
			match search :
						case 1: 
							print("Search")
						case 2:
							print("Service Nos")
						case 3:
							print("Add name")
						case 4:
							print("Erase")
						case 5: 
							print("Edit")
						case 6:
							print("Assign tone")
						case 7:
							print("Send b'card")
						case 8:
							print("""

							    Options
							
							1 -> Type of view
							2 -> Memory status
					""")
							view = int(input("press any key for options   "))
							match view :
								case 1:
									print("Type of view")
								case 2:
									print("Memory status")
								case _:
									print("Invalid input bruh !!!")


						case 9:
							print("Speed dials")
						case 10:
							print("Voice tags")
						case _: 
							print("Invalid input bruh !!!")
		


	case 2:
			print("""

			MESSAGES
		
		1 -> Write messages
		2 -> Inbox
		3 -> Outbox
		4 -> Picture messages
		5 -> Templates
		6 -> Smileys
		7 -> Message settings *
		8 -> Info service
		9 -> Voice mailbox number
		10 -> Service command editor
	""")

			inbox = int(input("Press keys for options  "))
			match inbox :
						case 1:
							print("Write messages")
						case 2: 
							print("Inbox")
						case 2:
							print("Outbox")
						case 4:
							print("Picture message")
						case 5:
							print("Templates")
						case 6:
							print("Smiley")
						case 7:
							print("""

							    Message settings
							
							1 -> Set 1
							2 -> Common
					""")
							set = int(input("Press 1 or 2 for options   "))
							match set :
								case 1:
									print("""

										Set 1
								
									1 -> Message center number
									2 -> Message sent as
									3 -> Message validity
						""")
									center = int(input("Press any key for options   "))
									match center :
										case 1: 
											print("Message center number")
										case 2:
											print("Message sent as")
										case 3:
											print("Message validity")
										case _:
											print("Invalid input bruh !!!")
								case 2:
									print("""

									   Common
									
									1 -> Delivery reports
									2 -> Reply via same centre
									3 -> Character support
						""")
									character = int(input("Press any key for options   "))
									match character :
										case 1:
											print("Delivery reports")
										case 2:
											print("Reply via same centre")
										case 3:
											print("Character support")
										case _:
											print("Invalid input bruh !!!")
								case _:
									print("Invalid input bruh !!!")


						case 8:
							print("Info service")
						case 9:
							print("Voice mailbox number")
						case 10:
							print("Service command editor")
						case _:
							print("Invalid input bruh !!!")
						
	case 3:
			print("""
			
				CHAT

			0 -> Go back
	""")
			chatting = int(input("Press 0 to go back   "))
			match chatting :
						case 0: 
							print("in progress !")	
						case _:
							print("Invalid input bruh !!!")
	case 4:
			print("""

			CALL REGISTER

		1 -> Missed calls
		2 -> Received calls
		3 -> Dialled number
		4 -> Erase recent call lists
		5 -> Show call duration *
		6 -> Show call costs *
		7 -> Call cost settings *
		8 -> Prepaid credit
	""")
			missed = int(input("Press any key for options   "))
			match missed :
						case 1:
							print("Missed calls")
						case 2:
							print("Received calls")
						case 3:
							print("Dialled number")
						case 4:
							print("Erase recent call lists")
						case 5:
							print("""

							Show call duration

							1 -> Last call duration
							2 -> All call's duration
							3 -> Recieved call's duration
							4 -> Dialled call's duration
							5 -> Clear timers
					""")
							clear_timer = int(input("Press any key for options   "))
							match clear_timer :
								case 1:
									print("Last call duration")
								case 2:
									print("All call's duration")
								case 3:
									print("Recieved call's duration")
								case 4:
									print("Dialled call's duration")
								case 5:
									print("Clear timer")
								case _:
									print("Invalid input bruh !!!")


						case 6:
							print("""

							   Show call cost

							1 -> Last call cost
							2 -> All call's cost
							3 -> Clear counter
					""")
							clear_counter = int(input("Press any key for options   "))
							match clear_counter :
								case 1:
									print("Last call cost")
								case 2:
									print("All call's cost")
								case 3:
									print("Clear counter")
								case _:
									print("Invalid input bruh !!!")
						case 7:
							print("""

							Call cost settings

							1 -> Call cost limit
							2 -> Show costs in
					""")
							show_cost = int(input("Press 1 or 2 for options   "))
							match show_cost :
								case 1:
									print("Call cost limit")
								case 2:
									print("Show costs in")
								case _:
									print("Invalid input bruh !!!")
						case 8:
							print("Prepaid credit")
						case _:
							print("Invalid input bruh !!!")
	case 5:
			print("""

			TONES

		1 -> Ringing tone
		2 -> Ringing volume
		3 -> Incoming call alert
		4 -> Composer
		5 -> Message alert tone
		6 -> Keypad tones
		7 -> Warning and game tones
		8 -> Vibrating alert
		9 -> Screen saver
	""")
			composer = int(input("Press any key for options   "))
			match composer :
						case 1:
							print("Ringing tone")
						case 2:
							print("Ringing volume")
						case 3:
							print("Incoming call alert")
						case 4:
							print("Composer")
						case 5:
							print("Message alert tone")
						case 6:
							print("Keypad tones")
						case 7:
							print("Warning and game tone")
						case 8:
							print("Vibrating alert")
						case 9:
							print("Vibrating alert")
						case _:
							print("Invalid input bruh !!!")

	case 6:
			print("""

			SETTINGS

		1 -> Call settings
		2 -> Phone settings
		3 -> Security settings
		4 -> Restore factory settings
	""")
			restore = int(input("Press any keys for options   "))
			match restore :
						case 1:
							print("Call settings")
						case 2:
							print("Phone settings")
						case 3:
							print("Security settings")
						case 4:
							print("Restore factory settings")
						case _:
							print("Invalid input bruh !!!")
	case 7:
			print("""

			CALL DIVERT

		0 -> Go back		
	""")
			divert = int(input("press 0 to go back   "))
			match divert :
						case 0:
							print("In progress!")
						case _:
							print("Invalid input bruh !!!")
	case 8:
			print("""

			GAME

		0 -> Go back
	""")
			game = int(input("press 0 to go back   "))
			match game :
						case 0: 
							print("In progress!")
						case _:
							print("Invalid input bruh !!!")
	case 9:
			print("""

			CALCULATE
				
		0 -> Go back
	""")
			calculate = int(input("Press 0 to go back   "))
			match calculate :
						case 0:
							print("In progress!")
						case _:
							print("Invalid input bruh !!!")
	case 10:
			print("""

			REMINDER

		0 -> Go back
	""")
			reminder = int(input("Press 0 to go back   "))
			match reminder :
						case 0:
							print("In progress!")
						case _:
							print("Invalid input bruh !!!")
	case 11:
			print("""

			CLOCK

		1 -> Alarm clock
		2 -> Clock settings
		3 -> Date settings
		4 -> Stopwatch
		5 -> Countdown timer
		6 -> Auto update of date and time
	""")
			date = int(input("press any key for options   "))
			match date :
						case 1:
							print("Alarm clock")
						case 2:
							print("Clock settings")
						case 3:
							print("Date settings")
						case 4:
							print("Stopwatch")
						case 5:
							print("Countdowm timer")
						case 6:
							print("Auto update of date and time")
						case _:
							print("Invalid input bruh !!!")
	case 12:
			print("""

			PROFILES

		0 -> Go back
	""")
			profile = int(input("Press 0 to go back   "))
			match profile :
						case 0:
							print("In progress!")
						case _:
							print("Invalid input bruh !!!")
	case 13:
			print("""

			SIM SERCICES

		0 -> Go back
	""")
			sim_service = int(input("Press 0 to go back   "))
			match sim_service :
						case 0:
							print("In progress!")
						case _:
							print("invalid input bruh !!!")
	case _:
			print("Oga put better number joh")