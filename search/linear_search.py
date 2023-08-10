"""
Pure Python implementation of Linear Search Algorithm

Algorithm consits in going through all the elements looking for given element.
Whenever element is found the algorithm ends. 
The advantage is that list don't have to be sorted. 
The downside is long execution time.
O(n)
"""

def linearSearch(list, item):
	index = 0
	found = False
	while index < len(list) and found is False:
		if list[index] == item:
			found = True
		else:
			index += 1
	return found

