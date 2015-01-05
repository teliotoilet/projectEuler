#!/usr/local/bin/python
import numpy as np

#nnum = 10
nnum = 100

nums = np.arange(1,nnum+1)
print sum(nums)**2 - np.dot(nums,nums)

