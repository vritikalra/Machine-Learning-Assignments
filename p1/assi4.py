import numpy as np


A = [[1,1,1], [9,3,1],[16,4,1],[49,7,1],[81,9,1]]
y = [[1],[6],[1],[8],[20]]

B = np.linalg.pinv(A)

final = np.matmul(B, y)

counter=0
stop=5
pred_y=[]
error=[]
while counter < stop:
    x0=A[counter]
    x0=x0[0]
    x1=A[counter]
    x1=x1[1]
    pred_y.append(final[0,0]*x0 + final[1,0]*x1 + final[2,0])
    
    fin_y=y[counter]
    fin_y=fin_y[0]
    
    error.append((fin_y-pred_y[counter])*(fin_y-pred_y[counter]))
    
    
    counter+=1

MSE = np.mean(error)





#least square error[3.343161284121494, 6.775302768166097, 20.338331410995753, 14.807405805459409, 15.41717128027684]








