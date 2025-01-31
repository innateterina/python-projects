# write a function to merge two sorted arrays into one sorted array without using built-in sorting or merging functions.
def MergeSortedArrays(sizeMaya, arrMaya, sizeDiego, arrDiego):
    result = []
    i = 0
    j = 0

    while i < sizeMaya and j < sizeDiego:
        if arrMaya[i] <= arrDiego[j]:
            result.append(arrMaya[i])
            i += 1
        else:
            result.append(arrDiego[j])
            j += 1

    # Add remaining elements from arrMaya
    while i < sizeMaya:
        result.append(arrMaya[i])
        i += 1

    # Add remaining elements from arrDiego
    while j < sizeDiego:
        result.append(arrDiego[j])
        j += 1

    return result


sizeMaya = int(input().strip())
arrMaya = list(map(int, input().strip().split()))
sizeDiego = int(input().strip())
arrDiego = list(map(int, input().strip().split()))


result = MergeSortedArrays(sizeMaya, arrMaya, sizeDiego, arrDiego)
print(*result)
