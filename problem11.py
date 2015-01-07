#!/usr/local/bin/python
from mathTools import *
import numpy as np

lineLen = 4

grid = readGrid('problem11.grd')
dims = grid.shape
print 'read grid with dimensions',dims
print grid

maxProd = 0
maxLine = []
maxRow = 0
maxCol = 0
maxDir = ''

for irow in range(dims[0]):
    row = grid[irow,:]
    for icol in range(dims[1]-lineLen):
        test = row[icol:icol+lineLen]
        prod = cumProd(test)
        if prod > maxProd:
            maxProd = prod
            maxLine = test
            maxRow = irow
            maxCol = icol
            maxDir = 'horizontal'

for icol in range(dims[1]):
    col = grid[:,icol]
    for irow in range(dims[0]-lineLen):
        test = col[irow:irow+lineLen]
        prod = cumProd(test)
        if prod > maxProd:
            maxProd = prod
            maxLine = test
            maxRow = irow
            maxCol = icol
            maxDir = 'vertical'

# shift rows left to check NW-SE diagonals
newGrid = np.zeros((dims[0],dims[1]*2-1),dtype=int)
for i in range(dims[1]):
    jst = dims[1]-1-i
    newGrid[i,jst:jst+dims[1]] = grid[i,:]
#print newGrid
for icol in range(dims[1]*2-1):
    col = newGrid[:,icol]
    for irow in range(dims[0]-lineLen):
        test = col[irow:irow+lineLen]
        if 0 in test:
            continue
        prod = cumProd(test)
        if prod > maxProd:
            maxProd = prod
            maxLine = test
            maxRow = irow
            maxCol = icol
            maxDir = 'diagonal (NW-SE)'

# shift rows right to check SW-NE diagonals
newGrid = np.zeros((dims[0],dims[1]*2-1),dtype=int)
for i in range(dims[1]):
    jst = i
    newGrid[i,jst:jst+dims[1]] = grid[i,:]
#print newGrid
for icol in range(dims[1]*2-1):
    col = newGrid[:,icol]
    for irow in range(dims[0]-lineLen):
        test = col[irow:irow+lineLen]
        if 0 in test:
            continue
        prod = cumProd(test)
        if prod > maxProd:
            maxProd = prod
            maxLine = test
            maxRow = irow
            maxCol = icol
            maxDir = 'diagonal (NE-SW)'


print 'Greatest product of',lineLen,'adjacent numbers occurs at',[maxRow+1,maxCol+1]
print '  in the',maxDir,'direction :',maxProd
print '  with sequence',maxLine
