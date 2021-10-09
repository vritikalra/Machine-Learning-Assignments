import numpy as np
import pandas as pd
import csv
import argparse

def activation_fn(y):
        y_predict = []
        for i in range(y.shape[0]):
            y_predict.append(1 if y[i] > 0 else 0)
        return y_predict


def Perceptron(y, x, weights_constant,weights_changing, lr,output_file):
    
    iteration = 100
    constant_errorcount = []
    changing_errorcount = []
        
    for k in range(iteration+1):
        result_constant = np.matmul(x,weights_constant)
        error_constant = y - np.asarray(activation_fn(result_constant))
        weights_constant += lr*np.matmul(np.transpose(x),error_constant)
        constant_errorcount.append(np.count_nonzero(error_constant))
        
        result_changing = np.matmul(x,weights_changing)
        error_changing = y - np.asarray(activation_fn(result_changing))
        weights_changing += (lr/(k+1))*np.matmul(np.transpose(x),error_changing)
        changing_errorcount.append(np.count_nonzero(error_changing))
    
    
    with open(output_file, 'w', newline='') as out_file:
            tsv_writer = csv.writer(out_file, delimiter='\t')
            tsv_writer.writerow(constant_errorcount)
            tsv_writer.writerow(changing_errorcount)
            
   


    
parser = argparse.ArgumentParser()    
parser.add_argument("--data", "-d", type=str, required=True)
parser.add_argument("--output", "-o", type=str, required=True)
args = parser.parse_args()
    
df = pd.read_csv(args.data, sep='\t', header=None)  
  
y = df.iloc[:,0]
y = y.replace('A',1).replace('B',0)
y=y.values
  

x = np.zeros((df.shape[0], df.shape[1]-1))
x[:,1:] = df[df.columns[1:3]]
x[:, 0] =  1


weights_constant = np.zeros(len(x.shape)+1) 
weights_changing = np.zeros(len(x.shape)+1)

lr = 1


Perceptron(y, x, weights_constant,weights_changing, lr,args.output)
