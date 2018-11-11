def partitionSum(arr, n, set1, set2, sum1, sum2, pos):

    if (pos == n):

        if (sum1 == sum2):
            for i in range(0, len(set1)):
                print("{} ".format(set1[i]), end="");
            print("")

            for i in range(0, len(set2)):
                print("{} ".format(set2[i]), end="");
            print("")
            return True

        else:
            return False

    set1.append(arr[pos])

    res = partitionSum(arr, n, set1, set2,
                   sum1 + arr[pos], sum2, pos + 1)

    if (res):
        return res

    set1.pop()
    set2.append(arr[pos])

    return partitionSum(arr, n, set1, set2, sum1,
                    sum2 + arr[pos], pos + 1)

def isPartitionPoss(arr, n):

    sum = 0

    for i in range(0, n):
        sum += arr[i]

    if (sum & 1 != 0):
        return False

    set1 = []
    set2 = []

    return partitionSum(arr, n, set1, set2, 0, 0, 0)

arr = [1,2,4,5]
n = len(arr)
if (isPartitionPoss(arr, n) == False):
    print("-1")

