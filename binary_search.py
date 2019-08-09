import random


def binary_search(data, target, low, high, count):
    if low > high:
        print(count)
        return False
    mid = (low + high) // 2
    if target == data[mid]:
        print(count)
        return True
    elif target < data[mid]:
        return binary_search(data, target, low, mid - 1, count + 1)
    else:
        return binary_search(data, target, mid + 1, high, count + 1)


def binary_search_for(data, target, low, high):
    aux = True
    aux1 = True
    count = 0
    while(aux):
        if low >= high:
            aux1 = False
            aux = False
        mid = (low + high) // 2
        if target == data[mid]:
            aux = False
            aux1 = True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
        count = count + 1
    print(count)
    return aux1


if __name__ == '__main__':

    data = [random.randint(0, 1000) for i in range(1000)]
    data.sort()
    print(data)
    target = int(input("What number?"))
    found = binary_search(data, target, 0, len(data)-1, 0)
    print(found)
    found1 = binary_search_for(data, target, 0, len(data)-1)
    print(found1)
