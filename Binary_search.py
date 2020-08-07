value = [100,5,4,6,3,98,35,643]
value.sort()
print(value)
ln = len(value)
print("Total Digit "+str(ln))


def binary_search(value,search_value):
    first = 0
    last = len(value) - 1
    while first <=last:
        mid =(first+last)//2
        if value[last]<search_value:
            return 'Not Found'
            break
        elif value[mid] == search_value:
            return  "Found The Item index " +str(value.index(search_value)+1)
            break
        elif value[mid] > search_value:
            last = mid-1
        else:
            first= mid + 1
        if first>last:
            return 'Not Found'

print(binary_search(value,9))