# from typing import List

def binary_search_func(itemlist, item):
    '''
    to find the position of the item in a list
    using binary search
    '''

    low = 0
    high = len(itemlist) - 1

    while low <= high:
        mid = int((low + high)/2)
        guess = itemlist[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


def main():
    '''
    func to run the binary_search_func
    '''
    item = 3
    itemlist = [1, 3, 5, 7, 9]
    item_idx = binary_search_func(
        itemlist=itemlist, item=item
    )
    print(f'The {item} present at the index {item_idx}')

if __name__ == '__main__':
    main()
