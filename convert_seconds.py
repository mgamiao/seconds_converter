def start():
	global input1
	global seconds
	global mins
	global hours
	input1 = int(input("Enter number of seconds: "))
	seconds = 0
	mins = 0
	hours = 0

	seconds = input1 % 60
	mins = int(input1 / 60)
	hours1()
	end()
def hours1():
	global input1
	global seconds
	global mins
	global hours
	if mins >= 60:
		hours = hours + 1
		mins = mins - 60
		hours1()

def end():
	global input1
	global seconds
	global mins
	global hours
	print(str(hours) + "hour(s)")
	print(str(mins) + "minute(s)")
	print(str(seconds) + "second(s)")

start()