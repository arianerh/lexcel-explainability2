# -*- coding: utf-8 -*-

import numpy as np
import itertools
import random

import model
import votingrules

# Ranking contains a numpy array of Orders (to be used to look at global explanation)
class Ranking :
	# votes is a list of Orders
	def __init__(self, votes) :
		self.votes = np.array(votes)

	def __str__(self) :
		for v in self.votes :
			print(v)

# Order contains the size of the population (popsize), the nb of coalitions present in it (nb_el) and its description as a numpy array of popsize-sized binary vectors describing the coalitions (e.g. for a population of size 3, [1,0,1] represents coalition 02)
class Order :
	# popsize is an int
	def __init__(self, popsize) :
		self.pop = [i for i in range(popsize)]
		self.nb_el = 0

	# given a coalition described by a binary vector (numpy ndarray)
	# prints the associated coalition
	def coal_to_str(self,c) :
		res = ""
		for i in range(len(c)) :
			if c[i] == 1 :
				res += str(i)
		return res

	def __str__(self) :
		res = self.coal_to_str(self.prefs[0])
		for i in range(1,len(self.prefs)) :
			res += (" ≻  "+self.coal_to_str(self.prefs[i]))
		return res

	# given an element (list of binary values describing coalition)
	# returns index of element if present in the order ; -1 if not
	# NB: by construction, an element may appear only once in an Order
	def index(self, elem) :
		for i in range(0, prefs.size) :
			if elem in prefs[i] :
				return i
		return -1

	# given two coalitions X and Y
	# returns True if X > Y, False if X < Y
	def is_before(self, X, Y) :
		if self.index(X) < self.index(Y) :
			return True
		return False

	# returns ranking over elements using the lexcel (as list of equivalence classes)
	# NB: by construction, if pop is of size 3, the elements will be named 0,1,2
	def lexcel(self) :
 		pop2 = [i for i in self.pop]
 		cpt = 0
 		res = [[x for x in pop2]]
 		# print(res)
 		while cpt < self.prefs.size :
 			res2 = [x for x in res]
 			for k in range(len(res)-1,-1,-1) :
 				worst = [i for i in res[k] if self.prefs[cpt][i]==0]
 				best = [i for i in res[k] if self.prefs[cpt][i]==1]
 				if worst and best :
 					res2[k] = [i for i in res[k] if self.prefs[cpt][i]==0]
 					res2.insert(k,[i for i in res[k] if self.prefs[cpt][i]==1])
 			# print(res, res2)
 			# print(cpt)
 			cpt += 1
 			if len(res2) == len(self.pop) :
 				return res2
 			res = res2
 		return res2

	# given preferences (list of coalitions described as binary vectors)
	# sts object's preferences
	def set_prefs(self, prefs) :
		nb_els = len(prefs)
		self.prefs = np.array(prefs)

	# given a coalition c described as a tuple
	# returns it as a list describing the coalition as a binary vector
	def coal_to_bin(self,c) :
		res = [0 for _ in self.pop]
		for el in c :
			res[el] = 1
		return res

	# given a point (numpy array of values) to evaluate, and a list of donor points to complete it with
	# generates a ranking over coalitions based on performance of donor point modified with some of the donor points
	def point_evaluation(self, current_point, donor_points) :
		coals = list()
		for i in range(1,len(self.pop)+1) :
			coals += list(itertools.combinations(self.pop,i))
		score = [0 for _ in coals]
		score.insert(0,model.function(current_point))
		# step 1: evaluate coalitions by changing the values of features not present in it
		for i in range(len(coals)) :
			tmp = np.copy(current_point)
			# select a donor point among those in the given list
			donor = random.sample(donor_points,1)
			# c indicates which elements to keep intact in current_point
			for k in range(len(coals)) :
				# if the element is not set to 1, we modify it by setting it to donor_point's value
				if coals[k] == 0 :
					tmp[k] = donor[k]
			score[i] = model.function(tmp)
		# step 2: order coalitions to set preferences
		p = []
		while coals :
			# remember we assume there will be no equivalence
			m = max(score)
			best = [coals[i] for i in range(len(coals)) if score[i] == m]
			p.append(self.coal_to_bin(best[0]))
			coals.remove(best[0])
			score = [x for x in score if x != m]
		# print(p)
		self.set_prefs(p)


# given the size of the population n
# returns a list of local preferences (rankings, each described by a list of lists) determined from an user-input number of points
def local_evaluation(n) :
	points = []
	nb_points = 4
	if input("Number of points to use for study is by default 4. Do you want to enter another size? [Y/N] ").lower() == "y" :
		try : 
			n = int(input("Enter desired number of points: "))
		except ValueError as ve:
			print("Incorrect type of input. Size of population is set to 4 by default")
			n = 4
	for i in range(nb_points) :
		points.append(generate_point(n))
		print(points[-1])
	local_prefs = []
	for p in points :
		o = Order(n)
		o.point_evaluation(p, [x for x in points if np.array_equal(x,p)])
		local_prefs.append(o.lexcel())
	return local_prefs


# given a population (list of integers from 0 to the size of the population)
# returns (randomly-generated) preferences over coalitions using binary vectors to describe each coalition
def generate_prefs(pop) :
	coal = list()
	for i in range(len(pop)+1) :
		coal += list(itertools.combinations(pop,i))
	coal = random.sample(coal, len(coal))
	# print(coal)
	p = []
	for c in coal :
		tmp = [0 for _ in pop]
		for i in c :
			tmp[i] = 1
		p.append(tmp)
	return p


# given a size s
# returns a point (numpy array) composed of s values between 0 and 1
def generate_point(s) :
	return np.array([random.random() for _ in range(s)])


# local performance: given a point, deduce a ranking over features by testing "coalitions" performance
if __name__ == "__main__" :
	n = 4
	if input("Population is by default of size 4. Do you want to enter another size? [Y/N] ").lower() == "y" :
		try : 
			n = int(input("Enter desired size of population: "))
		except ValueError as ve:
			print("Incorrect type of input. Size of population is set to 4 by default")
			n = 4
	# m = 10
	# votes = []
	local_prefs = local_evaluation(n)
	print("local prefs are ")
	for p in local_prefs :
		print(p)
	global_prefs_borda = votingrules.borda(local_prefs, [i for i in range(n)])
	print(global_prefs_borda)
	global_prefs_wborda = votingrules.weighted_borda(local_prefs, [i for i in range(n)], [random.random() for _ in range(len(local_prefs))])
	print(global_prefs_wborda)