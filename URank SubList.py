'''

This algorithm is used to get the
unranked value for the subset with k elements

inorder to find the unrank value for m with given k
we need to find the largest binomial coefficient C(k,i) that is  <= m
where m = sum of C(i,V_i-1) for i in range(1,k+1)

Then we just subtract the binomial coefficient C(k,i) from m
and repeat with k replaced by k-1


'''

# this is the function for get the C(m,n)
def func(m,n):
    a=b=result=1
    if m>n:
        print("n不能小于m 且均为整数")
    elif ((type(m)!=int)or(type(n)!=int)):
        print("n不能小于m 且均为整数")
    else:
        minNI=min(m,n-m)#使运算最简便
        for j in range(0,minNI):
        #使用变量a,b 让所用的分母相乘后除以所有的分子
            a=a*(n-j)
            b=b*(minNI-j)
            result=a//b #在此使用“/”和“//”均可，因为a除以b为整数
        return result


# At first we need to input the rank number
m = int(input('Please input the rank value:'))
k = int(input('Please input the subset length:'))

# then we do the unrank part
# we let R be the current value for the Rank value
R = m

# we also need a list to store the unrank result
v = [0 for i in range(0,k+1)]

#
for i in range(k,0,-1):
    # we use p as the i which we want
    p = i

    # then we find the biggest
    while (func(i,p) <= R):
        p = p + 1

    # then we subtract
    R = R - func(i,p-1)

    # And we store the result
    v[i] = p

print(v[1:k+1])

