"""
Pure Python implementation of Merge Sort Algorithm

Performance is not dependent on whether the set of data is sorted.
In the first part - division - algorithm recursively divide data to two-piece parts, as long as the data size is larger than the defined criterion.
In the second part - merge - merge algorithm processes data until until you get the final result. 

Note in Notion with visualisation (lang: PL): https://right-party-a74.notion.site/Sortowanie-przez-scalanie-7ff55adac03c48aabd5cb1ecce3847e7?pvs=4
"""

def mergeSort(list):
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]
	
        mergeSort(left) # repeat till len of every side is 1
        mergeSort(right)
        
        i = 0
        j = 0
        
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1

if __name__ == "__main__":
    def example():
        list = [1242, 413432, 23432, 5313432, 120]

        print(list) # [1242, 413432, 23432, 5313432, 120]
        mergeSort(list)
        print(list) # [120, 1242, 23432, 413432, 5313432]

    example()