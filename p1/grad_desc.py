#program for batch linear regression using gradient descent
'''
import csv

with open('random.csv') as csv_file:
    csv_reader= csv.reader(csv_file,delimiter=',')
    data=[]
    
    for row in csv_reader:
        data.append(row)
x=len(data[0])        
vari=[]
vari.append(data[0][0])
print(data[1][1])
        
'''



#code for taking any csv file and spliting dependent and independent variables 
with open('random.csv') as csv_file:
    input_var=[]
    output_var=[]
    for row in csv_file:
        
        row_temp=row.split(',')
        input_var.append(row_temp[:-1])
        output_var.append(row_temp[-1])

#create a weight array with same shape and initialize it with zeros

weights=[]
weights=input_var
len_input_var=len(input_var[0])
end=0
value=0
row=0
column=0
y_pred=0
gradient=0
lr

#initialize variables
x0=1


while len_input_var>end:
    
    y_actual=output_var[row][column]
    

    y_pred=y_pred+x0*w0
    error=y_actual-y_pred
    error=error*x0
    gradient=gradient+error
    while column<len_input_var:
        
        if(row==0): #for initial values 
            weight[row][column]=0
            y_pred=ypred+input_var[row][column]*weight[row][column]
            error=y_actual-y_pred
            error=error*input_var[row][column]
            gradient=gradient+error
            column+=1
        else:
            y_pred=ypred+input_var[row][column]*weight[row-1][column]
            error=y_actual-y_pred
            error=error*input_var[row][column]
            gradient=gradient+error
            column+=1
            
        #update weights
        
        w0=w0+lr*gradient
        column=0
        
        while column<len_input_var:
            
            weight[row][column]= weight[row][column] + lr*gradient
            
            
        x='1'
        y=x
        y=int(x)
    
            
            
        
    
    
        
    
    

#code for splitting each individual variable into arrays and also assigning weights to it
'''        
len_input_var=len(input_var[0])
value=0
x=[]
while value <= len_input_var:
    x[''.format(value)]= []##input_var[value]
    value+=1
'''
while value <=len_input_var:
    weights[]append(input_var)
    

#create a weight array of same dimension as of input variables

        
def gradient_desc:
    
    
    
    



        

        


    