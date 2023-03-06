'''
This algorithm is used to get he Rank for the
permutation PI.

We have the property that :
Rank(PI) = n*Rank(PI')  + PART2

(j is the max number n's index and we count the location from 1)
PART2 = j-1 if Rank(PI') is odd
PART2 = n-j if Rank(PI') is even

'''

# INIT

# we get the Rank from 0
R = 0

# then we do the main part
# for we can only handle the invert of the permutaion
# we need to change our permutation to the invert one
pi_string = input("please input the permutation separated by the space:")
pi = [int(n) for n in pi_string.split()]
# we make this as the boundary
boundary_pi = max(pi) + 1
pi.insert(0, boundary_pi)
pi.append(boundary_pi)

#print(pi)

# the invert permutation pi_minus_1
# pi_minus_1[i] will
# get the index for the element i in the permutation
pi_minus_1 = [i for i in range(boundary_pi)]


# we should record the index for the value
for i in range(1,boundary_pi) :
    #print(pi.index(i))
    pi_minus_1[i] = pi.index(i)

print(pi_minus_1)

# the main part :

# At first we let the Rank to be the 0
rank = 0

for i in range(1,boundary_pi):
    # we also need to get the number of moves
    moves = 0
    for j in range(1,boundary_pi):
        if j<i and pi_minus_1[j] < pi_minus_1[i]:
            moves = moves+1
        else:
            pass

    #print(moves)

    # then we need to get the recurve part
    if rank%2!=0 :
        remainder = moves
    else:
        remainder = i-1-moves

    # then next n
    rank = i*rank + remainder

print(rank)


'''
5 1 6 2 3 7 4
'''
