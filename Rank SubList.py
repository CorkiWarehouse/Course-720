'''

This algorithm is used to get the rank for the subset
in the colex order

'''

# we also need to import the function to get
# the C(m,n) value
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


# at first we need to get our input
# a subset V

input_subset = input("please input the subset separated by the space:")
v = [int(n) for n in input_subset.split()]
v.insert(0,0)

# we also need k as the length for our subset
k = len(v)-1

# we make R to represent the Rank
R = 0

# then we do the ranking
for i in range(1,k+1) :
    R = R + func(i,v[i]-1)

# this is the result for this subset
print(R)
