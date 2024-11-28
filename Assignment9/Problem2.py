'''
Name: Ziheng (Tony) Fang
CS 156
'''
import pandas
import math

trainData = pandas.read_csv("ExampleTrainDataset.csv") ## read in data

lambdaVal = 0.01 # learning rate

iterations = 50

## we were not given the original weights?
w1old = 0

w2old = 0

w3old = 0

## we are not given the actual and estimated outputs
y_actual = 0

y_hat = 0

def ActivationFunction(x):
    return pow(math.e, x) / (1 + pow(math.e, x))

def ActivationFunctionDeriv(x):
    return ActivationFunction(x) * (1 - ActivationFunction(x))

def main():
    for i in range(iterations):
        w1new = w1old - lambdaVal* 2(y_actual - y_hat) * ActivationFunctionDeriv(w1old)
        w2new = w2old - lambdaVal* 2(y_actual - y_hat) * ActivationFunctionDeriv(w2old)
        w3new = w3old - lambdaVal* 2(y_actual - y_hat) * ActivationFunctionDeriv(w3old)
