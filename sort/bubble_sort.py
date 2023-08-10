"""
Pure Python implementation of Bubble Sort Algorithm

The easiest and the slowest algorithm used for sorting. 
Highest value on list floats up like a bubble in every run of the algorithm loop. 
Quadratic Complexity O(n^2).
Should be used only with small set of data.

Note in Notion (lang: PL): https://right-party-a74.notion.site/Sortowanie-b-belkowe-b82ef408490b41f697e367b8e2561db9?pvs=4
"""

def bubbleSort(list):
    lastElementIndex = len(list) - 1
    for passNo in range(lastElementIndex, 0, -1):
        for idx in range(passNo):
            if list[idx] > list[idx + 1]:
                list[idx], list[idx + 1] = list[idx + 1], list[idx]
    return list