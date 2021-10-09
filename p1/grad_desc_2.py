#code for taking any csv file and spliting dependent and independent variables 
import csv
 
#Take value of threshold and learning rate from user

thr = input("Enter threshold: ")
thr = float(thr)
lr = input("Enter learning rate: ")
lr = float(lr)

#take csv file from local directory(or any directory , just give the full location!)

with open('random.csv') as csv_file:
    
    input_var=[]
    output_var=[]
    row_temp=[]
    count=0
    for row in csv_file:
        row_temp = (row.split(','))
        row_num_temp=[]
    
        x=0
        while x<len(row_temp):
            
            row_num_temp.append(float(row_temp[x]))
            x+=1
        
        input_var.append(row_num_temp[:-1])
        input_var[count].append(1)
        count+=1
        output_var.append(row_num_temp[-1])


weights=[]  #initialize weight required
weights_temp=[]
len_input_var=len(input_var[0]) #fill initial weights and keep a shape 
i=j=0

while i<len(input_var):
    
    while j<len_input_var:
        weights_temp.append(0)
        j+=1
    weights.append(weights_temp)
    i+=1
    

    
    
mean_squared_e_sum=[]
mean_squared_e_sum.append(0)
weight_saver=[]
add_weight_saver=[]
itr_counter=0

#initialize high value for threshold(temp solution)
mean_sq_e=float(999999999)

while mean_sq_e > thr:
    
    
    
#target_fuction_formula

#some loop which can take all values in a row ie x1w1, x2w2, x0w0
    y_pred=[]
    mean_squared_e=[]
    mean_e=[]


    row=0
    
    while row < len(input_var):
        col=0
        y_pred_temp=0
        while col < len(input_var[0]):
            y_pred_temp=y_pred_temp+input_var[row][col]*weights[row][col]
            col+=1
    
        y_pred.append(y_pred_temp)
        row+=1

#some loop which will take any_var=0 upto len of the rows 

    counting_var=0

    while counting_var < len(y_pred):
    
        mean_e.append((output_var[counting_var]-y_pred[counting_var]))
        mean_squared_e.append(mean_e[counting_var]*mean_e[counting_var])
    
        counting_var+=1
    
# for taking mean squared error
        
    mean_sq_e = sum(mean_squared_e)
    mean_squared_e_sum.append(sum(mean_squared_e))




#initialize gradient formula
    gradients = [] 
    row=0

    counting_var=0

    while row < len(input_var):
        col=0
        grad_temp=[]
        while col < len(input_var[0]):

            grad_temp.append (input_var[row][col] * mean_e[counting_var])
            col+=1
        gradients.append(grad_temp)
        counting_var+=1
        row+=1


#update weights

    row=0
    weights_u=[]
    
    if itr_counter == 0:
        pass
        
    else: 
        
        weights=weight_saver

    while row < len(gradients):
    
        col=0
        weights_temp=[]
        while col < len(gradients[0]):

            weights_temp.append(weights[row][col] + lr * gradients[row][col])
            col+=1
    
        weights_u.append(weights_temp)    
        row+=1
        



    



#list sum of weights
    
    sum_of_weights = []
    col = 0
    temp_sum = []
    
    while col < len(weights_u[0]):
    
        row = 0
        temp_sum_2=0
        
        while row< len(weights_u):
        
            temp_sum_2 = temp_sum_2 + weights_u[row][col]
            row+=1
    
        temp_sum.append( temp_sum_2)
        col+=1
   
    sum_of_weights.append(temp_sum)
    
    #take all values required for csv file and put in some single 2d list and save
    #to save
    temp_row=[]
    if itr_counter == 0:
        pass
    else:
        
        weights=add_weight_saver
    row=0
    temp_row.append(itr_counter)
    for x in weights[row]:
        temp_row.append(x)
    temp_row.append(mean_sq_e )
   
    
    with open('random_answer.csv','a',newline='') as csv_file: 
        csv_writer=csv.writer(csv_file,delimiter=',')
        csv_writer.writerow(temp_row)
    csv_file.close()
   
    '''we need to set weights array with summed weights to calculate                ypred(target_function)'''
  
    weights=[]  #initialize weight required
    weights_temp=[]
    len_input_var=len(input_var[0]) #fill initial weights and keep a shape 
    counter=0
    row=0

    #weights=weights_u
    
    
    while counter<len(input_var):
        col=0
        weights_temp=[]
    
        while col< len (input_var[0]):
            weights_temp.append((sum_of_weights[row][col]))
            col+=1
        weights.append(weights_temp)
        counter+=1
    
    weight_saver=[]
    weight_saver=weights_u
    add_weight_saver=[]
    add_weight_saver=weights
    
    itr_counter+=1
   
    thresher=mean_squared_e_sum[itr_counter-1] - mean_squared_e_sum[itr_counter]
    if thresher < 0: 
        thresher=thresher*-1
    else:
        pass
    
    if  thresher<= thr: 
        break
    else:
        pass
     
    
    























