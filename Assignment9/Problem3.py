'''
Name: Ziheng (Tony) Fang
CS 156
**Note that this is generated using ChatGPT as allowed per instructions on assignment.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("ExampleTrainDataset.csv")

# Extract input features (X) and target (Y)
X = data[['x1', 'x2', 'x3']].values
Y = data['Y'].values

# Normalize the features for stability
X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)

# Define sigmoid activation function and its derivative
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def sigmoid_derivative(z):
    return sigmoid(z) * (1 - sigmoid(z))

# Initialize network parameters
input_size = X.shape[1]  # Number of input features
hidden_size = 4          # Number of neurons in hidden layer
output_size = 1          # Number of output neurons
learning_rate = 0.01     # Learning rate
iterations = 50          # Number of training iterations

# Weight initialization
np.random.seed(42)
W1 = np.random.randn(input_size, hidden_size) * 0.01
b1 = np.zeros((1, hidden_size))
W2 = np.random.randn(hidden_size, output_size) * 0.01
b2 = np.zeros((1, output_size))

# Training process
losses = []

for i in range(iterations):
    # Forward pass
    Z1 = np.dot(X, W1) + b1
    A1 = sigmoid(Z1)
    Z2 = np.dot(A1, W2) + b2
    A2 = sigmoid(Z2)

    # Compute loss (mean squared error)
    loss = np.mean((A2 - Y.reshape(-1, 1)) ** 2)
    losses.append(loss)

    # Backward pass
    dZ2 = A2 - Y.reshape(-1, 1)
    dW2 = np.dot(A1.T, dZ2) / X.shape[0]
    db2 = np.sum(dZ2, axis=0, keepdims=True) / X.shape[0]
    dA1 = np.dot(dZ2, W2.T)
    dZ1 = dA1 * sigmoid_derivative(Z1)
    dW1 = np.dot(X.T, dZ1) / X.shape[0]
    db1 = np.sum(dZ1, axis=0, keepdims=True) / X.shape[0]

    # Update weights and biases
    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2
    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1

# Plot training loss over iterations
plt.figure(figsize=(8, 6))
plt.plot(range(iterations), losses, marker='o', label='Training Loss')
plt.title('Training Loss over Iterations')
plt.xlabel('Iterations')
plt.ylabel('Loss')
plt.grid()
plt.legend()
plt.show()

# Print final weight vectors
print("Final Weights and Biases:")
print("W1 (Input to Hidden Layer):", W1)
print("b1 (Hidden Layer Bias):", b1)
print("W2 (Hidden to Output Layer):", W2)
print("b2 (Output Layer Bias):", b2)
