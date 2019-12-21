import math
import copy
import operator
from factornode import factornode
from variablenode import variablenode
import multiprocessing
from multiprocessing import Process, current_process
from time import time
import random
import matplotlib.pyplot as plt


def create_1d_array(size):
    arr = []
    for i in range(size):
        arr.append(0)
    return arr


def create_two_dimention_array(size):
    arr = []
    for i in range(size):
        column = []
        for j in range(size):
            column.append(-1)
        arr.append(column)
    return arr


def calculation(variable_index, table, total_neighbour, values, variables):
    arrays = {}
    b_index = []
    r_index = []
    t_size = pow(2, total_neighbour)
    # print(t_size)
    for i in range(total_neighbour):
        arrays[i] = []
    for i in range(t_size):
        a = str(bin(i))[2:]
        remaining_digit = total_neighbour - len(a)
        for j in range(remaining_digit):
            a = '0' + a
        # print('a', a)
        for k in range(total_neighbour):
            if k == variable_index:
                if a[k] == '0':
                    b_index.append(i)
                else:
                    r_index.append(i)
                continue
            if a[k] == '0':
                arrays[k].append(values[variables[k]][0])
            else:
                # print(values[variables[k]])
                arrays[k].append(values[variables[k]][1])

    table1 = [0] * t_size
    # print('array', arrays)
    for i in range(t_size):
        table1[i] = table[i]
    for i in range(total_neighbour):
        if i == variable_index:
            continue
        for j in range(t_size):
            table1[j] = table1[j] + arrays[i][j]
    # print('table1',table1,b_index,r_index)
    maxB = -1000
    maxR = -1000
    for i in b_index:
        maxB = max(table1[i], maxB)
    for i in r_index:
        maxR = max(table1[i], maxR)
    t = (maxB, maxR)
    # print('t value',t)
    return t


def intermediatestep(node, ci_nodes, ci_values, factornodes, adjacentfactor, parvariable, linker_variables, vis,
                     topnode):
    vis.append(node)
    # print(node,parvariable,vis)
    values = {}
    for factor in adjacentfactor[node]:
        if factor in vis:
            continue
        vis.append(factor)
        variable = linker_variables[node][factor]
        if variable == topnode:
            continue
        # print('variable',variable)
        if variable in ci_values:
            # print('if ', variable)
            values[variable] = ci_values[variable]
        else:
            # print('else')
            val = intermediatestep(factor, ci_nodes, ci_values, factornodes, adjacentfactor, variable, linker_variables,
                                   vis, topnode)
            values[variable] = val

    # print('values',node, values)
    table = copy.deepcopy(factornodes[node].table)
    # print('table',table)
    factvariables = copy.deepcopy(factornodes[node].variables)
    total_neighbour = factornodes[node].total_neighbour
    for i in range(total_neighbour):
        if factvariables[i] not in values:
            values[factvariables[i]] = (0, 0)
    final_value = calculation(factvariables.index(parvariable), table, total_neighbour, values, factvariables)
    return final_value


def intermediatestepallfact(factors_nodes, ci_variable, ci_values, factornodes, adjacentfactor, cvar
                            , linker_variables, cluster, intermediateval):
    sumval = (0, 0)
    for fact in factors_nodes:
        if fact not in cluster[i]:
            val = intermediatestep(fact, ci_variable, ci_values, factornodes, adjacentfactor, cvar
                                   , linker_variables, [],
                                   cvar)
            sumval = tuple(map(operator.add, sumval, val))
    intermediateval[cvar] = sumval
    return intermediateval


def make_cluster(total_factor, max_cluster_num, neighbour_factor, linker_variables):
    factortocluster = []
    for i in range(total_factor):
        factortocluster.append(0)

    leaf_nodes = []
    for i in range(total_factor):
        if len(neighbour_factor[i]) == 1:
            leaf_nodes.append(i)

    total_leaf_nodes = len(leaf_nodes)
    clusters = {}
    total_cluster_no = int(math.ceil(total_factor / max_cluster_num))
    # print('to_c_n0', total_cluster_no)

    for i in range(total_cluster_no):
        clusters[i] = []

    vis_factor = []
    for i in range(total_factor):
        vis_factor.append(i)

    cluster_with_leaf = min(total_cluster_no, total_leaf_nodes)

    for i in range(cluster_with_leaf):
        vis_factor.remove(leaf_nodes[i])

        clusters[i].append(leaf_nodes[i])
        factortocluster[leaf_nodes[i]] = i

    # print(clusters, 'leaf')

    # #print(vis_factor)

    for i in range(total_cluster_no):
        if len(vis_factor) == 0:
            break

        if len(clusters[i]) == 0:
            if len(vis_factor) != 0:
                j = vis_factor[0]
                # #print(i, j)
                clusters[i].append(j)
                factortocluster[j] = i
                vis_factor.remove(j)

        added_factor = 1
        # #print('i', i)
        vis_ind = 0
        while vis_ind < len(vis_factor):
            if added_factor >= max_cluster_num:
                break
            j = vis_factor[vis_ind]
            for fact in clusters[i]:
                if j in neighbour_factor[fact]:
                    clusters[i].append(j)
                    factortocluster[j] = i
                    added_factor = added_factor + 1
                    vis_factor.remove(j)
                    vis_ind = 0

                    break

            if j in vis_factor:
                vis_ind = vis_ind + 1

        # print(i, clusters)

    # print(clusters, 'clusters with leaf')

    # print('added', total_factor)
    while len(vis_factor) != 0:
        clusters[total_cluster_no] = []

        j = vis_factor[0]
        clusters[total_cluster_no].append(j)
        factortocluster[j] = total_cluster_no
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
                    factortocluster[j] = total_cluster_no
                    added_factor = added_factor + 1
                    vis_factor.remove(j)
                    break
            if j in vis_factor:
                vis_ind = vis_ind + 1

        total_cluster_no = total_cluster_no + 1
    adjacentcluster = {}
    for i in range(total_cluster_no):
        adjacentcluster[i] = []

    for i in range(0, total_factor):
        for j in range(i + 1, total_factor):
            ci = factortocluster[i]
            cj = factortocluster[j]
            if ci != cj and linker_variables[i][j] != -1:
                if cj not in adjacentcluster[ci]:
                    adjacentcluster[ci].append(cj)
                    adjacentcluster[cj].append(ci)

    return clusters, factortocluster, adjacentcluster


def cluster_calculation(pid, factornodes, variablenodes, variables_total_adjacent, factors_total_adjacent,
                        variables_send_message, variables_final_send_message, factors_send_message,
                        factors_final_send_message, final_values):
    ct = time()
    wh = 1
    total_factor_count = len(factornodes)
    total_variable_count = len(variablenodes)

    print('proceess', pid, '-----------------------------------------')
    # print(pid, total_factor_count, total_variable_count)
    # for f in factornodes:
    # print(pid, f, factornodes[f].variables)
    # for v in variablenodes:
    # print(pid,v, variablenodes[v].factors_nodes)
    while (True):
        # --print(pid,wh)
        wh = wh + 1

        # if(total_factor_count==0&total_variable_count==0):
        # break
        flag = False
        # print(variables_total_adjacent, factors_total_adjacent)
        for i in variablenodes:
            # print('proceess',pid,'v', i)
            # print(variables_total_adjacent[i], variables_send_message[i])
            if (variables_total_adjacent[i] == 1 and variables_send_message[i] == 0):
                # print('proceess',pid,'first if')
                flag = True
                factor_index = variablenodes[i].remaining_factors[0]
                variablenodes[i].last_factor_index = variablenodes[i].factors_nodes.index(factor_index)
                # print('proceess',pid,'factor_index and remaing_factor , last_variable_index', factor_index,
                # variablenodes[i].remaining_factors, variablenodes[i].last_factor_index)
                val = variablenodes[i].find_sum_exclude_last()
                # print('proceess',pid,'val', val,factors_total_adjacent)
                factors_total_adjacent[factor_index] = factors_total_adjacent[factor_index] - 1
                # print('proceess',pid,'adjacent_node', factors_total_adjacent[factor_index])
                factornodes[factor_index].values[i] = val
                # print('proceess',pid,'factor_values', factornodes[factor_index].values)
                # print('proceess',pid,'factor_remaining_variables', factornodes[factor_index].remaining_variables)
                factornodes[factor_index].remaining_variables.remove(i)
                # print('proceess',pid,'sesh', factornodes[factor_index].remaining_variables)
                variables_send_message[i] = 1
            elif (variables_total_adjacent[i] == 0 and variables_final_send_message[i] == 0):
                # print('2nd if')
                flag = True
                final_values[i] = variablenodes[i].terminate()
                # print('proceess',pid,'final_values[i]', final_values[i]);
                for fact in variablenodes[i].factors_nodes:
                    # print('proceess',pid,'fact age', i, fact, variablenodes[i].last_factor_index)
                    if (variablenodes[i].last_factor_index != -1 and variablenodes[i].factors_nodes[
                        variablenodes[i].last_factor_index] == fact):
                        continue
                    # print('proceess',pid,'fact', i, fact)
                    f_val = tuple(map(operator.sub, final_values[i], variablenodes[i].f_values[fact]))
                    factors_total_adjacent[fact] = factors_total_adjacent[fact] - 1
                    factornodes[fact].values[i] = f_val
                    factornodes[fact].remaining_variables.remove(i)
                total_variable_count = total_variable_count - 1
                variables_final_send_message[i] = 1

        for i in factornodes:
            # print('f i', i)
            # print('f', factors_total_adjacent[i], factors_send_message[i], factors_final_send_message[i])
            if (factors_total_adjacent[i] == 1 and factors_send_message[i] == 0):
                # print('proceess',pid,'3rd if')
                flag = True
                variable_index = factornodes[i].remaining_variables[0]
                factornodes[i].last_variable_index = factornodes[i].variables.index(variable_index)
                # print('proceess',pid,'f remaining variables , last_variable_index', factornodes[i].remaining_variables[0])
                val = factornodes[i].find_value()
                # print('proceess',pid,'f val', val)
                variables_total_adjacent[variable_index] = variables_total_adjacent[variable_index] - 1
                # print('proceess',pid,'f variables adjacent', variables_total_adjacent[variable_index])
                variablenodes[variable_index].f_values[i] = val
                # print('proceess',pid,'f f_values', variablenodes[variable_index].f_values)
                variablenodes[variable_index].remaining_factors.remove(i)
                # print('proceess',pid,'f sesh remaining factors', variablenodes[variable_index].remaining_factors)
                factors_send_message[i] = 1
            elif (factors_total_adjacent[i] == 0 and factors_final_send_message[i] == 0):
                flag = True
                # print('proceess',pid,'4th if')
                variables_values = factornodes[i].terminate()
                # print(variables_values)
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

    # print('final_values',final_values)
    # for i in variablenodes:
    # print(i, final_values[i])

    # print('returninngggg')
    et = time()
    print('process', pid, et-ct)
    return final_values


def createtable(size):
    size = pow(2, size)
    table = []
    for i in range(size):
        value = random.randint(0, 100)
        table.append(value)
    return table


if __name__ == '__main__':
    x = []
    y1 = []
    y2 = []
    for clusterindex in range(2, 4,1 ):
        total_factor_count = 500
        total_variable_count = total_factor_count * 8
        max_fact_in_cluster = math.ceil(total_factor_count / clusterindex)
        linker_variables = create_two_dimention_array(total_factor_count)
        factors_total_adjacent = [0] * total_factor_count
        variables_total_adjacent = [0] * total_variable_count
        variables_send_message = [0] * total_variable_count
        factors_send_message = [0] * total_factor_count
        variables_final_send_message = [0] * total_variable_count
        factors_final_send_message = [0] * total_factor_count
        varinfact = {}
        factinvar = {}
        adjacentfactor = {}
        per_fact_var = int(math.ceil(total_variable_count / total_factor_count))
        lenvarinfact = [0] * total_factor_count
        varind = 0
        for i in range(total_factor_count):
            varinfact[i] = []
        for i in range(total_variable_count):
            factinvar[i] = []
            adjacentfactor[i] = []
        for i in range(total_factor_count):
            for j in range(per_fact_var):
                if (varind >= total_variable_count):
                    break
                varinfact[i].append(varind)
                factinvar[varind].append(i)
                factors_total_adjacent[i] = factors_total_adjacent[i] + 1
                variables_total_adjacent[varind] = variables_total_adjacent[varind] + 1
                lenvarinfact[i] = lenvarinfact[i] + 1
                varind = varind + 1

        '''
        for i in range(total_variable_count):
            factinvar[i] = []
        for i in range(total_factor_count):
            varinfact[i] = [i]
            adjacentfactor[i]=[]
            factinvar[i].append(i)
            variables_total_adjacent[i] = variables_total_adjacent[i] + 1
        for i in range(total_factor_count, total_variable_count, 1):
                factindex = random.randint(0, total_factor_count - 1)
                varinfact[factindex].append(i)
                factinvar[i].append(factindex)
                factors_total_adjacent[factindex] = factors_total_adjacent[factindex] + 1
                lenvarinfact[factindex] = lenvarinfact[factindex] + 1
                variables_total_adjacent[i] = variables_total_adjacent[i] + 1
        '''
        for i in range(1, total_factor_count, 1):
            neig_fact_index = i - 1
            adjacentfactor[neig_fact_index].append(i)
            adjacentfactor[i].append(neig_fact_index)
            linking_variable_index = random.randint(0, lenvarinfact[neig_fact_index] - 1)
            linking_variable = varinfact[neig_fact_index][linking_variable_index]
            varinfact[i].append(linking_variable)
            factinvar[linking_variable].append(i)
            variables_total_adjacent[linking_variable] = variables_total_adjacent[linking_variable] + 1
            factors_total_adjacent[i] = factors_total_adjacent[i] + 1
            linker_variables[i][neig_fact_index] = linking_variable
            linker_variables[neig_fact_index][i] = linking_variable

        # --print(variables_total_adjacent)
        # --print(factors_total_adjacent)
        # --print(varinfact)
        # --print(factinvar)
        # --print(linker_variables)
        factornodes = []
        factornodes1 = []
        variablenodes = []
        variablenodes1 = []
        for i in range(total_factor_count):
            table = createtable(len(varinfact[i]))
            fact = factornode(varinfact[i], table)
            fact1 = factornode(varinfact[i], table)
            # print(i,table)
            factornodes.append(fact)
            factornodes1.append(fact1)
        for i in range(total_variable_count):
            var = variablenode(factinvar[i])
            variablenodes.append(var)
            var1 = variablenode(factinvar[i])
            variablenodes1.append(var1)

        final_values = {}
        '''
        total_variable_count = 9
        total_factor_count = 6
        factors_total_adjacent = [2, 3, 2, 2, 3, 2]
        variables_total_adjacent = [1, 2, 1, 2, 2, 2, 1, 2, 1]
        final_values = {}

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
        adjacentfactor = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2, 4], 4: [3, 5], 5: [4]}
        linker_variables = create_two_dimention_array(6)

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
        '''
        # -------------------------------------smp-------------------------------------------------
        total_factor_count1 = total_factor_count
        total_variable_count1 = total_variable_count
        variables_total_adjacent1 = copy.deepcopy(variables_total_adjacent)
        factors_total_adjacent1 = copy.deepcopy(factors_total_adjacent)
        variables_send_message1 = copy.deepcopy(variables_send_message)
        variables_final_send_message1 = copy.deepcopy(variables_final_send_message)
        factors_send_message1 = copy.deepcopy(factors_send_message)
        factors_final_send_message1 = copy.deepcopy(factors_final_send_message)
        final_values1 = {}
        st = time()
        wh = 1
        # for f in range(len(factornodes1)):
        #     print(f, factornodes1[f].variables)
        # --for v in range(len(variablenodes1)):
        # -- print(v, variablenodes1[v].factors_nodes)

        # cause ami smp bad dicchi eikhane

        while (True):
            # -- print('where',wh)
            wh = wh + 1
            # print(total_factor_count, total_variable_count)
            # if(total_factor_count==0&total_variable_count==0):
            # break
            flag = False
            # print(variables_total_adjacent1, factors_total_adjacent1)
            for i in range(len(variables_total_adjacent1)):
                # -- print('v', i)
                # --print(variables_total_adjacent[i], variables_send_message[i])
                if (variables_total_adjacent1[i] == 1 and variables_send_message1[i] == 0):
                    # -- print('first if')
                    flag = True
                    factor_index = variablenodes1[i].remaining_factors[0]
                    variablenodes1[i].last_factor_index = variablenodes1[i].factors_nodes.index(factor_index)
                    # --print('factor_index and remaing_factor , last_variable_index', factor_index,
                    # --variablenodes[i].remaining_factors, variablenodes1[i].last_factor_index)
                    val = variablenodes1[i].find_sum_exclude_last()
                    # --print('val', val)
                    factors_total_adjacent1[factor_index] = factors_total_adjacent1[factor_index] - 1
                    # --print('adjacent_node', factors_total_adjacent1[factor_index])
                    factornodes1[factor_index].values[i] = val
                    # --print('factor_values', factornodes1[factor_index].values)
                    # --print('factor_remaining_variables', factornodes1[factor_index].remaining_variables)
                    factornodes1[factor_index].remaining_variables.remove(i)
                    # --print('sesh', factornodes1[factor_index].remaining_variables)
                    variables_send_message1[i] = 1
                elif (variables_total_adjacent1[i] == 0 and variables_final_send_message1[i] == 0):
                    # --print('2nd if')
                    flag = True
                    final_values1[i] = variablenodes1[i].terminate()
                    # --print('final_values[i]', final_values1[i]);
                    for fact in variablenodes1[i].factors_nodes:
                        # --print('fact age', i, fact, variablenodes1[i].last_factor_index)
                        if (variablenodes1[i].last_factor_index != -1 and variablenodes1[i].factors_nodes[
                            variablenodes1[i].last_factor_index] == fact):
                            continue
                            # --print('fact', i, fact)
                        f_val = tuple(map(operator.sub, final_values1[i], variablenodes1[i].f_values[fact]))
                        factors_total_adjacent1[fact] = factors_total_adjacent1[fact] - 1
                        factornodes1[fact].values[i] = f_val
                        factornodes1[fact].remaining_variables.remove(i)
                    total_variable_count1 = total_variable_count1 - 1
                    variables_final_send_message1[i] = 1

            for i in range(len(factors_total_adjacent1)):
                # --print('f i', i)
                # --print('f', factors_total_adjacent1[i], factors_send_message1[i], factors_final_send_message1[i])
                if (factors_total_adjacent1[i] == 1 and factors_send_message1[i] == 0):
                    # --print('3rd if')
                    flag = True
                    variable_index = factornodes1[i].remaining_variables[0]
                    factornodes1[i].last_variable_index = factornodes1[i].variables.index(variable_index)
                    # --print('f remaining variables , last_variable_index', factornodes1[i].remaining_variables[0])
                    val = factornodes1[i].find_value()
                    # --print('f val', val)
                    variables_total_adjacent1[variable_index] = variables_total_adjacent1[variable_index] - 1
                    # --print('f variables adjacent', variables_total_adjacent1[variable_index])
                    variablenodes1[variable_index].f_values[i] = val
                    # --print('f f_values', variablenodes1[variable_index].f_values)
                    variablenodes1[variable_index].remaining_factors.remove(i)
                    # --print('f sesh remaining factors', variablenodes1[variable_index].remaining_factors)
                    factors_send_message1[i] = 1
                elif (factors_total_adjacent1[i] == 0 and factors_final_send_message1[i] == 0):
                    flag = True
                    # --print('4th if')
                    variables_values = factornodes1[i].terminate()
                    # --print(variables_values);
                    for j in variables_values:
                        if (factornodes1[i].last_variable_index != -1 and factornodes1[i].variables[
                            factornodes1[i].last_variable_index] == j):
                            continue
                        variablenodes1[j].f_values[i] = variables_values[j]
                        variables_total_adjacent1[j] = variables_total_adjacent1[j] - 1
                        variablenodes1[j].remaining_factors.remove(i)
                    total_factor_count1 = total_factor_count1 - 1
                    factors_final_send_message1[i] = 1
            if (flag == False):
                break
        # --for i in range(len(final_values1)):
        # --print(i, final_values1[i])
        et = time()
        smptime = et - st
        y1.append(smptime)
        # x.append(clusterindex)
        print('smp', smptime)

        cluster, factortocluster, adjacentcluster = make_cluster(total_factor_count, max_fact_in_cluster,
                                                                 adjacentfactor, linker_variables)
        # \\print('main',cluster,factortocluster,adjacentcluster)
        total_cluster = len(cluster)
        ci_variable = []
        ci_values = {}
        inclustercivar = {}
        inclustercival = []
        for i in range(total_cluster):
            inclustercivar[i] = []

        for i in range(len(variablenodes)):
            len_adjfact = len(variablenodes[i].factors_nodes)
            if len_adjfact >= 2:
                for j in range(0, len_adjfact):
                    adjfj = variablenodes[i].factors_nodes[j]
                    flag = False
                    for k in range(j + 1, len_adjfact):
                        adjfk = variablenodes[i].factors_nodes[k]
                        cj = factortocluster[adjfj]
                        ck = factortocluster[adjfk]
                        if cj != ck:
                            ci_variable.append(i)
                            inclustercivar[cj].append(i)
                            inclustercivar[ck].append(i)
                            flag = True
                            break
                    if (flag):
                        break

        c_factornodes = []
        c_variablenodes = []
        c_variables_total_adjacent = []
        c_factors_total_adjacent = []
        c_factors_send_message = []
        c_factors_final_send_message = []
        c_variables_send_message = []
        c_variables_final_send_message = []
        # print('ci_variable', ci_variable)
        for i in range(len(cluster)):
            c_factornodes.append({})
            c_variablenodes.append({})
            c_variables_total_adjacent.append({})
            c_factors_total_adjacent.append({})
            c_factors_send_message.append({})
            c_factors_final_send_message.append({})
            c_variables_send_message.append({})
            c_variables_final_send_message.append({})
            inclustercival.append({})
        for i in range(len(cluster)):
            for fact in cluster[i]:
                fact_temp = factornodes[fact].newfact()
                c_factornodes[i][fact] = fact_temp
                c_factors_total_adjacent[i][fact] = len(fact_temp.variables)
                c_factors_send_message[i][fact] = 0
                c_factors_final_send_message[i][fact] = 0
                for var in fact_temp.variables:
                    if var in c_variablenodes[i]:
                        continue
                    c_variables_send_message[i][var] = 0
                    c_variables_final_send_message[i][var] = 0
                    if var not in ci_variable:
                        var_temp = variablenode(variablenodes[var].factors_nodes)
                        c_variablenodes[i][var] = var_temp
                        c_variables_total_adjacent[i][var] = len(var_temp.factors_nodes)
                    else:
                        var_factor_temp = copy.deepcopy(variablenodes[var].factors_nodes)
                        var_factor = []
                        for f in var_factor_temp:
                            if f in cluster[i]:
                                var_factor.append(f)
                        c_variablenodes[i][var] = variablenode(var_factor)
                        c_variables_total_adjacent[i][var] = len(var_factor)
        stpmp = time()
        # --print("start")
        st1st = time()
        # -------------# ------------------------------first round message passing-------------------
        process_first_round = []
        manager = multiprocessing.Manager()
        final_values = []
        p1_count = 0
        for i in range(len(cluster)):
            final_values.append(manager.dict())
            if (len(adjacentcluster[i]) == 1):
                p = Process(target=cluster_calculation, args=(
                    i, c_factornodes[i], c_variablenodes[i], c_variables_total_adjacent[i], c_factors_total_adjacent[i],
                    c_variables_send_message[i]
                    , c_variables_final_send_message[i], c_factors_send_message[i], c_factors_final_send_message[i],
                    final_values[i],))
                # --print('len', len(cluster))
                process_first_round.append(p)
                process_first_round[p1_count].start()
                p1_count = p1_count + 1

        for pro in process_first_round:
            pro.join()
        for i in range(total_cluster):
            if(len(adjacentcluster[i]) == 1):
                for j in inclustercivar[i]:
                    inclustercival[i][j] = final_values[i][j]
                    ci_values[j] = final_values[i][j]
        etfst = time()
        print('first round', etfst-st1st)
        print('intermediate')
        # ---------------------------------------------------intermediatestep----------------------------------------------

        stinter = time()
        intermediateval = []
        intermediate_step_process = []

        # print('ci value',inclustercival,ci_values)
        p2_count = 0
        for i in range(total_cluster):
            intermediateval.append(manager.dict())
            for cvar in inclustercivar[i]:
                if cvar in ci_values and len(adjacentcluster[i]) != 1:
                    inclustercival[i][cvar] = ci_values[cvar]
                    continue
                factnode = variablenodes[cvar].factors_nodes
                p = Process(target=intermediatestepallfact,
                            args=(factnode, ci_variable, ci_values, factornodes, adjacentfactor, cvar
                                  , linker_variables, cluster, intermediateval[i]))

                intermediate_step_process.append(p)
                intermediate_step_process[p2_count].start()
                p2_count = p2_count + 1

        for p in intermediate_step_process:
            p.join()
        for i in range(total_cluster):
            for cvar in inclustercivar[i]:
                if cvar in ci_values and len(adjacentcluster[i]) == 1:
                    inclustercival[i][cvar] = intermediateval[i][cvar]
        etinter = time()
        print('intermediate',etinter-stinter)
        print(inclustercival)
        # --------------------#print cluster factor nodes and variable nodes------------------------
        '''
        #print('check')
        for i in range(len(cluster)):
            #print('factor')

            for factor in c_factornodes[i]:
                #print(i, factor, c_factornodes[i][factor].variables)
            #print('variable')

            for var in c_variablenodes[i]:
                #print(i, var, c_variablenodes[i][var].factors_nodes)
        '''
        print('second round')
        st2nd = time()
        # --------------------------------------second round of cluster message passing-------------------
        c2_factornodes = []
        c2_variablenodes = []
        c2_variables_total_adjacent = []
        c2_factors_total_adjacent = []
        c2_factors_send_message = []
        c2_factors_final_send_message = []
        c2_variables_send_message = []
        c2_variables_final_send_message = []
        # print('ci_variable',ci_variable)
        for i in range(len(cluster)):
            c2_factornodes.append({})
            c2_variablenodes.append({})
            c2_variables_total_adjacent.append({})
            c2_factors_total_adjacent.append({})
            c2_factors_send_message.append({})
            c2_factors_final_send_message.append({})
            c2_variables_send_message.append({})
            c2_variables_final_send_message.append({})
            inclustercival.append({})
        for i in range(len(cluster)):
            for fact in cluster[i]:
                fact_temp = factornodes[fact].newfact()
                c2_factornodes[i][fact] = fact_temp
                c2_factors_total_adjacent[i][fact] = len(fact_temp.variables)
                c2_factors_send_message[i][fact] = 0
                c2_factors_final_send_message[i][fact] = 0
                for var in fact_temp.variables:
                    if var in c2_variablenodes[i]:
                        continue
                    c2_variables_send_message[i][var] = 0
                    c2_variables_final_send_message[i][var] = 0
                    if var not in ci_variable:
                        var_temp = variablenode(variablenodes[var].factors_nodes)
                        c2_variablenodes[i][var] = var_temp
                        c2_variables_total_adjacent[i][var] = len(var_temp.factors_nodes)
                    else:
                        var_factor_temp = copy.deepcopy(variablenodes[var].factors_nodes)
                        var_factor = []
                        for f in var_factor_temp:
                            if f in cluster[i]:
                                var_factor.append(f)
                        # print('final_var_factor',var_factor)
                        c2_variablenodes[i][var] = variablenode(var_factor)
                        c2_variables_total_adjacent[i][var] = len(var_factor)

        for i in range(total_cluster):
            for cvar in inclustercival[i]:
                # print('i','cvar',i,cvar,c2_variablenodes[i][cvar],inclustercival[i][cvar])
                c2_variablenodes[i][cvar].set_init_sum(inclustercival[i][cvar])

        # print('---------------------second round--------------------------------------')
        all_final_values = {}
        final_values1 = []
        process_second_round = []
        for i in range(len(cluster)):
            final_values1.append(manager.dict())
            p = Process(target=cluster_calculation, args=(
                i, c2_factornodes[i], c2_variablenodes[i], c2_variables_total_adjacent[i], c2_factors_total_adjacent[i],
                c2_variables_send_message[i]
                , c2_variables_final_send_message[i], c2_factors_send_message[i], c2_factors_final_send_message[i],
                final_values1[i],))
            process_second_round.append(p)
            process_second_round[i].start()

        for pro in process_second_round:
            pro.join()
        et2nd = time()
        print('second',et2nd-st2nd)

        # --for i in range(total_cluster):
        # -- print(final_values1[i])
        for i in range(total_cluster):
            for j in c2_variablenodes[i]:
                all_final_values[j] = final_values1[i][j]

        # --for i in range(total_variable_count):
        # -- print(i,all_final_values[i])
        etpmp = time()
        pmptime = etpmp - stpmp
        # --print(smptime)
        # --print(pmptime)
        x.append(clusterindex)
        # --y1.append(smptime)
        y2.append(pmptime)
    print('x', x)
    print('y1', y1)
    print('y2', y2)
    '''
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.legend(['smptime', 'pmptime(total clusters 4)'])
    plt.xlabel('factornode')
    plt.ylabel('time(seconds)')
    plt.title('SMP vs PMP for sparse graph')
    plt.show()
    '''