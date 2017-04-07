# import threading
import random

MAP_SIZE = 24

##################################################################
# MONSTER
monsters = []
level = [1]
def generate_monster():
	posr = random.randrange(23)
	posc = random.randrange(23)
	monsters.append({ 'position': [posr,posc],  
						'avatar': ' ƒ' ,
						'type':'Troll',
						'level': level[0],
						'health': 100 * level[0],
						'inventory':
						[{'type':'weapon','name':'Club','damage':7 + (4*level[0])},
						{'type':'shield','name':'Shield','damage':15}] })
	level[0] = level[0] + 1

generate_monster()

##################################################################

# WEAPON DICTIONARY
def new_weapon(lvl):
	return [
		{'type':'weapon','name':'Sword','damage':7 * lvl},
		{'type':'weapon','name':'Spear','damage':7 * lvl},
		{'type':'weapon','name':'Flail','damage':7 * lvl},
		{'type':'weapon','name':'Reaper','damage':7 * lvl}
	][lvl%4]

#  CREATE PLAYER
health = 100
gold = 5
inventory = [{'type':'weapon','name':'Axe','damage':10},
			{'type':'shield','name':'Shield','damage':15}]
player = {'name': 'ZORK', 'inventory':inventory, 'health': health, 'gold': gold}
# player['inventory'][0] = new_weapon(level[0])



message_key = ['', '', '']



					
def message(x, additional = ''):
	return {
	'cast': 'Magic spell cast, doing some damage.',
	'g5': 'Gained 5 Gold.',
	'g1': 'Gained 1 Gold.',
	'm1': 'Fight monster: {} with {} HP:{} '
		.format(monsters[0]['type'], monsters[0]['inventory'][0]['name'], monsters[0]['health']),
	'.':'Nothing to say.',
	'':'',
	'killedit':'You have slain the monster!',
	'looted':'You have looted the corpse',
	'dmg': '- DAMAGE = '
	}[x] + additional


# STATS
def hud():
	print("LEFT : {} {}  HEALTH: {}  {}".format(player['inventory'][0]['name'], player['inventory'][0]['damage'], player['health'], 
		message(message_key[2][:3], message_key[2][message_key[2].find(' '):] ) ) )
	print("RIGHT: {}   GOLD  : {} ".format(player['inventory'][1]['name'], player['gold'] ))
	# print(":POTION ^(f)                  (r)^ STAFF:")
	print( message(message_key[1]), message(message_key[0]))




# HELPER FUNCTION FOR mapit()
def get_index_from_bit(c):
	for i in range(MAP_SIZE):
		if c == 1 << i :
			return MAP_SIZE - i

########################################
# STRING TEMPLATES
avatar = " †"
trail  = "  "
map_row = " . . . . . . . . . . . . . . . . . . . . . . . ."
map_rows = []
for r in range(MAP_SIZE):
	map_rows.append(map_row)

head = [0]
# HEADER TEMPLATES
def header():
	if head[0] == 0:
		print("################################################## ")
		print("################ A D V E N T U R E ############### ")
		print("################################################## ")
	elif head[0] == 1:
		print("################################################## ")
		print("################# A SPELL IS CAST ################ ")
		print("################################################## ")
	elif head[0] == 2:
		print("################################################## ")
		print("################ MONSTER ATTACKED ################ ")
		print("################################################## ")
	elif head[0] == 3:
		print("################################################## ")
		print("################ !!!!YOU DIED!!!! ################ ")
		print("################################################## ")
	elif head[0] == 4:
		print("################################################## ")
		print("############### !!!! YOU WON !!!! ################ ")
		print("################################################## ")

# VARIABLE
current_position = [10,1024]


def monster_move():
	m = 0
	mon_row = monsters[m]['position'][0] 
	mon_col = monsters[m]['position'][1]
	mon_ind = MAP_SIZE - mon_row
	mon_colm = mon_col
	newrow  = map_rows[mon_row][ : (mon_colm-1)*2]
	newrow += ' ,'
	newrow += map_rows[mon_row][(mon_colm)*2 : ]
	map_rows[mon_row] = newrow
	if monsters[m]['position'][0] < 1 :
		monsters[m]['position'][0] = 1
	elif monsters[m]['position'][0] > 22:
		monsters[m]['position'][0] = 22
	else:
		monsters[m]['position'][0] += random.choice([-1,0,1])
	if  monsters[m]['position'][1] < 2:
		monsters[m]['position'][1] = 2
	elif monsters[m]['position'][1] > 22:
		monsters[m]['position'][1] = 22
	else:
		monsters[m]['position'][1] += random.choice([-1,0,1])

def check_proximity():
	# if ....
	if abs(monsters[0]['position'][0] - current_position[0]) < 2 and 2 > abs(monsters[0]['position'][1] - get_index_from_bit(current_position[1]) ) :
		return True
	return False
	# pass

def check_death(arg):
	if arg < 0:
		return True
	return False

def game_over(win):
	# print('GAME OVER')
	if win:
		head[0] = 4
		# header()
		m0 = monsters[0]['position'][0]
		m1 = monsters[0]['position'][1]
		new_row = map_rows[m0][:(m1-1)*2]
		new_row += ' x'
		new_row += map_rows[m0][m1*2:]
		message_key[1] = 'killedit'
		map_rows[m0] = new_row
		z = monsters.pop()
		generate_monster()
		# mapit()
	else:
		head[0] = 3
		header()
		quit()

def monster_attack():
	player['health'] = player['health'] - monsters[0]['inventory'][0]['damage']
	if check_death(player['health']):
		game_over(False)
	message_key[2] = 'dmg ' + str(monsters[0]['inventory'][0]['damage'])

################################################################################
def player_attack(arg):
	print(arg)
	if check_proximity():
		if arg == 'kill':
			monsters[0]['health'] = monsters[0]['health'] - (player['inventory'][0]['damage'] * 10)
			head[0] = 2
		else:
			monsters[0]['health'] = monsters[0]['health'] - int(player['inventory'][0]['damage'] * (player['gold'] * .01 ))
		if check_death(monsters[0]['health']):
			game_over(True)
	monster_go()
	mapit(current_position[0], current_position[1])
################################################################################

def cast_spell(spell = ''):
	if spell[:5] == 'black':
		player_attack('kill')
	elif spell[:5] == 'orang':
		pass
	elif spell == '':
		player_attack(spell)
	mapit()

# IF MODE == ROAM: MOVE
# IF MODE == FIGHT: ATTACK HERO
monster_modes = ['ROAM','FIGHT']
monster_mode = monster_modes[0]
def monster_go():
	proximity = check_proximity()
	if proximity:
		monster_mode = monster_modes[1]
	else:
		monster_mode = monster_modes[0]
	if monster_mode == 'ROAM':
		head[0] = 0
		monster_move()
		message_key[1] = ''
		message_key[2] = ''
	elif monster_mode == 'FIGHT':
		message_key[1] = 'm1'
		head[0] = 2
		monster_attack()

# GENERATE MAP
def mapit(row = current_position[0] , col = current_position[1]):

	header()

	ind = MAP_SIZE - row
	### MONSTER
	m = 0
	mon_row = monsters[m]['position'][0] 
	mon_col = monsters[m]['position'][1]
	mon_ind = MAP_SIZE - mon_row
	mon_colm = mon_col
	newrow  = map_rows[mon_row][ : (mon_colm-1)*2]
	newrow += monsters[m]['avatar']
	newrow += map_rows[mon_row][(mon_colm)*2 : ]
	map_rows[mon_row] = newrow
	for r in range(row):
		print(map_rows[r], r)
	colm = get_index_from_bit(col)
	newrow  = map_rows[row][ : (colm-1)*2]
	if map_rows[row][ (colm-1)*2:(colm)*2 ] == ' .':
		player['gold'] += 1
		message_key[0] = 'g1'
	elif map_rows[row][ (colm-1)*2:(colm)*2 ] == ' ,':
		player['gold'] += 5
		message_key[0] = 'g5'
	elif map_rows[row][ (colm-1)*2:(colm)*2 ] == ' x':
		# if input("Loot courpse? y ").lower() == 'y' :
		player['inventory'][0] = new_weapon(level[0])
		message_key[0] = 'looted'
	else:
		message_key[0] = ''
	newrow += trail
	newrow += map_rows[row][(colm)*2 : ]
	map_rows[row] = newrow
	p  = map_rows[row][ : (colm-1)*2]
	p += avatar
	p += map_rows[row][(colm)*2 : ]
	print(p, row)
	for x in range(1, ind):
		print( map_rows[row + x] , row + x )
	hud()

# INITIATE APP
mapit()

# CALCULATE TRANSLATION OF current_position
def move(arg):
	# print("move arg: ", arg)
	if arg == 2 : # 'n'
		if current_position[0] > 0:
			current_position[0] = current_position[0] - 1
		current_position[1] = current_position[1] 
	elif arg == 8: # 's' | '8' :
		if current_position[0] < 23:
			current_position[0] = current_position[0] + 1
		current_position[1] = current_position[1] 
		# move(8) 
	elif arg == 6: # 'e' | '6' :
		current_position[0] = current_position[0] 
		if current_position[1] > 1:
			current_position[1] = current_position[1] >> 1
		# move(6) 
	elif arg == 4 :# 'w' | '4' :
		current_position[0] = current_position[0] 
		if current_position[1] < 1 << 23:
			current_position[1] = current_position[1] << 1
		# move(4) 
	elif arg == 1 :# 'nw' | '1' :
		if current_position[0] > 0:
			current_position[0] = current_position[0] - 1
		if current_position[1] < 1 << 23:
			current_position[1] = current_position[1] << 1
		# move(1) 
	elif arg == 3 :# 'ne' | '3' :
		if current_position[0] > 0:
			current_position[0] = current_position[0] - 1 
		if current_position[1] > 1:
			current_position[1] = current_position[1] >> 1
		# move(3) 
	elif arg == 7 :# 'sw' | '7' :
		if current_position[0] < 23:
			current_position[0] = current_position[0] + 1
		if current_position[1] < 1 << 23:
			current_position[1] = current_position[1] << 1
		# move(7) 
	elif arg == 9 :# 'se' | '9' :
		if current_position[0] < 23:
			current_position[0] = current_position[0] + 1 
		if current_position[1] > 1:
			current_position[1] = current_position[1] >> 1
		# move(9) 
	monster_go()
	# header(0)
	mapit(current_position[0], current_position[1])

def heal_self(arg = '9'):
	print(arg)
	player['gold'] = player['gold'] - int(arg)
	player['health'] = player['health'] + int(arg)
	monster_go()

# USER INPUT LOOP
while True:
	command = input("Type Command: ( n s e w (at)tack cast heal x:exit )\n>>> ").lower()

	if command[:2] == 'at':
		player_attack(command[command.find(" ")+1:])
	elif command[:4] == 'cast':
		cast_spell(command[5:])
		head[0] = 1
		mapit(current_position[0], current_position[1])
	elif command[:4] == 'heal':
		if len(command) > 4:
			heal_self(command[5:])
		else:
			heal_self()
		head[0] = 0
		mapit(current_position[0], current_position[1])
			
	else:
		for i in range(len(command)):
			if command[i] == 'x':
				quit()
			elif command[i] == 'n' or '2' == command[i] :
				move(2) 
			elif command[i] == 's' or '8' == command[i] :
				move(8) 
			elif command[i] == 'e' or '6' == command[i] :
				move(6) 
			elif command[i] == 'w' or '4' == command[i] or 'q' == command[i] :
				move(4) 
			elif command[i] == '1':
				move(1) 
			elif command[i] == '3':
				move(3) 
			elif command[i] == '7' or 'a' == command[i] :
				move(7) 
			elif command[i] == '9' or 'd' == command[i] :
				move(9) 

# NEXT:
# MONSTER MAPPING WITH RANDOM MOTION move in realtime
# ITEM AQUISITION, weapons, potions, scrolls allow spell casting
# RANDOM LEVEL ENEMIES ROAMING | FIGHTING MODE
# 
##################################################################
### move monster :
# LOOP NEVER ENTERED
# def dothis():
# 	pass
# 	# map_monster()
# 	# print('move those monsters')
# 	# move monster
# def loopthis():
# 	threading.Timer(2.0, loopthis).start()
# 	print ("Hello, World!")
# 	# dothis()
# loopthis()



