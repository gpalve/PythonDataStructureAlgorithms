def getBinarySearchItem(list,item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid  = int(( low + high ) / 2 )
        guess = list[ mid ]
        print("Low =" + str(low) + " High = " + str(high) +  " Mid = " + str(mid) + " guess =" + str(guess) + " item = " + str(item)) 
        if guess == item:
            return "Item found at index " + str(mid) + ">>>" + str(list[ mid ])
        if guess < item:
            low = mid + 1
        else:
            high = mid -1
    return None

mylist = list(range(0,4096))
# Binary search has an efficiency of O(log n) runtime. It halves the number of list every time.
print(getBinarySearchItem(mylist,1377))