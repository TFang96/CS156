'''
Name: Ziheng (Tony) Fang
CS 156
'''
import pandas
import math

input_data = pandas.read_csv("ExampleTrainDataset.csv", usecols=["x1", "x2", "x3"]) #input data
target_values = pandas.read_csv("ExampleTrainDataset.csv", usecols=["y"]) #outputs

lambdaVal = 0.01 # learning rate

iterations = 50

#weights
weights = []
for i in range(len(input_data)):
    weights.append(0)

batch_size = len(input_data) # get batch size

actual_outputs = []

losses = []




def activationfunc(x):
    return pow(math.e, x) / (1 + pow(math.e, x))

def activationfuncderiv(x):
    return activationfunc(x) * (1 - activationfunc(x))

def calculate_losses(y_hat):
    sum = 0
    for i in range(len(y_hat)):
        sum += (target_values.iloc[i, 0] - y_hat[i]) ** 2
    return sum

def main():
    for i in range(iterations):
        linear_output = 0
        for j in range(batch_size):
            linear_output += input_data[j, 0] * weights[0] + input_data[j, 1] * weights[1] + input_data[j, 2] * weights[2] #linear output of each batch
            y_hat = activationfunc(linear_output)
            actual_outputs.append(y_hat) # this contains all the y_hat
            losses.append(calculate_losses(y_hat))

            #update weights using gradients
            weights[0] -= lambdaVal * (-2*(target_values.iloc[j, 0] - y_hat) * activationfuncderiv(linear_output) * input_data.iloc[j, 0])
            weights[1] -= lambdaVal * (-2*(target_values.iloc[j, 0] - y_hat) * activationfuncderiv(linear_output) * input_data.iloc[j, 1])
            weights[2] -= lambdaVal * (-2*(target_values.iloc[j, 0] - y_hat) * activationfuncderiv(linear_output) * input_data.iloc[j, 2])
