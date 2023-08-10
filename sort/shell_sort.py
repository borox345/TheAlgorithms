"""
Pure Python implementation of Shell Sort Algorithm

Bubble sort algorithm compares the values of immediate neighbors and change their order. 
In the first run, instead of direct neighbors, positions that are a certain number of places away are compared. 
In each subsequent run, this number is reduced by half.

Note in Notion (lang: PL): https://right-party-a74.notion.site/Sortowanie-Shella-7af59ececccc4683addc2416b3e0da30?pvs=4
"""

def shellSort(list):
	distance = len(list) // 2
	while distance > 0:
		for i in range(distance, len(list)):
			temp = list[i]
			j = i
			while j >= distance and list[j - distance] > temp:
				list[j] = list[j - distance]
				j = j - distance
			list[j] = temp
		distance = distance // 2
	return list