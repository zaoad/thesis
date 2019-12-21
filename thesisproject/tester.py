import operator
# 2 dimentional array
import math

"""
arr=[]
for i in range(5):
    column=[]
    for j in range(5):
        column.append(0)
    arr.append(column)

arr=[]
#3 dimentional a rray
for i in range(5):
    column1=[]
    for j in range(5):
       column2=[]
       for k in range(5):
           column2.append(0)
       column1.append(column2)
    arr.append(column1)
a=1
for i in range(5):
    for j in range(5):
        for k in range(5):
            arr[i][j][k]=a
            a=a+1
dict={1:(1,2),2:(2,4)}
for x in dict:
    print(dict[x])
b=(1,2)
c=(2,4)
d=tuple(map(operator.add,dict[1],dict[2]))
print(d)
"""
'''
import matplotlib.pyplot as plt

# x axis values
x = [1,2,3]
# corresponding y axis values
y = [2,4,1]

# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')

# function to show the plot
plt.show()
'''


def make_cluster(total_factor, neighbour_factor, max_cluster_num):
    leaf_nodes = []
    for i in range(total_factor):
        if len(neighbour_factor[i]) == 1:
            leaf_nodes.append(i)

    total_leaf_nodes = len(leaf_nodes)
    clusters = {}
    total_cluster_no = int(math.ceil(total_factor / max_cluster_num))
    print('to_c_n0', total_cluster_no)

    for i in range(total_cluster_no):
        clusters[i] = []

    vis_factor = []
    for i in range(total_factor):
        vis_factor.append(i)

    cluster_with_leaf = min(total_cluster_no, total_leaf_nodes)

    for i in range(cluster_with_leaf):
        vis_factor.remove(leaf_nodes[i])

        clusters[i].append(leaf_nodes[i])

    print(clusters, 'leaf')

    # print(vis_factor)

    for i in range(total_cluster_no):
        if len(vis_factor) == 0:
            break

        if len(clusters[i]) == 0:
            if len(vis_factor) != 0:
                j = vis_factor[0]
                # print(i, j)
                clusters[i].append(j)
                vis_factor.remove(j)

        added_factor = 1
        # print('i', i)
        vis_ind = 0
        while vis_ind < len(vis_factor):
            if added_factor >= max_cluster_num:
                break
            j = vis_factor[vis_ind]
            for fact in clusters[i]:
                if j in neighbour_factor[fact]:
                    clusters[i].append(j)
                    added_factor = added_factor + 1
                    vis_factor.remove(j)
                    vis_ind = 0

                    break

            if j in vis_factor:
                vis_ind = vis_ind + 1

        print(i, clusters)

    print(clusters, 'clusters with leaf')

    print('added', total_factor)
    while len(vis_factor) != 0:
        clusters[total_cluster_no] = []

        j = vis_factor[0]
        clusters[total_cluster_no].append(j)
        vis_factor.remove(j)

        added_factor = 1
        vis_ind = 0
        while vis_ind < len(vis_factor):
            if added_factor >= max_cluster_num:
                break
            j = vis_factor[vis_ind]
            for fact_in in clusters[total_cluster_no]:
                if j in neighbour_factor[fact_in]:
                    clusters[total_cluster_no].append(j)
                    added_factor = added_factor + 1
                    vis_factor.remove(j)
                    break
            if j in vis_factor:
                vis_ind = vis_ind + 1

        total_cluster_no = total_cluster_no + 1

    return clusters

'''
arr=[]
for i in range(6):
    column=[]
    for j in range(6):
        column.append(-1)
    arr.append(column)


arr[0][1]=1
arr[1][2]=3





arr[2][3]=4
arr[3][4]=5
arr[4][5]=7
'''
'''
arr = {}
arr[0] = [1, 5]
arr[1] = [0, 2]
arr[2] = [1, 3, 4]
arr[3] = [2]
arr[4] = [2]
arr[5] = [0, 6, 7, 12]
arr[6] = [5, 13]
arr[7] = [5, 8, 9]
arr[8] = [7]
arr[9] = [7, 10, 11, 14]
arr[10] = [9, 18, 19]
arr[11] = [9, 15, 16]
arr[12] = [5]
arr[13] = [6]
arr[14] = [9, 17, 20]
arr[15] = [11]
arr[16] = [11]
arr[17] = [14]
arr[18] = [10]
arr[19] = [10]
arr[20] = [14]
print(arr)

cluster = make_cluster(21, arr, 6)
print(cluster)
#----------------
a = str(bin(10))[2:]
total_digit = 5
remaining_digit=total_digit-len(a)
print(remaining_digit)
for i in range(remaining_digit):
    a='0'+a

print(a)
for i in range(5,9):
    print(i)
total_neighbour=10
arrays={}
#-----------------
t_size=pow(2,total_neighbour)
for i in range(total_neighbour):
    arrays[i] = []

for i in range(t_size):
    a = str(bin(i))[2:]
    remaining_digit = total_neighbour - len(a)
    for j in range(remaining_digit):
        a = '0' + a
    for k in range(total_neighbour) :
        if k==variable_node:
            if(a[k]==0)
                t0.append(k)
            else:
                t1.append(k)
        if a[k]==0:
            arrays[k].append(self.values[self.variables[k]][0])
        else:
            arrays[k].append(self.values[self.variables[k]][0])

'''
import matplotlib.pyplot as plt

x =[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
y1 =[5.5358195304870605, 5.5755791664123535, 5.604951858520508, 5.5987019538879395, 5.524821043014526, 5.766504526138306, 5.779725074768066, 5.592265367507935, 5.796171188354492, 5.672652006149292, 5.665135383605957, 5.49776291847229, 5.783466577529907, 5.628030300140381, 5.541230201721191, 5.42552638053894, 5.82379937171936, 5.286451101303101, 5.605793237686157]
y2 =[5.515553951263428, 2.907907724380493, 1.9079842567443848, 1.8312263488769531, 1.536309003829956, 1.499476432800293, 1.4143948554992676, 1.445406436920166, 1.5247340202331543, 1.6020686626434326, 1.74582839012146, 1.829035758972168, 1.9647033214569092, 1.9798376560211182, 2.11293625831604, 2.2741518020629883, 2.404989242553711, 2.524988889694214, 2.7403371334075928]
plt.plot(x,y1)
plt.plot(x,y2)

plt.legend(['smptime','pmptime'])
plt.xlabel('number of clusters')
plt.ylabel('time(seconds)')
plt.title('SMP vs PMP for dense graph(total factor 500)')
plt.show()
'''
plt.plot(x, y1)
    plt.plot(x, y2)
    plt.legend(['smptime', 'pmptime(total clusters 4)'])
    plt.xlabel('factornode')
    plt.ylabel('time(seconds)')
    plt.title('SMP vs PMP for sparse graph')
    plt.show()
'''