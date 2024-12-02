'''
Name: Ziheng (Tony) Fang
CS 156
'''
import pandas
import math
import matplotlib.pyplot

input_data = pandas.read_csv("ExampleTrainDataset.csv", usecols=["x1", "x2", "x3"]) #input data
target_values = pandas.read_csv("ExampleTrainDataset.csv", usecols=["Y"]) # #outputs
test_input_data = pandas.read_csv("ExampleTestDataset.csv", usecols=["x1", "x2", "x3"]) #input test data
test_target_values = pandas.read_csv("ExampleTestDataset.csv", usecols=["Y"]) # #expected outputs for test

lambdaVal = 0.01 # learning rate

iterations = 50

#weights
weights = []
for i in range(len(input_data)):
    weights.append(0)

batch_size = len(input_data) # get batch size

test_size = len(test_input_data) # number of tests

actual_outputs = []

losses = []

test_losses = []




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

    #Part 2b - Report test loss
    for i in range(test_size):
        actual_out = activationfunc(test_input_data.iloc[i, 0] * weights[0] + test_input_data.iloc[i, 1] * weights[1] + test_input_data.iloc[i, 2] * weights[2]) # compute actual output
        test_losses.append(abs(test_target_values.iloc[i, 0] - actual_out))
    for i in range(len(test_losses)):
        print("Test " + str(i + 1) + ": Loss: " + str(test_losses[i]))

main()
