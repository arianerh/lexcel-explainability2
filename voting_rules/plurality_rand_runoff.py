# -*- coding: utf-8 -*-
import copy
import random

import voting_rules.plurality as plurality

# given a list of votes (vote = list of integers) and a list cands containing the top 2 candidates
# returns the best of the two elements based on expressed votes
# NB: in case of equivalence, randomness is used as a tie-breaker
def runoff(votes,cands) :
	pro_x = 0
	pro_y = 0
	for v in votes :
		cont = True
		i = 0
		while i in range(len(v)) and cont :
			if cands[0] in v[i] :
				if cands[1] not in v[i] :
					pro_x += 1
				cont = False
			elif cands[1] in v[i] :
				pro_y += 1
				cont = False
			i += 1
	if pro_x > pro_y :
		return [cands[0]]
	elif pro_y > pro_x :
		return [cands[1]]
	# if tie: randomness is used as tie-breaker
	return [random.choice(cands)]


# given a list of preferences (list of integers)
# returns preferences aggregrated using plurality with runoff (with random tie-breaker)
def rule(prefs) :
	p2 = copy.deepcopy(prefs)
	res= []
	while len(p2[0]) > 1 :
		top = []
		for p in p2 :
			top += [el for el in p[0]]
		score = [top.count(el) for el in set(top)]
		cands = [el for el in set(top) if top.count(el)==max(score)]
		backup = []
		# if only one candidate, we look at the second best score
		if len(cands) < 2 :
			backup = [x for x in cands]
			score.remove(max(score))
			top = [x for x in top if x != backup[0]]
			cands = [el for el in set(top) if top.count(el)==max(score)]
		# if more than two candidates have the most votes, we use randomness as a tie-breaker
		while len(cands)+len(backup) > 2 :
			cands.pop(random.randint(0,len(cands)-1))
		cands = backup + cands
		res.append(runoff(p2, cands))
		p2 = [[x for x in p if x not in res] for p in p2]
	res.append(p2[0][0])
	return res
