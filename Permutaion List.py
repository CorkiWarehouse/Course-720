## init

# get the input n
n = eval(input("please input a number:"))

# the permutation pi
pi = [i for i in range(n + 2)]

# the invert permutation pi_minus_1
# pi_minus_1[i] will
# get the index for the element i in the permutation
pi_minus_1 = [i for i in range(n + 2)]

# get the direction dir
# -1 is go left and 1 is go right
dir = [i for i in range(n + 2)]

# in order to check keep track of which digits
# are moving we use the set of active digits A
# initially all the digits > 1 are active.
# if digit i comes to a boundary, it becomes
# passive(deleted from A) all digits > i become active
A = [i for i in range(2,n + 1)]

# then we get the list we need
# we count the number from 1 and end at n
# so the zero and n+1 are both the boundary
for i in range(0,n+2) :
    pi[i] = i
    pi_minus_1[i] = i

    # we let the direction all go to the left at first
    dir[i] = -1

pi[0] = n+1

'''
print(pi)
print(pi_minus_1)
print(dir)
print(A)

do the test
'''

# we could also have a sum value
# to count how many permutations we have made
sum = 0

# the main part

# at first we need a flag to tell us
# if we have done the algorithm
done = False

if n==1 :
    print(pi[1:n])
    done=True
    sum = 1


print('============================')

while not done :

    print(pi)

    sum = sum+1

    if len(A) != 0 :
        # get the max one in A that
        # we can change
        m = max(A)

        # then we get the index j for the max
        j = pi_minus_1[m]

        # we let this element go the dir step
        pi[j] = pi[j+dir[m]]

        # and we know that the element is m
        pi[j+dir[m]] = m

        # the index for the max will be updated
        # we just need to plus
        pi_minus_1[m] = pi_minus_1[m] + dir[m]

        # we also need to update the change one
        # And it is the inverse meaning
        # pi[j] have already changed to smaller one
        pi_minus_1[pi[j]] = j

        # for we have move the max one
        # for a step
        # we need to check the next step
        # if we reach the boundary
        # and there is another situation
        # if we reach one is not boundary but it bigger than the m
        if m < pi[j+2*dir[m]] :

            # then we change the direction
            dir[m] = (-1) * dir[m]

            # we also need to remove the max one
            # at now this one is not available for now
            A.remove(m)

        # and we also need to make sure that after some steps
        # we may need to move the remove items
        # so we need this step
        if len(A) != 0:
            A = list(set(A + [i for i in range(m + 1, n + 1)]))
        else:
            A = list(set([i for i in range(m + 1, n + 1)]))

    else :
        done = True

print(sum)
