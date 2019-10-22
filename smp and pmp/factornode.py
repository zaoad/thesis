import copy
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

    def newfact(self):
        variables=copy.deepcopy(self.variables)
        table=copy.deepcopy(self.table)
        fact=factornode(variables,table)
        return fact
    '''
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
            #print('duk 3')
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
            #print('table1', table1)
        t = (maxB, maxR)
        return t
    '''
    def find_value(self):
        pair_maxR_maxB = self.find_maxR_maxB1(self.last_variable_index)

        return pair_maxR_maxB

    def terminate(self):
        #print('terminate')
        for i in range(self.total_neighbour):
            pair_maxR_maxB = self.find_maxR_maxB1(i)

            self.final_table[self.variables[i]] = pair_maxR_maxB
        return self.final_table

    def find_maxR_maxB1(self, variable_index):
        arrays = {}
        b_index=[]
        r_index=[]
        t_size = pow(2, self.total_neighbour)
        #print(t_size)
        for i in range(self.total_neighbour):
            arrays[i] = []
        for i in range(t_size):
            a = str(bin(i))[2:]
            remaining_digit = self.total_neighbour - len(a)
            for j in range(remaining_digit):
                a = '0' + a
            for k in range(self.total_neighbour):
                if k == variable_index:
                    if a[k] == '0':
                        b_index.append(i)
                    else:
                        r_index.append(i)
                    continue
                if a[k] == '0':
                    arrays[k].append(self.values[self.variables[k]][0])
                else:
                    #print(self.values[self.variables[k]])
                    arrays[k].append(self.values[self.variables[k]][1])

        table1 = [0]*t_size
        #print('array', arrays)
        for i in range(t_size):
            table1[i]=self.table[i]
        for i in range(self.total_neighbour):
            if i==variable_index:
                continue
            for j in range(t_size):
                table1[j]=table1[j]+arrays[i][j]
        #print('table1',table1,b_index,r_index)
        maxB=-1000
        maxR=-1000
        for i in b_index:
            maxB=max(table1[i],maxB)
        for i in r_index:
            maxR=max(table1[i],maxR)
        t = (maxB, maxR)
        return t
