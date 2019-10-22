from time import time
import operator
import copy
from factornode import factornode
import random

'''
class factornode:
    table = []
    variables = []
    last_variable_index = -1
    remaining_variables = []
    count = 0
    total_neighbour = 0
    values = {}
    final_table = {}

    def __init__(self, variables, table):
        self.variables = variables
        self.remaining_variables = copy.deepcopy(variables)
        self.total_neighbour = len(variables)
        self.table = table
        self.last_variable_index = -1
        self.count = 0
        self.values = {}
        self.final_table = {}

    def find_maxR_maxB(self, variable_index):
        print('find_maxR_maxB', variable_index)
        maxB = -1000
        maxR = -1000
        if (self.total_neighbour == 1):
            print('duk 1')
            maxB = self.table[0]
            maxR = self.table[1]
        elif (self.total_neighbour == 2):
            print('duk 2', 'hi')

            table1 = [0, 0, 0, 0]
            if (variable_index == 0):
                ind1B = self.values[self.variables[1]][0]
                ind1R = self.values[self.variables[1]][1]
                array1 = [ind1B, ind1R, ind1B, ind1R]
                for i in range(4):
                    table1[i] = self.table[i] + array1[i]
                print(table1, self.table, array1)
                maxB = max(table1[0], table1[1])
                maxR = max(table1[2], table1[3])
            else:
                ind0B = self.values[self.variables[0]][0]
                ind0R = self.values[self.variables[0]][1]
                array0 = [ind0B, ind0B, ind0R, ind0R]
                for i in range(4):
                    table1[i] = self.table[i] + array0[i]

                maxB = max(table1[0], table1[2])
                maxR = max(table1[1], table1[3])
                print(maxB, maxR)


        elif (self.total_neighbour == 3):
            print('duk 3')
            table1 = [0, 0, 0, 0, 0, 0, 0, 0]
            if (variable_index == 0):
                ind1B = self.values[self.variables[1]][0]
                ind1R = self.values[self.variables[1]][1]
                ind2B = self.values[self.variables[2]][0]
                ind2R = self.values[self.variables[2]][1]
                array1 = [ind1B, ind1B, ind1R, ind1R, ind1B, ind1B, ind1R, ind1R]
                array2 = [ind2B, ind2R, ind2B, ind2R, ind2B, ind2R, ind2B, ind2R]
                for i in range(8):
                    table1[i] = self.table[i] + array1[i] + array2[i]

                maxB = max(table1[0], max(table1[1], max(table1[2], table1[3])))
                maxR = max(table1[4], max(table1[5], max(table1[6], table1[7])))

            elif (variable_index == 1):
                ind0B = self.values[self.variables[0]][0]
                ind0R = self.values[self.variables[0]][1]
                ind2B = self.values[self.variables[2]][0]
                ind2R = self.values[self.variables[2]][1]
                array0 = [ind0B, ind0B, ind0B, ind0B, ind0R, ind0R, ind0R, ind0R]
                array2 = [ind2B, ind2R, ind2B, ind2R, ind2B, ind2R, ind2B, ind2R]
                for i in range(8):
                    table1[i] = self.table[i] + array0[i] + array2[i]

                maxB = max(table1[0], max(table1[1], max(table1[4], table1[5])))
                maxR = max(table1[2], max(table1[3], max(table1[6], table1[7])))
            elif (variable_index == 2):
                ind0B = self.values[self.variables[0]][0]
                ind0R = self.values[self.variables[0]][1]
                ind1B = self.values[self.variables[1]][0]
                ind1R = self.values[self.variables[1]][1]
                array0 = [ind0B, ind0B, ind0B, ind0B, ind0R, ind0R, ind0R, ind0R]
                array1 = [ind1B, ind1B, ind1R, ind1R, ind1B, ind1B, ind1R, ind1R]
                for i in range(8):
                    table1[i] = self.table[i] + array1[i] + array0[i]

                maxB = max(table1[0], max(table1[4], max(table1[2], table1[6])))
                maxR = max(table1[1], max(table1[5], max(table1[3], table1[7])))
            print('table1', table1)
        t = (maxB, maxR)
        return t

    def find_value(self):
        pair_maxR_maxB = self.find_maxR_maxB(self.last_variable_index)

        return pair_maxR_maxB

    def terminate(self):
        print('terminate')
        for i in range(self.total_neighbour):
            pair_maxR_maxB = self.find_maxR_maxB(i)

            self.final_table[self.variables[i]] = pair_maxR_maxB
        return self.final_table
'''

class variablenode:
    f_values = {}
    factors_nodes = []
    last_factor_index = -1
    remaining_factors = []
    count = 0
    total_neighbor = -1
    f_final_table = {}

    def __init__(self, factor_nodes):
        self.factors_nodes = factor_nodes
        self.total_neighbor = len(factor_nodes)
        self.remaining_factors = copy.deepcopy(factor_nodes)
        self.f_values = {}
        self.f_final_table = {}
        self.count = 0
        self.last_factor_index = -1

    def find_sum_exclude_factor(self, index):
        sum = (0, 0)
        for i in range(self.total_neighbor):
            if (i == index):
                continue
            sum = tuple(map(operator.add, sum, self.f_values[self.factors_nodes[i]]))
        return sum

    def find_sum_exclude_last(self):
        sum = (0, 0)
        for i in self.f_values:
            sum = tuple(map(operator.add, sum, self.f_values[i]))
        return sum

    def terminate(self):
        sum = (0, 0)
        for i in self.f_values:
            sum = tuple(map(operator.add, sum, self.f_values[i]))
        return sum


def create_two_dimention_array():
    arr = []
    for i in range(5):
        column = []
        for j in range(5):
            column.append(0)
        arr.append(column)
    return arr


def create_three_dimentional_array():
    arr = []
    for i in range(5):
        column1 = []
        for j in range(5):
            column2 = []
            for k in range(5):
                column2.append(0)
            column1.append(column2)
        arr.append(column1)
    return arr
def createtable(size):
    size=pow(2,size)
    table=[]
    for i in range(size):
        value=random.randint(0,100)
        table.append(value)
    return table

st = time()
'''
factors_total_adjacent = [2, 2]
variables_total_adjacent = [1, 2, 1]
final_values = {}
total_variable_count=3
total_factor_count=2
factornodes=[]
variables=[0,1]
table=create_two_dimention_array()
table[0][0]=3
table[0][1]=5
table[1][0]=6
table[1][1]=1
fact= factornode(variables,table)
factornodes.append(fact)
variables=[1,2]
table=create_two_dimention_array()
table[0][0]=2
table[0][1]=1
table[1][0]=3
table[1][1]=7
fact= factornode(variables,table)
factornodes.append(fact)
variablenodes=[]
nei_factors=[0]
var=variablenode(nei_factors)
variablenodes.append(var)
nei_factors=[0,1]
var=variablenode(nei_factors)
variablenodes.append(var)
nei_factors=[1]
var=variablenode(nei_factors)
variablenodes.append(var)
variables_send_message=[0,0,0]
factors_send_message=[0,0]
variables_final_send_message=[0,0,0]
factors_final_send_message=[0,0]

'''
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
total_variable_count=int(input())
total_factor_count=int(input())
factors_total_adjacent=[1]*total_factor_count
variables_total_adjacent=[0]*total_variable_count
variables_send_message=[0]*total_variable_count
factors_send_message=[0]*total_factor_count
variables_final_send_message=[0]*total_variable_count
factors_final_send_message=[0]*total_factor_count
varinfact={}
factinvar={}
lenvarinfact=[1]*total_factor_count
for i in range(total_variable_count):
    factinvar[i]=[]
for i in range(total_factor_count):
    varinfact[i]=[i]
    factinvar[i].append(i)
    variables_total_adjacent[i]=variables_total_adjacent[i]+1
for i in range(total_factor_count,total_variable_count,1):
    factindex=random.randint(0,total_factor_count-1)
    varinfact[factindex].append(i)
    factinvar[i].append(factindex)
    factors_total_adjacent[factindex]=factors_total_adjacent[factindex]+1
    lenvarinfact[factindex]=lenvarinfact[factindex]+1
    variables_total_adjacent[i]=variables_total_adjacent[i]+1

for i in range(1, total_factor_count, 1):
    neig_fact_index = random.randint(0, i-1)
    linking_variable_index = random.randint(0, lenvarinfact[neig_fact_index]-1)
    linking_variable=varinfact[neig_fact_index][linking_variable_index]
    varinfact[i].append(linking_variable)
    factinvar[linking_variable].append(i)
    variables_total_adjacent[linking_variable]=variables_total_adjacent[linking_variable]+1
    factors_total_adjacent[i]=factors_total_adjacent[i]+1

print(variables_total_adjacent)
print(factors_total_adjacent)
print(varinfact)
print(factinvar)
factornodes=[]
variablenodes=[]
for i in range(total_factor_count):
  table=createtable(len(varinfact[i]))
  fact=factornode(varinfact[i],table)
  factornodes.append(fact)
for i in range(total_variable_count):
    var=variablenode(factinvar[i])
    variablenodes.append(var)

final_values={}

'''
factors_total_adjacent = [2, 3, 2, 2, 3, 2]
variables_total_adjacent = [1, 2, 1, 2, 2, 2, 1, 2, 1]
final_values = {}
total_variable_count = 9
total_factor_count = 6
factornodes = []
variables = [0, 1]
table = [3, 10, 12, 4]
fact = factornode(variables, table)
factornodes.append(fact)
variables = [1, 2, 3]
table = [5, 8, 15, 9, 7, 18, 4, 6]
fact = factornode(variables, table)
factornodes.append(fact)
variables = [3, 4]
table = [5, 20, 24, 6]
fact = factornode(variables, table)
factornodes.append(fact)
variables = [4, 5]
table = [8, 30, 34, 9]
fact = factornode(variables, table)
factornodes.append(fact)
variables = [5, 6, 7]
table = [6, 9, 25, 7, 6, 27, 3, 2]
fact = factornode(variables, table)
factornodes.append(fact)
variables = [7, 8]
table = [12, 40, 45, 13]
fact = factornode(variables, table)
factornodes.append(fact)
variablenodes = []
nei_factors = [0]
var = variablenode(nei_factors)
variablenodes.append(var)
nei_factors = [0, 1]
var = variablenode(nei_factors)
variablenodes.append(var)
nei_factors = [1]
var = variablenode(nei_factors)
variablenodes.append(var)
nei_factors = [1, 2]
var = variablenode(nei_factors)
variablenodes.append(var)
nei_factors = [2, 3]
var = variablenode(nei_factors)
variablenodes.append(var)
nei_factors = [3, 4]
var = variablenode(nei_factors)
variablenodes.append(var)
nei_factors = [4]
var = variablenode(nei_factors)
variablenodes.append(var)
nei_factors = [4, 5]
var = variablenode(nei_factors)
variablenodes.append(var)
nei_factors = [5]
var = variablenode(nei_factors)
variablenodes.append(var)
variables_send_message = [0, 0, 0, 0, 0, 0, 0, 0, 0]
factors_send_message = [0, 0, 0, 0, 0, 0]
variables_final_send_message = [0, 0, 0, 0, 0, 0, 0, 0, 0]
factors_final_send_message = [0, 0, 0, 0, 0, 0]
'''

st=time()
while (True):
    print(total_factor_count, total_variable_count)
    # if(total_factor_count==0&total_variable_count==0):
    # break
    flag = False
    print(variables_total_adjacent, factors_total_adjacent)
    for i in range(len(variables_total_adjacent)):
        print('v', i)
        print(variables_total_adjacent[i], variables_send_message[i])
        if (variables_total_adjacent[i] == 1 and variables_send_message[i] == 0):
            print('first if')
            flag = True
            factor_index = variablenodes[i].remaining_factors[0]
            variablenodes[i].last_factor_index = variablenodes[i].factors_nodes.index(factor_index)
            print('factor_index and remaing_factor , last_variable_index', factor_index,
                  variablenodes[i].remaining_factors, variablenodes[i].last_factor_index)
            val = variablenodes[i].find_sum_exclude_last()
            print('val', val)
            factors_total_adjacent[factor_index] = factors_total_adjacent[factor_index] - 1
            print('adjacent_node', factors_total_adjacent[factor_index])
            factornodes[factor_index].values[i] = val
            print('factor_values', factornodes[factor_index].values)
            print('factor_remaining_variables', factornodes[factor_index].remaining_variables)
            factornodes[factor_index].remaining_variables.remove(i)
            print('sesh', factornodes[factor_index].remaining_variables)
            variables_send_message[i] = 1
        elif (variables_total_adjacent[i] == 0 and variables_final_send_message[i] == 0):
            print('2nd if')
            flag = True
            final_values[i] = variablenodes[i].terminate()
            print('final_values[i]', final_values[i]);
            for fact in variablenodes[i].factors_nodes:
                print('fact age', i, fact, variablenodes[i].last_factor_index)
                if (variablenodes[i].last_factor_index != -1 and variablenodes[i].factors_nodes[
                    variablenodes[i].last_factor_index] == fact):
                    continue
                print('fact', i, fact)
                f_val = tuple(map(operator.sub, final_values[i], variablenodes[i].f_values[fact]))
                factors_total_adjacent[fact] = factors_total_adjacent[fact] - 1
                factornodes[fact].values[i] = f_val
                factornodes[fact].remaining_variables.remove(i)
            total_variable_count = total_variable_count - 1
            variables_final_send_message[i] = 1

    for i in range(len(factors_total_adjacent)):
        print('f i', i)
        print('f', factors_total_adjacent[i], factors_send_message[i], factors_final_send_message[i])
        if (factors_total_adjacent[i] == 1 and factors_send_message[i] == 0):
            print('3rd if')
            flag = True
            variable_index = factornodes[i].remaining_variables[0]
            factornodes[i].last_variable_index = factornodes[i].variables.index(variable_index)
            print('f remaining variables , last_variable_index', factornodes[i].remaining_variables[0])
            val = factornodes[i].find_value()
            print('f val', val)
            variables_total_adjacent[variable_index] = variables_total_adjacent[variable_index] - 1
            print('f variables adjacent', variables_total_adjacent[variable_index])
            variablenodes[variable_index].f_values[i] = val
            print('f f_values', variablenodes[variable_index].f_values)
            variablenodes[variable_index].remaining_factors.remove(i)
            print('f sesh remaining factors', variablenodes[variable_index].remaining_factors)
            factors_send_message[i] = 1
        elif (factors_total_adjacent[i] == 0 and factors_final_send_message[i] == 0):
            flag = True
            print('4th if')
            variables_values = factornodes[i].terminate()
            print(variables_values);
            for j in variables_values:
                if (factornodes[i].last_variable_index != -1 and factornodes[i].variables[
                    factornodes[i].last_variable_index] == j):
                    continue
                variablenodes[j].f_values[i] = variables_values[j]
                variables_total_adjacent[j] = variables_total_adjacent[j] - 1
                variablenodes[j].remaining_factors.remove(i)
            total_factor_count = total_factor_count - 1
            factors_final_send_message[i] = 1
    if (flag == False):
        break
for i in range(len(final_values)):
    print(i, final_values[i])

et = time()
print(et - st)


