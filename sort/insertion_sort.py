"""
Pure Python implementation of Insertion Sort Algorithm

The assumption on which insertion sort is based is the removal of an element of the data structure and inserting it in its proper position.

Efficiency:
If the list is already sorted, the execution time of such an algorithm will be linear O(n).
However, if the list is unsorted then the execution time will be O(n²).

Note in Notion (lang: PL): https://right-party-a74.notion.site/Sortowanie-przez-wstawianie-0f8e46b09f5a4bf3805e8310d4193eef?pvs=4
"""

def InsertionSort(list):
    for i in range(1, len(list)):
        j = i - 1
        element_next = list[i]
        while(list[j] > element_next) and (j >= 0):
            list[j + 1] = list[j]
            j = j - 1
            print(list)
        list[j + 1] = element_next
    return list
