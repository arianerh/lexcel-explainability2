# -*- coding: utf-8 -*-

import random
import numpy as np

TRUTH = 1

# given a point(numpy array)
# returns evaluation by distance to TRUTH (value of the ideal)
def function(point) :
	tmp = np.sum(point)*random.random()
	return abs(TRUTH-tmp)