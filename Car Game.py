from random import randint
import os

# Misc.
screen = [["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		  ]

end = False
end2 = False
minimum = 0
difficulty = input("<Car Game>\n\nSelect a mode:\n1: Easy - Only the very front breaks the car.\n2: Hard - The front and the front wheels break the car if contact.\n>")
mode = input("Do you want constant obstacles, or random obstacles? (C/R)\n>")

if difficulty != "1" and difficulty != "2":
	end = True
	
if mode == "c":
	minimum = 10
elif mode == "r":
	minimum = 1
else:
	end2 = True

def pixel1(y,x):
	screen[y][x] = "■"
	
def pixel0(y,x):
	screen[y][x] = "□"

barrier = 0
px = 8
py = 9
ox = 0
oy = -1
on_screen = False
use = False

decor = 1
num = 0
if num < 10:
	str_num = [str(num)[-1],"0"]
else:
	str_num = [str(num)[-1],str(num)[-2]]
	
# From lines 56-238 is all functions
def digit1():
	if str_num[0] == "0":
		pixel1(10,18)
		pixel1(9,19)
		pixel1(7,19)
		pixel1(6,18)
		pixel1(7,17)
		pixel1(9,17)
	elif str_num[0] == "1":
		pixel1(7,19)
		pixel1(9,19)
	elif str_num[0] == "2":
		pixel1(10,18)
		pixel1(9,17)
		pixel1(8,18)
		pixel1(7,19)
		pixel1(6,18)
	elif str_num[0] == "3":
		pixel1(10,18)
		pixel1(9,19)
		pixel1(7,19)
		pixel1(6,18)
		pixel1(8,18)
	elif str_num[0] == "4":
		pixel1(9,19)
		pixel1(7,19)
		pixel1(7,17)
		pixel1(8,18)
	elif str_num[0] == "5":
		pixel1(10,18)
		pixel1(9,19)
		pixel1(6,18)
		pixel1(7,17)
		pixel1(8,18)
	elif str_num[0] == "6":
		pixel1(10,18)
		pixel1(9,19)
		pixel1(6,18)
		pixel1(7,17)
		pixel1(9,17)
		pixel1(8,18)
	elif str_num[0] == "7":
		pixel1(9,19)
		pixel1(7,19)
		pixel1(6,18)
	elif str_num[0] == "8":
		pixel1(10,18)
		pixel1(9,19)
		pixel1(7,19)
		pixel1(6,18)
		pixel1(7,17)
		pixel1(9,17)
		pixel1(8,18)
	elif str_num[0] == "9":
		pixel1(10,18)
		pixel1(9,19)
		pixel1(7,19)
		pixel1(6,18)
		pixel1(7,17)
		pixel1(8,18)
		
def digit2():
	if str_num[1] == "0":
		pixel1(4,18)
		pixel1(3,19)
		pixel1(1,19)
		pixel1(0,18)
		pixel1(1,17)
		pixel1(3,17)
	elif str_num[1] == "1":
		pixel1(3,19)
		pixel1(1,19)
	elif str_num[1] == "2":
		pixel1(4,18)
		pixel1(3,17)
		pixel1(2,18)
		pixel1(1,19)
		pixel1(0,18)
	elif str_num[1] == "3":
		pixel1(4,18)
		pixel1(3,19)
		pixel1(1,19)
		pixel1(0,18)
		pixel1(2,18)
	elif str_num[1] == "4":
		pixel1(3,19)
		pixel1(1,19)
		pixel1(1,17)
		pixel1(2,18)
	elif str_num[1] == "5":
		pixel1(4,18)
		pixel1(3,19)
		pixel1(0,18)
		pixel1(1,17)
		pixel1(2,18)
	elif str_num[1] == "6":
		pixel1(4,18)
		pixel1(3,19)
		pixel1(0,18)
		pixel1(1,17)
		pixel1(3,17)
		pixel1(2,18)
	elif str_num[1] == "7":
		pixel1(3,19)
		pixel1(1,19)
		pixel1(0,18)
	elif str_num[1] == "8":
		pixel1(4,18)
		pixel1(3,19)
		pixel1(1,19)
		pixel1(0,18)
		pixel1(1,17)
		pixel1(3,17)
		pixel1(2,18)
	elif str_num[1] == "9":
		pixel1(4,18)
		pixel1(3,19)
		pixel1(1,19)
		pixel1(0,18)
		pixel1(1,17)
		pixel1(2,18)
		
def player(y,x):
	pixel1(y,x)
	pixel1(y-1,x-1)
	pixel1(y,x-2)
	pixel1(y-2,x-1)
	pixel1(y-2,x)
	pixel1(y-2,x-2)
	pixel1(y-3,x-1)
	
def player_off(y,x):
	pixel0(y,x)
	pixel0(y-1,x-1)
	pixel0(y,x-2)
	pixel0(y-2,x-1)
	pixel0(y-2,x)
	pixel0(y-2,x-2)
	pixel0(y-3,x-1)

def road():
	if decor == 0:
		pixel1(0,0)
		pixel1(2,0)
		pixel1(4,0)
		pixel1(6,0)
		pixel1(8,0)
		pixel1(10,0)
		pixel1(0,14)
		pixel1(2,14)
		pixel1(4,14)
		pixel1(6,14)
		pixel1(8,14)
		pixel1(10,14)
	elif decor == 1:
		pixel1(1,0)
		pixel1(3,0)
		pixel1(5,0)
		pixel1(7,0)
		pixel1(9,0)
		pixel1(1,14)
		pixel1(3,14)
		pixel1(5,14)
		pixel1(7,14)
		pixel1(9,14)
		
def line(y,x):
	pixel1(y,x)
	pixel1(y,x-1)
	pixel1(y,x-2)
	pixel1(y,x-3)
	pixel1(y,x-4)
	
def line_off(y,x):
	pixel0(y,x)
	pixel0(y,x-1)
	pixel0(y,x-2)
	pixel0(y,x-3)
	pixel0(y,x-4)
	
def capital(str):
	temp = str.upper()
	return temp

# If any of the inputs at the start are invalid
if end == False and end2 == False:
	use = True
	os.system("cls" if os.name == "nt" else "clear")

# Main
while use:
	# Score, player, road decoration is set to 'screen'
	digit1()
	digit2()
	player(py,px)
	road()
	
	# Obstacles
	if on_screen == False:
		barrier = randint(minimum,10)
		
		if barrier == 10:
			ox = randint(6,12)
			line(oy,ox)
			on_screen = True
	
	if on_screen == True:
		if oy < 10:
			line_off(oy,ox)
			oy += 1
			line(oy,ox)
			
			if oy == 9:
				num += 1
		else:
			line_off(oy,ox)
			oy = -1
			on_screen = False
			
	# Difficulty lose screens
	if difficulty == "1":
		if screen[py-3][px-1] == "□":
			print("#    ###  ###  ###")
			print("#    # #  #    #  ")
			print("#    # #  ###  ###")
			print("#    # #    #  #  ")
			print(f"###  ###  ###  ###  {num}/100")
			break	
		
	elif difficulty == "2":
		if screen[py-3][px-1] == "□" or screen[py-2][px-2] == "□" or screen[py-2][px] == "□":
			print("#    ###  ###  ###")
			print("#    # #  #    #  ")
			print("#    # #  ###  ###")
			print("#    # #    #  #  ")
			print(f"###  ###  ###  ###  {num}/100")
			break
	
	# Prints the screen, then clears to avoid visual bugs
	for i in screen:
		print("".join(i))
	
	screen = [["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		  	["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		 	 ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		 	 ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
			  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		 	 ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		 	 ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		 	 ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		 	 ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
			  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
			  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		 	 ]
	
	print(f"Car Game | (C)2022 | Difficulty: {difficulty} | Mode: {capital(mode)}")		 	 
	move = input("A or D\n>")
	
	# Movement
	if move == "a":
		if px > 4:
			px -= 1
	elif move == "d":
		if px < 12:
			px += 1
			
	# Road decoration
	if decor == 0:
		decor = 1
	elif decor == 1:
		decor = 0
	
	# Screen clear
	os.system("cls" if os.name == "nt" else "clear")
	
	# Scoreboard
	if num < 10:
		str_num = [str(num)[-1],"0"]
	else:
		str_num = [str(num)[-1],str(num)[-2]]
	
	# Win screen
	if num == 100:
		print("# # #  ###  #   #")
		print("# # #   #   ##  #")
		print("# # #   #   # # #")
		print("# # #   #   #  ##")
		print("#####  ###  #   #")
		break
		
# Error messages
if end == True:
	print(f"Invalid difficulty of '{difficulty}'")
elif end2 == True:
	print(f"Invalid mode of '{mode}'")