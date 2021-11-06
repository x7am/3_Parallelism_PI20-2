from multiprocessing import Process, Pool
from json import load
import numpy as np
import csv

def element(args):
    index, A, B = args[0], args[1], args[2]
    i, j = index; res = 0
    N = A.shape[1] or B.shape[0]
    for k in range(N):
        res += A[i, k] * B[k, j]
    return res

def check_matrix(matrix1, matrix2):
    print('matrix can exist') if matrix1.shape[1]==matrix2.shape[0] else print('matrix cant exist')
    
def generate_map(mt1, mt2):
    args = []
    for i in range(mt1.shape[0]):
        for j in range(mt2.shape[1]):
            args.append(((i, j), mt1, mt2))
    print(args)


if __name__ == "__main__":
    with open('matrix1.json','r') as f:
        matrix1 = np.matrix(load(f))

    with open('matrix2.json','r') as f:
        matrix2 = np.matrix(load(f))

    p = Pool(matrix1.shape[0] * matrix2.shape[1])

    if check_matrix(matrix1, matrix2):
        args = generate_map(matrix1, matrix2)
        result = np.array(p.map(element, args))
        matrix = result.reshape(matrix1.shape[0], matrix2.shape[1])
      
        filename = input('filename')
        file = open(filename, 'w')
        for line in matrix:
            for elem in line:
                file.write(f'{elem}\t')
            file.write('\n')
         file.close()
       
    else:
        file = open('result.txt', 'w')
        file.close()
