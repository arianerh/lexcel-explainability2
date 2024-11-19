# -*- coding: utf-8 -*-
import copy

# given a list of preferences (list of equivalence classes)
# returns winner(s) using plurality
def plu(prefs) :
	top = []
	# retrieve top elements
	for p in prefs :
		top += [el for el in p[0]]
	cands = set(top)
	# if all candidates appear once, they all have the same amount of votes
	if len(cands) == len(top) :
		return top
	# otherwise we only retrieve those with the most votes
	m = max([top.count(el) for el in top])
	return [el for el in cands if top.count(el)==m]

