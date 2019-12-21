def findf0(x1,x2,x1valueR,x1valueB):
    maxR=0
    maxB=0
    if(x1==1&x2==1):
        maxR=max(maxR,3+x1valueR)
    if(x1==1&x2==0):
        maxB=max(maxB,10+x1valueB)
    if(x1==0&x2==1):
        return 12
    if(x1==0&x2==0):
        return 4

def findf1(x1,x2,x3):
    if(x1==1&x2==1&x3==1):
        return 5
    if(x1==1&x2==1&x3==0):
        return 8
    if(x1==1&x2==0&x3==1):
        return 15
    if(x1==1&x2==0&x3==0):
        return 9
    if(x1==0&x2==1&x3==1):
        return 7
    if(x1==0&x2==1&x3==0):
        return 18
    if(x1==0&x2==0&x3==1):
        return 4
    if(x1==B&x2==B&x3==0):
        return 6

def findf2(x3,x4):
    if(x3==1&x4==1):
        return 5
    if(x3==1&x4==0):
        return 20
    if(x3==0&x4==1):
        return 24
    if(x3==0&x4==0):
        return 6

def findf3(x4,x5):
    if(x4==1&x5==1):
        return 8
    if(x4==1&x5==0):
        return 30
    if(x4==0&x5==1):
        return 34
    if(x4==0&x5==0):
        return 9

def findf4(x5,x6,x7):
    if(x5==1&x6==1&x7==1):
        return 6
    if(x5==1&x6==1&x7==0):
        return 9
    if(x5==1&x6==0&x7==1):
        return 25
    if(x5==1&x6==0&x7==0):
        return 7
    if(x5==0&x6==1&x7==1):
        return 6
    if(x5==0&x6==1&x7==0):
        return 27
    if(x5==0&x6==0&x7==1):
        return 3
    if(x5==0&x6==0&x7==0):
        return 2

def findf5(x7,x8):
    if(x7==1&x8==1):
        return 12
    if(x7==1&x8==0):
        return 40
    if(x7==0&x8==1):
        return 45
    if(x7==0&x8==0):
        return 13
def findstring(factors_neighbor):
    for node in factors_neighbor:
        if factors_neighbor[node]==None:
            print node,'node'
            return node
    return 1
x0=(0,0)
x1=(0,0)
x2=(0,0)
x3=(0,0)
x4=(0,0)
x5=(0,0)
x6=(0,0)
x7=(0,0)
x8=(0,0)
factors=['F0','F1','F2','F3','F4','F5']
total_neighbor={}
total_neighbor['F0']=2
total_neighbor['F1']=3
total_neighbor['F2']=2
total_neighbor['F3']=2
total_neighbor['F4']=3
total_neighbor['F5']=2
get_neighbor={}
get_neighbor['F0']=0
get_neighbor['F1']=0
get_neighbor['F2']=0
get_neighbor['F3']=0
get_neighbor['F4']=0
get_neighbor['F5']=0

factors_get={}
factors_get['F0']={'x0':None, 'x1':None}
factors_get['F1']={'x1':None, 'x2':None,'x3':None}
factors_get['F2']={'x3':None, 'x4':None}
factors_get['F3']={'x4':None, 'x5':None}
factors_get['F4']={'x5':None, 'x6':None,'x7':None}
factors_get['F5']={'x7':None, 'x8':None}
factors_put={}
factors_put['F0']={'x0':None, 'x1':None}
factors_put['F1']={'x1':None, 'x2':None,'x3':None}
factors_put['F2']={'x3':None, 'x4':None}
factors_put['F3']={'x4':None, 'x5':None}
factors_put['F4']={'x5':None, 'x6':None,'x7':None}
factors_put['F5']={'x7':None, 'x8':None}
edge_list_node_to_factor={'x0':['F0'],'x1':['F0','F1'],'x2':['F1'],'x3':['F1','F2'],'x4':['F2','F3'],
           'x5':['F3','F4'],'x6':['F4'],'x7':['F4','f5'],'x8':['F5']}

edge_list_factor_to_node={}
for node in edge_list_node_to_factor:
    for neighbor in edge_list_node_to_factor[node]:
        print node+" "+neighbor
        edge_list_factor_to_node[neighbor]=[]
for node in edge_list_node_to_factor:
    for neighbor in edge_list_node_to_factor[node]:
        print node+" "+neighbor
        edge_list_factor_to_node[neighbor].append(node)
print('------------------------------------')
for factor in edge_list_factor_to_node:
    for node in edge_list_factor_to_node[factor]:
        print factor,node
print('SMP algorithm')
for node in edge_list_node_to_factor:
    if len(edge_list_node_to_factor[node])==1:
        for factor in edge_list_node_to_factor[node]:
            print('ki',factor)
            factors_get[factor][node]=(0,0)
            get_neighbor[factor]=get_neighbor[factor]+1
            print(factors_get[factor],'ah')

print(factors_get)
for factor in factors:
    if total_neighbor[factor]-get_neighbor[factor]==1:
        lastnode=findstring(factors_get[factor])




