# PartitionProblem
I am assuming numbers are non-negative and items in a partition are contiguous. 



The minimum time complexity required is O(n). As I need to go to all the elements at least once in order to get the total sum. 



When the help of allocating extra memory of O(n), I can use the following logic:



a = [...input list..]

cummulative_sum = [a[0]]



for i in range(1,len(a)):

    cummulative_sum.append(cummulative_sum[i-1] + a[i])



total_sum = cummulative_sum[-1] // the last item will give total sum

if total_sum & 1 == 1:

    print "cannot be partitioned."



half_sum = total_sum >> 1 



I can do the binary search on cummulative_sum for half_sum this will improve execution time. However, the overall time complexity will remain O(n). If the item is found in cummulative_sum, the list is partitionable otherwise not.




TimeComplexity  : O(n)

Space Complexity : O(1)


 I can not apply the binary search if the input list contains negative numbers. Then I am bound to apply linear search as the cummulative_sum list will not be in increasing order.



If I don't want to allocate extra memory, then the following logic can be applied :



a = [...input list..]

total_sum = 0



for i in a:

    total_sum += i



if total_sum & 1 == 0:

    print "cannot be partitioned"



half_sum = total_sum >> 1



current_sum = 0

for i in a:

    current_sum += i

    if current_sum == half_sum:

        print "can be partitioned"

        break

    elif current_sum > half_sum

        print "cannot be partitioned"

        break



TimeComplexity  : O(n)

Space Complexity : O(1)





Now, if the case id partition can contain items from any position then,



My another solution :

TimeComplexity  : O(2^n)

Space Complexity : O(n)

