'''
Name: Ziheng (Tony) Fang
CS 156
'''
import pandas
import math
import matplotlib.pyplot

input_data = pandas.read_csv("ExampleTrainDataset.csv", usecols=["x1", "x2", "x3"]) #input data
target_values = pandas.read_csv("ExampleTrainDataset.csv", usecols=["Y"]) # #outputs

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

def calculate_losses(row, y_hat):
    return (target_values.iloc[row, 0] - y_hat) ** 2

def main():
    for i in range(iterations):
        loss_iteration = 0
        for j in range(batch_size):
            linear_output = input_data.iloc[j, 0] * weights[0] + input_data.iloc[j, 1] * weights[1] + input_data.iloc[j, 2] * weights[2] #linear output of each batch
            y_hat = activationfunc(linear_output)
            actual_outputs.append(y_hat) # this contains all the y_hat
            loss_iteration += calculate_losses(j, y_hat)

            #update weights using gradients
            weights[0] -= lambdaVal * (-2*(target_values.iloc[j, 0] - y_hat) * activationfuncderiv(linear_output) * input_data.iloc[j, 0])
            weights[1] -= lambdaVal * (-2*(target_values.iloc[j, 0] - y_hat) * activationfuncderiv(linear_output) * input_data.iloc[j, 1])
            weights[2] -= lambdaVal * (-2*(target_values.iloc[j, 0] - y_hat) * activationfuncderiv(linear_output) * input_data.iloc[j, 2])
        losses.append(loss_iteration)
    for i in range(len(losses)):
        print("Iteration: " + str(i+1) + " Loss: " + str(losses[i]))
    '''
    Graph Loss Data
    '''
    matplotlib.pyplot.title("Losses vs. Iterations")
    matplotlib.pyplot.xlabel("Iterations")
    matplotlib.pyplot.ylabel("Loss Amount")
    matplotlib.pyplot.plot(range(1, iterations + 1), losses, marker="*")
    matplotlib.pyplot.show()

main()
