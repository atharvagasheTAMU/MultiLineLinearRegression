import pickle
import numpy as np
from itertools import accumulate
from collections import defaultdict
import warnings
warnings.filterwarnings("ignore")

def solution():

    try:
        file_path = input('Please Enter File of the type of instances. \n')
        file = open(file_path, 'rb')
        example = pickle.load(file)
    except:
        print("Invalid File Path")
        return
    
    def multiLineFit(index):
        
        x_list_array = np.array(example['x_list'][index])
        preSumX = [0] + list(accumulate(x_list_array))

        y_list_array = np.array(example['y_list'][index])
        preSumY = [0] + list(accumulate(y_list_array))        

        productXY = x_list_array * y_list_array
        preSumXY = [0] + list(accumulate(productXY))
        
        sumX2 = np.square(x_list_array)
        preSumX2 = [0] + list(accumulate(sumX2))
        

        n = example['n_list'][index]

        C = example['C_list'][index]

        cost_matrix = [[-1] * n for i in range(n)]

        def computeE(i,j):
            if cost_matrix[i][j] != -1:
                return cost_matrix[i][j]
            i, j = i+1, j+1 
            n = j-i+1
            a = float(((n * (preSumXY[j]-preSumXY[i-1])) - ((preSumX[j]-preSumX[i-1]) * (preSumY[j]-preSumY[i-1]))) / ((n * (preSumX2[j] - preSumX2[i-1])) - np.square(preSumX[j]-preSumX[i-1])))
            b = float(((preSumY[j]-preSumY[i-1]) - (a * (preSumX[j]-preSumX[i-1]))) / n)
            cost_matrix[i-1][j-1] = float(np.sum(np.square(y_list_array[i-1 : j] - (a * x_list_array[i-1 : j]) - b))) + C
            return cost_matrix[i-1][j-1]

        cuts =[[] for i in range(n)]
        costs = [0 for i in range(n)]
        for j in range(0,n):
            opt_cost, opt_cut = computeE(0,j), -1
            for i in range(1,j):
                cost = costs[i-1] + computeE(i,j)
                if cost < opt_cost:
                    opt_cost, opt_cut = cost, i-1
            costs[j] = opt_cost
            if opt_cut != -1:
                cuts[j] = cuts[opt_cut] + [opt_cut]

        cuts[n-1].append(n-1)
        return len(cuts[n-1]),cuts[n-1],costs[n-1]

    res=defaultdict(list)
    for i in range(len(example['x_list'])):
        optimal_num_lines, breakpoints, total_cost = multiLineFit(i)
        res['k_list'].append(optimal_num_lines)
        res['last_points_list'].append(breakpoints)
        res['OPT_list'].append(total_cost)

    res = dict(res)
    file_path = file_path + '_solutions'
    with open(file_path, 'wb') as fp:
        pickle.dump(res, fp)
        print('Dictionary saved to ' + file_path +' file successfully')

print('Welcome to the solution of Multi Line Fitting Problem.')
while True:
    choice = input('\nPress 1 to continue, 0 to exit.\n')
    if choice == '0':
        break
    elif choice == '1':
        res = solution()
    else:
        print ('Invalid Input')

