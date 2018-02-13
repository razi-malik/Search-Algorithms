#!/usr/bin/env python

'''
Binary Search:

NOTE: Binary search is always performed on sorted array
'''

def binarySearch(alist, item):
	if len(alist) == 0:
		return False
	else:
		mid = len(alist)/2
		if item == alist[mid]:
			return True
		else:
			if item < alist[mid]:
				return binarySearch(alist[: mid], item)
			else:
				return binarySearch(alist[mid + 1 :], item)

testlist = [1, 5, 7, 20, 30]
print binarySearch(testlist, 5)
print binarySearch(testlist, 29)





























