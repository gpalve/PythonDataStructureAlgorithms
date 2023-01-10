# function for finding smallest element from given list of elements
def find_smallest(mylist):
    smallest = mylist[0]
    smallest_index = 0
    for i in range(1,len(mylist)):
        if mylist[i] < smallest:
            smallest = mylist[i]
            smallest_index = i
    return smallest_index

def selectionSort(mylist):
    newList = []
    for i in range(len(mylist)):
        smallest = find_smallest(mylist)
        newList.append(mylist.pop(smallest)) # very crucial step to pop the smallest from old list.
        print("Original List",mylist,"New List",newList,"\n")
    return newList

mylist = [25,45,78,12]
print("Original List",mylist,"\n")
print("Sorting.....\n")
selectionSort(mylist)