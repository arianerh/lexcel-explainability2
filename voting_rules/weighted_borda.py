# -*- coding: utf-8 -*-
import random
import copy

# given a list of preferences (list of integers) and a vector of weights comprised between 0 and 1 (the lower the weight, the more power yielded)
# returns preferences aggregated using Borda using weights over voters
def rule(prefs, weights) :
	cands = [i for i in prefs[0]]
	score = [0 for _ in cands]
	res = []
	for i in range(len(prefs)) :
		j = 0
		cpt = 0
		while j in range(len(prefs[i])) and cpt < len(cands) :
			if weights[i] != 0 :
				score[cands.index(prefs[i][j])] += (len(prefs[i]) - (j+1))/weights[i]
			else :
				tmp = min(weights)
				# if the smallest weight is under 0.01, we use a 10th of the minimum
				if tmp < 0.01 :
					tmp /= 10
				# otherwise we use 0.01
				else :
					tmp = 0.01
				score[cands.index(prefs[i][j])] += (len(prefs[i]) - (j+1))/tmp
			cpt += 1
			j += 1
	while max(score) > -1 :
		tmp2 = [x for x in cands if score[cands.index(x)] == max(score)]
		res += tmp2
		for x in tmp2 :
			score[cands.index(x)] = -1
	return res


if __name__ == "__main__" :
	m = 5
	n = 6
	cands = [i for i in range(n)]
	votes = [copy.deepcopy(cands) for _ in range(m)]
	for v in votes :
		random.shuffle(v)
	print(votes)
	weights = [random.random() for _ in range(m)]
	print(weights)
	res = rule(votes, weights)
	print(res)