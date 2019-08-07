import random


def binary_search(data, target, low, high):
    if low > high:
        return False
    mid = (low + high) // 2
    if target == data[mid]:
        return True
    elif target < data[mid]:
        return binary_search(data, target, low, mid - 1)
    else:
        return binary_search(data, target, mid + 1, high)


def binary_search_for(data, target, low, high):
    aux = True
    while(aux):
        if low > high:
            aux = True
        mid = (low + high) // 2
        if target == data[mid]:
            aux = False
        elif target < data[mid]:
            high = high - 1
        else:
            low = low + 1
    return not aux


if __name__ == '__main__':
    data = [random.randint(0, 100) for i in range(1000)]
    data.sort()
    print(data)
    target = int(input("What number?"))
    found = binary_search(data, target, 0, len(data)-1)
    print(found)
    found1 = binary_search_for(data, target, 0, len(data)-1)
    print(found1)
