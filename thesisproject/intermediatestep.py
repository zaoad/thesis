import copy
from factornode import factornode
def create_two_dimention_array():
    arr = []
    for i in range(6):
        column = []
        for j in range(6):
            column.append(0)
        arr.append(column)
    return arr

def calculation(variable_index, table,total_neighbour,values,variables):
        print('find_maxR_maxB', variable_index)
        maxB = -1000
        maxR = -1000
        if (total_neighbour == 1):
            print('duk 1')
            maxB = table[0]
            maxR = table[1]
        elif (total_neighbour == 2):
            print('duk 2', 'hi')

            table1 = [0, 0, 0, 0]
            if (variable_index == 0):
                ind1B = values[variables[1]][0]
                ind1R = values[variables[1]][1]
                array1 = [ind1B, ind1R, ind1B, ind1R]
                for i in range(4):
                    table1[i] = table[i] + array1[i]
                print(table1, table, array1)
                maxB = max(table1[0], table1[1])
                maxR = max(table1[2], table1[3])
            else:
                ind0B = values[variables[0]][0]
                ind0R = values[variables[0]][1]
                array0 = [ind0B, ind0B, ind0R, ind0R]
                for i in range(4):
                    table1[i] = table[i] + array0[i]

                maxB = max(table1[0], table1[2])
                maxR = max(table1[1], table1[3])
                print(maxB, maxR)


        elif (total_neighbour == 3):
            print('duk 3')
            table1 = [0, 0, 0, 0, 0, 0, 0, 0]
            if (variable_index == 0):
                ind1B = values[variables[1]][0]
                ind1R = values[variables[1]][1]
                ind2B = values[variables[2]][0]
                ind2R = values[variables[2]][1]
                array1 = [ind1B, ind1B, ind1R, ind1R, ind1B, ind1B, ind1R, ind1R]
                array2 = [ind2B, ind2R, ind2B, ind2R, ind2B, ind2R, ind2B, ind2R]
                for i in range(8):
                    table1[i] = table[i] + array1[i] + array2[i]

                maxB = max(table1[0], max(table1[1], max(table1[2], table1[3])))
                maxR = max(table1[4], max(table1[5], max(table1[6], table1[7])))

            elif (variable_index == 1):
                ind0B = values[variables[0]][0]
                ind0R = values[variables[0]][1]
                ind2B = values[variables[2]][0]
                ind2R = values[variables[2]][1]
                array0 = [ind0B, ind0B, ind0B, ind0B, ind0R, ind0R, ind0R, ind0R]
                array2 = [ind2B, ind2R, ind2B, ind2R, ind2B, ind2R, ind2B, ind2R]
                for i in range(8):
                    table1[i] = table[i] + array0[i] + array2[i]

                maxB = max(table1[0], max(table1[1], max(table1[4], table1[5])))
                maxR = max(table1[2], max(table1[3], max(table1[6], table1[7])))
            elif (variable_index == 2):
                ind0B = values[variables[0]][0]
                ind0R = values[variables[0]][1]
                ind1B = values[variables[1]][0]
                ind1R = values[variables[1]][1]
                array0 = [ind0B, ind0B, ind0B, ind0B, ind0R, ind0R, ind0R, ind0R]
                array1 = [ind1B, ind1B, ind1R, ind1R, ind1B, ind1B, ind1R, ind1R]
                for i in range(8):
                    table1[i] = table[i] + array1[i] + array0[i]

                maxB = max(table1[0], max(table1[4], max(table1[2], table1[6])))
                maxR = max(table1[1], max(table1[5], max(table1[3], table1[7])))
            print('table1', table1)
        t = (maxB, maxR)
        return t


def intermediatestep(node, ci_nodes,ci_values, factornodes, adjacentfactor, parvariable,linker_variables,vis,topnode):
    vis.append(node)
    print(node,parvariable)
    values={}
    for factor in adjacentfactor[node]:
        if factor in vis:
            continue
        variable = linker_variables[node][factor]
        if variable==topnode:
           continue
        print('variable',variable)
        if variable in ci_nodes :
            print('if ', variable)
            values[variable]=ci_values[variable]
        else :
            print('else')
            val=intermediatestep(factor,ci_nodes,ci_values,factornodes,adjacentfactor,variable,linker_variables,vis,topnode)
            values[variable]=val

    print('values',node, values)
    table=copy.deepcopy(factornodes[node].table)
    print('table',table)
    factvariables=copy.deepcopy(factornodes[node].variables)
    total_neighbour=factornodes[node].total_neighbour
    for i in range(total_neighbour):
        if factvariables[i] not in values:
            values[factvariables[i]]=(0,0)
    final_value=calculation(factvariables.index(parvariable),table,total_neighbour,values,factvariables,)
    return final_value



ci_nodes=[3,5]
ci_values={3:(27,28),5:(65,72)}
factornodes=[]
variables=[0,1]
table=[3,10,12,4]
fact= factornode(variables,table)
factornodes.append(fact)
variables=[1,2,3]
table=[5,8,15,9,7,18,4,6]
fact= factornode(variables,table)
factornodes.append(fact)
variables=[3,4]
table=[5,20,24,6]
fact= factornode(variables,table)
factornodes.append(fact)
variables=[4,5]
table=[8,30,34,9]
fact= factornode(variables,table)
factornodes.append(fact)
variables=[5,6,7]
table=[6,9,25,7,6,27,3,2]
fact= factornode(variables,table)
factornodes.append(fact)
variables=[7,8]
table=[12,40,45,13]
fact= factornode(variables,table)
factornodes.append(fact)
adjacentfactor = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2, 4], 4: [3, 5],5: [4] }
linker_variables=create_two_dimention_array()

linker_variables[0][1] = 1
linker_variables[1][0] = 1
linker_variables[1][2] = 3
linker_variables[2][1] = 3
linker_variables[2][3] = 4
linker_variables[3][2] = 4
linker_variables[3][4] = 5
linker_variables[4][3] = 5
linker_variables[4][5] = 7
linker_variables[5][4] = 7
val=intermediatestep(3, ci_nodes, ci_values, factornodes, adjacentfactor, 5, linker_variables, [],5)
print(5,val)
