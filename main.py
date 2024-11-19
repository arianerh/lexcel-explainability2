# -*- coding: utf-8 -*-

from orders import lexcel
from voting_rules import borda, plurality_iterated, plurality_veto, plurality_rand_runoff

if __name__ == "__main__" :
	n = 4
	if input("Population is by default of size 4. Do you want to enter another size? [Y/N] ").lower() == "y" :
		try : 
			n = int(input("Enter desired size of population : "))
		except ValueError as ve:
			print("Incorrect type of input. Size of population is set to 4 by default")
			n = 4
	print("\n")
	nb_orders = 5
	if input("Number of orders is by default set to 5. Do you want to enter another number? [Y/N] ").lower() == "y" :
		try : 
			nb_orders = int(input("Enter desired number of orders: "))
		except ValueError as ve:
			print("Incorrect type of input. Number of orders is set to 5 by default")
			nb_orders = 5
	print("\n")
	votes = []
	for _ in range(nb_orders) :
		votes.append(lexcel.launch(n))
	print("votes are :")
	for v in votes :
		print(v)
	print("Rules implemented for aggregation:\n1- Borda\n2- Plurality\n3- Plurality with (random) runoff\n4- Plurality with veto")#\n5- Weighted Borda")
	res = []
	try :
		rule = int(input("Enter the number of the selected rule: "))
	except ValueError as ve :
		print("Incorrect type of input. Rule is by default set to 1 (Borda)\n")
		rule = 1

	if rule < 0 or rule > 4 : 
		print("Incorrect rule number. Rule is by default set to 1 (Borda)\n")
		rule = 1
	if rule == 1 :
		res = borda.rule(votes)
	elif rule == 2 :
		res = plurality_iterated.rule(votes)
	elif rule == 3 :
		res = plurality_rand_runoff.rule(votes)
	elif rule == 4 :
		res = plurality_veto.rule(votes)
	# elif rule == 5 :
	# 	res = weighted_borda.rule(votes,[random.randint() for _ in range(n)])	
	print("result is "+str(res))