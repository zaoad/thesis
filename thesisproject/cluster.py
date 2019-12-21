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
