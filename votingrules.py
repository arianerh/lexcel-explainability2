# -*- coding: utf-8 -*-

# given a list of local rankings (list of rankings, each being a list of lists of integers) and the studied population pop
# returns preferences (list of lists of integers) aggregrated using Borda
def borda(prefs, pop) :
	cands = [i for i in pop]
	score = [0 for _ in cands]
	res = []
	for i in range(len(prefs)) :
		j = 0
		cpt = 0
		while j in range(len(prefs[i])) and cpt < len(cands) :
			for k in prefs[i][j] :
				score[cands.index(k)] += (len(prefs[i]) - (j+1))
			cpt += 1
			j += 1
	# print(score)
	while max(score) > -1 :
		tmp2 = [x for x in cands if score[cands.index(x)] == max(score)]
		res.append(tmp2)
		for x in tmp2 :
			score[cands.index(x)] = -1
	return res

# given a list of local rankings (list of rankings, each being a list of lists of integers), the studied population pop and a vector of weights comprised between 0 and 1 (the lower the weight, the more power yielded)
# returns preferences (list of equivalence classes) aggregated using Borda using weights over the rankings
def weighted_borda(prefs, pop, weights) :
	print("weights are "+str(weights))
	cands = [i for i in pop]
	score = [0 for _ in cands]
	res = []
	for i in range(len(prefs)) :
		j = 0
		cpt = 0
		while j in range(len(prefs[i])) and cpt < len(cands) :
			if weights[i] != 0 :
				for k in prefs[i][j] :
					score[cands.index(k)] += (len(prefs[i]) - (j+1))/weights[i]
			else :
				tmp = min(weights)
				# if the smallest weight is under 0.01, we use a 10th of the minimum
				if tmp < 0.01 :
					tmp /= 10
				# otherwise we use 0.01
				else :
					tmp = 0.01
				for k in prefs[i][j] :
					score[cands.index(k)] += (len(prefs[i]) - (j+1))/tmp
			cpt += 1
			j += 1
	while max(score) > -1 :
		tmp2 = [x for x in cands if score[cands.index(x)] == max(score)]
		res.append(tmp2)
		for x in tmp2 :
			score[cands.index(x)] = -1
	return res