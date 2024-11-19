# -*- coding: utf-8 -*-
import copy
import random


# given a vote (list of integers) and a list of candidates (list of integers)
# returns the integer in cands placed last in the vote
def least_preferred(vote,cands) :
	for k in range(len(vote)-1, -1, -1) :
		for c in vote[k] :
			if c in cands :
				return c


# given a list of votes (vote = list of equivalence classes)
# returns the winner(s) according to plurality veto
def plur_veto(votes) :
	top = []
	for v in votes :
		top += [el for el in v[0]]
	cands = list(set(top))
	score = [0 for _ in cands]
	# an element's score is the number of votes in which it is placed first
	for i in range(len(cands)) :
		score[i] += top.count(cands[i])
	# only keep candidates with a non-null score
	cands = [x for x in cands if score[cands.index(x)]!=0]
	score = [x for x in score if x!=0]
	posvoters = []
	while len(cands) > 1 :
		if not posvoters :
			posvoters = [i for i in range(len(votes))]
		# randomly select one voter and remove it from consideration to express that they have had their turn
		voter = posvoters.pop(random.randint(0,len(posvoters)-1))
		res = least_preferred(votes[voter],cands)
		score[cands.index(res)] -= 1
		cands = [x for x in cands if score[cands.index(x)]!=0]
		score = [x for x in score if x!=0]
	return cands


def rule(prefs) :
	p2 = copy.deepcopy(prefs)
	res = []
	while p2[0] :
		res.append(plur_veto(p2))
		p2 = [[x for x in p2[i] if x not in res] for i in range(len(p2))]
	return res
