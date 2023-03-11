'''

This algorithm is used to find the subset which
follows (V1,V2,...,Vk) in colex order

We need to find the smallest j such that V_j + 1 < V_(j+1)
(Or j = k if there is no such j), replacing V_j by V_j + 1
and replacing (V_1,V_2,...,V_(j-1)) by (1,2,3,...,j-1)

'''

# at first we need to initial the V list
# and the k elements from n elements
k = int(input('Please input the number of the subset elements:'))
n = int(input('Please input the n value for the subset:'))

# then we have the subset list V
# for we count the elements from 1
# we need the k+2 and 0 to be the bound
v = [int(i) for i in range(0,k+2)]

# then we let the V_(k+1) also be the boundary
v[k+1] = n+1

# we also need a flag value
Done = False

# then we do the main part
while not Done :
    # we print all the subset part
    print(v[1:k+1])

    # this is check if we have done
    # such that if we want get k = 3 from n = 5
    # then if the v[1] is not less than 3
    # we have done the last subset
    # for we have 345 this subset

    # same as we get 4 elements from 6
    # the last one must be 3456
    # so if the first one is 3 (not <6-(4-1)) we have done all the subset
    # for last one is 3456
    if v[1] < n-(k-1) :
        # we use the j to find the smallest
        # j such that V_j + 1 < V_(j+1)
        j = 1

        # this part is used to find the j
        while (v[j+1]<=v[j]+1) :
            j= j +1

        # then we increase the j element with 1
        v[j] = v[j] + 1

        # And then replace the elements before j
        # if j is not the first element in our subset

        if (j==1):
            continue
        else:
            # this is used to get the new rank
            for i in range(1,j):
                v[i] = i


    # if we have the n-(k-1) as the first
    # which means  that we have done the creating
    else:
        Done = True




