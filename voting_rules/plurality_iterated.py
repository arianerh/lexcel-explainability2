# -*- coding: utf-8 -*-
import copy

import voting_rules.plurality as plurality

# given a list of preferences (list of integers)
# returns preferences aggregrated using iterated plurality
def rule(prefs) :
	p2 = copy.deepcopy(prefs)
	res = []
	seen = []
	while p2[0] :
		# retrieve winner(s)
		res.append(plurality.plu(p2))
		seen += [x for x in res[-1]]
		p2 = [[x for x in p2[i] if x not in [[a] for a in seen]] for i in range(len(p2))]
	return res
