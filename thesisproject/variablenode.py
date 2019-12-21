import copy
import operator
class variablenode:
    f_values = {}
    factors_nodes = []
    last_factor_index = -1
    remaining_factors = []
    count = 0
    total_neighbor = -1
    f_final_table = {}
    init_sum=(0,0)
    def __init__(self, factor_nodes):
        self.factors_nodes = factor_nodes
        self.total_neighbor = len(factor_nodes)
        self.remaining_factors = copy.deepcopy(factor_nodes)
        self.f_values = {}
        self.f_final_table = {}
        self.count = 0
        self.last_factor_index = -1
        self.init_sum=(0,0)

    def find_sum_exclude_factor(self, index):
        sum = self.init_sum
        for i in range(self.total_neighbor):
            if (i == index):
                continue
            sum = tuple(map(operator.add, sum, self.f_values[self.factors_nodes[i]]))
        return sum

    def find_sum_exclude_last(self):
        sum = self.init_sum
        for i in self.f_values:
            sum = tuple(map(operator.add, sum, self.f_values[i]))
        return sum

    def terminate(self):
        sum =self.init_sum
        for i in self.f_values:
            sum = tuple(map(operator.add, sum, self.f_values[i]))
        return sum

    def set_init_sum(self,a):
        self.init_sum=a