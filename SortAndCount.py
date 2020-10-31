# Implement in Python 3 a function named "sort_and_counting" that counts the number of inversions
# in an array and returns the count and the sorted array in O(nlogn) time. For example
# sort_and_count([1, 3, 5, 2, 4, 6]) returns ([1, 2, 3, 4, 5, 6], 3).
#
# Inversions - two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j


def sort_and_count(p):
    temp = [0]*len(p)  # "empty" array of same size
    result = invCountAndSort(p, temp, 0, len(p) - 1)
    return p, result


def invCountAndSort(p, temp, left, right):  # count the total inversions in the array and sort it
    count = 0

    if left < right:
        mid = (left + right) // 2
        count += invCountAndSort(p, temp, left, mid)  # inversions count left subarray
        count += invCountAndSort(p, temp, mid + 1, right)  # inversion count right subarray
        count += merge(p, temp, left, mid, right)  # merge both sorted subarrays
    return count


def merge(p, temp, left, mid, right):
    i = left
    j = mid + 1
    k = left
    count = 0

    while i <= mid and j <= right:
        if p[i] <= p[j]:
            temp[k] = p[i]
            i += 1
            k += 1
        else:  # inversion occurs since p[i] > p[j] can occur
            temp[k] = p[j]
            count += (mid-i + 1)
            j += 1
            k += 1

    while i <= mid:  # copy remaining elements into array
        temp[k] = p[i]
        i += 1
        k += 1

    while j <= right:  # copy remaining elements into array
        temp[k] = p[j]
        j += 1
        k += 1

    for x in range(left, right + 1):  # replace original array
        p[x] = temp[x]

    return count


print(sort_and_count([1, 3, 5, 2, 4, 6]))

