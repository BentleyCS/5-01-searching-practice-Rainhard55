import random
def randomSearch(items:list, target) -> int:
    tries = 0

    while True:
        index = random.randint(0, len(items)-1)
        tries += 1

        if items[index] == target:
            print(f"Found {target} at index {index}")
            return index
pass
print(randomSearch([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 10))

def linearSearch(items:list, target) ->tuple[int,int]:
    checks = 0

    for index in range(len(items)):
        checks += 1
        if items[index] == target:
            return index, checks

    return -1, checks


    #Modify the below function such that it implements linear search.
    #Return the index of the target value and the amount of checks it took
    #if the value is not within the list return -1 as the index.
    pass


def binarySearch(items:list, target) -> tuple[int,int]:
    left, right = 0, len(items)-1
    checks = 0
    while left <= right:
        mid = (left+right)//2
        checks += 1
        if items[mid] == target:
            return mid, checks
        elif items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, checks
    # Modify the below function such that it implements linear search.
    # Return the index of the target value and the amount of checks it took
    # if the value is not within the list return -1 as the index.

pass
