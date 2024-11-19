# -*- coding: utf-8 -*-

# given a list of preferences (list of integers)
# returns preferences aggregrated using Borda
def rule(prefs) :
	cands = []
	for k in range(len(prefs[0])) :
		cands += [i for i in prefs[0][k]]
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
	while max(score) > -1 :
		tmp2 = [x for x in cands if score[cands.index(x)] == max(score)]
		res.append(tmp2)
		for x in tmp2 :
			score[cands.index(x)] = -1
	return res
