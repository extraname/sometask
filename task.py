from math import factorial

"""
Task 1.
Если мы из корректно записанного арифметического выражения, содержащего числа,
знаки операций и открывающие и закрывающие круглые скобки выбросим числа и знаки
операций, а затем запишем оставшиеся в выражении скобки без пробелов между ними,
то полученный результат назовем правильным скобочным выражением [скобочное
выражение "(()(()))" - правильное, а "()(" и "())(" - нет].
Найти число правильных скобочных выражений, содержащих N открывающихся и N
закрывающихся скобок. N вводится с клавиатуры. N неотрицательное целое число.

1 step - create main function only_nice_brackets with low level validator 
2 step - create recursion wrapper _only_nice_brackets 
3 step - return result
"""


def only_nice_brackets(n):
    string_ = [""] * 2 * n
    if n > 0:
        _only_nice_brackets(string_, 0, n, 0, 0)
    return


def _only_nice_brackets(string_, position, n, open_bracket, close_bracket):
    if close_bracket == n:
        for i in string_:
            print(i, end="")
        print()
        return
    else:
        if open_bracket > close_bracket:
            string_[position] = ')'
            _only_nice_brackets(string_, position + 1, n, open_bracket, close_bracket + 1)
        if open_bracket < n:
            string_[position] = '('
            _only_nice_brackets(string_, position + 1, n, open_bracket + 1, close_bracket)


print(only_nice_brackets(0))

''' 
Task 2.
You are given a list of cities. Each direct connection between two cities has its transportation
cost (an integer bigger than 0). The goal is to find the paths of minimum cost between pairs of
cities. Assume that the cost of each path (which is the sum of costs of all direct connections
belonging to this path) is at most 200000. The name of a city is a string containing characters
a,...,z and is at most 10 characters long.2)


The Floyd algorithm is used to solve the problem. First, we create a matrix class, 
instances of the class will be input. 
The main problem for solving the problem is to create a layout of the correct matrix
'''


class Matrix:
    inf = 100000

    def __init__(self, ssize):
        self.size = ssize
        self.matrix = [[self.inf for x in range(ssize)] for x in range(ssize)]
        for i in range(self.size):
            self.matrix[i][i] = 0

    def __getitem__(self, i):
        return self.matrix[i]


    def floyd(self):
        for k in range(self.size):
            for i in range(self.size):
                for j in range(self.size):
                    if self.matrix[i][k] != self.inf and self.matrix[k][j] != self.inf:
                        self.matrix[i][j] = min(self.matrix[i][k] + self.matrix[k][j],
                                                self.matrix[i][j])

    def input(self, i, j, value=inf):
        self.matrix[i][j] = value

    def print(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] == self.inf:
                    print("inf\t", end='')
                else:
                    print(self.matrix[i][j], "\t", end='')
            print()


while True:
    try:
        number_of_tests = int(input("Number of tests: "))
        if number_of_tests > 0:
            print(number_of_tests)
        else:
            raise ZeroDivisionError
        break
    except:
        print("Please, input correct number of cities!")

while True:
    try:
        number_of_cities = int(input("Number of cities: "))
        if 0 < number_of_cities <= 100000:
            print(number_of_cities)
        else:
            raise ZeroDivisionError
        break
    except:
        print("Please, input correct number of cities!")

matrix = Matrix(number_of_cities)
current_city_number = 0
city_names = [number_of_cities]
for test in range(number_of_tests):
    for i in range(number_of_cities):
        while True:
            try:
                name = input("City name: ")
                if len(city_names) < 10:
                    city_names.append(name)
                p = int(input("Number of neighbours in " + name + ": "))
                if p >= number_of_cities:
                    raise NameError
                break
            except:
                print("BAD INPUT!!!\n")
        for j in range(p):
            while True:
                try:
                    nr_cost = input("Number of city and cost: ").split(' ')
                    neighb_city_number = int(nr_cost[0]) - 1
                    transport_cost = int(nr_cost[1])
                    if (neighb_city_number == current_city_number
                            or neighb_city_number < 0
                            or transport_cost < 1):
                        raise ZeroDivisionError
                    matrix[current_city_number][neighb_city_number] = transport_cost
                    break
                except:
                    print("BAD INPUT!\n")
        current_city_number += 1

    matrix.floyd()

    while True:
        try:
            number_of_test_travels = int(input("Number of test travels: "))
            if number_of_test_travels > 0:
                print(number_of_test_travels)
            else:
                raise ZeroDivisionError
            break
        except:
            print("Please, input correct number of cities!")
    for i in range(number_of_test_travels):
        while True:
            cost_btw_cities = input("Input start and end cities of your travel: ").split(' ')
            try:
                start_city = int(city_names.index(cost_btw_cities[0])) - 1
                end_city = int(city_names.index(cost_btw_cities[1])) - 1
                break
            except:
                print("Input correct name of cities!")

        print(matrix[start_city][end_city])


"""
Task 3.
Find the sum of the digits in the number 100! (i.e. 100 factorial)


1 step - from math import factorial 
2 step - create a generic function to find the sum of the digits in the number
3 step - return result
    
"""


def sum_factorial(number):
    result = 0
    for digit in str(factorial(number)):
        result += int(digit)
    return result


print(sum_factorial(100))
