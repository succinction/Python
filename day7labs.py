# Return the sum of any number of integers using *args.
# >>> combine_many(980, 667, 4432, 788, 122, 9, 545, 222)
# 7765



# def combine_many(*args):
# 	x = 0
# 	for v in args:
# 		x += v
# 	print(x)

# combine_many(980, 667, 4432, 788, 122, 9, 545, 222)
# # 7765


# # CHASE DANIELS ####################################
# def combine_many(*args):
#     return sum(integers for integers in args)
# print(combine_many(1,982,345,1234))
# # CHASE DANIELS ####################################


# def choose_longer(*args):
# 	string = ''
# 	for x in range(len(args)):
# 		if x+1 < len(args):
# 			if (len(args[x]) > len(args[x+1])):
# 			 	string = args[x]
# 			else:
# 			 	string = args[x+1]
# 	print(string)
# # Return the longest.
# # >>> 
# choose_longer("Greg", "Rooney", "darth vader")
# 'Rooney'

"""
Calculate the smallest number of coins needed to represent an amount of cents
less than 100.
Hint: Keep a running total of the remainder as you write.
>>> make_change(94)
3 quarters
1 dimes
1 nickles
4 pennies
"""

# def make_change(arg):
# 	quarters = int(arg / 25)
# 	change = arg % 25
# 	dimes = int(change / 10)
# 	change2 = change % 10
# 	nickles = int(change2/5)
# 	penies = change2 % 5
# 	print("{} cents = \n{} quarters, \n{} dimes, \n{} nickles, \n{} penies"
# 		.format(arg,quarters,dimes,nickles,penies))

# make_change(int(input("enter a number under 100: ")))

"""
Write a function that returns the meal for any given hour of the day.
Breakfast: 7AM - 9AM
Lunch: 12PM - 2PM
Dinner: 7PM - 9PM
Hammer: 10PM - 4AM
>>> meal(7)
'Breakfast time.'
>>> meal(13)
'Lunch time.'
>>> meal(20)
'Dinner time.'
>>> meal(21)
'No meal scheduled at this time.'
>>> meal(0)
'No meal scheduled at this time.'
>>> meal(3)
'Hammer time.'
>>> meal(9999)
'Not a valid time.'
"""

# list = ['Hammer', 'Hammer', 'Hammer', 'Hammer', 'Hammer', 
# 		'none', 'none', 
# 		'Breakfast', 'Breakfast', 'Breakfast', 
# 		'none', 'none', 
# 		'Lunch', 'Lunch', 'Lunch', 
# 		'none', 'none', 
# 		'none', 'none', 
# 		'Dinner', 'Dinner', 'Dinner', 
# 		'Hammer', 'Hammer', 'Hammer', 
# 		]

# def mealtime(arg):
# 	print(list[arg])

# while True:
# 	tm = input('Mealtime enter time 1-24 or q: ')
# 	if tm == 'q':
# 		quit()
# 	else:
# 		mealtime(int(tm))


def combine_many(*args):
    print(sum(args))
combine_many(980, 667, 4432, 788, 122, 9, 545, 222, 1)
# combine_many(combine_many1)


