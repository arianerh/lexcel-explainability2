# -*- coding: utf-8 -*-


import random
import itertools


# given a list of evaluations (list of a tuple [describing a coalition] and an integer [describing its associated score])
# returns the corresponding order over coalitions (list of equivalence classes)
def ordered_coals(evals) :
	res = []
	scores = [ev[1] for ev in evals]
	while scores :
		cur = [ev[0] for ev in evals if ev[1]==max(scores)]
		res.append(cur)
		scores = [x for x in scores if x != max(scores)]
	return res


# given a list of evaluations (list of a tuple [describing a coalition] and an integer [describing its associated score]) and the population N (expressed as a list of individuals)
# returns a ranking over individuals (expressed as a list of equivalence classes) according to the lex-cel
def ordered_ind(evals, N) :
	o = ordered_coals(evals)
	# o = [[(2,),(1,),(2,3),(1,2)],[(1,3),(1,2,3),(3,)]]
	# print(o)
	return lexcel(o,N)


def lexcel(o, N) :
	res = []
	cur = [i for i in N]
	cpt = 0
	seen = []

	while cpt in range(len(o)) and len(seen) != len(N) :
		score = [0 for _ in cur]
		for c in o[cpt] :
			for el in c :
				if el in cur :
					score[cur.index(el)] += 1
		cur = [el for el in cur if score[cur.index(el)]==max(score)]
		if len(cur) == 1 :
			res.append(cur)
			seen += cur
		elif len(cur) < len(N) :
			tmp = lexcel(o,cur)
			res += tmp
			seen += cur
			cpt += 1
		else :
			cpt += 1
		cur = [i for i in N if i not in seen]

	if cur :
		res.append(cur)
	return res

def launch(n) :
	coal = []
	N = [i+1 for i in range(n)]
	for i in range(1,len(N)+1) :
		coal += list(itertools.combinations(N,i))
	evals = []
	for c in coal :
		evals.append([c,random.random()])
	return ordered_ind(evals, N)