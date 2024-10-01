import numpy as np
from scipy.special import expit  # Sigmoid function

def pairwise_distances(X):
    #Compute pairwise Euclidean distances between points in X.
    sum_X = np.sum(np.square(X), axis=1)
    distances = np.sqrt(
        -2 * np.dot(X, X.T) + sum_X[:, np.newaxis] + sum_X[np.newaxis, :]
    )
    return distances

def compute_high_dimensional_affinities(X, perplexity=30.0):
   
    #Compute the pairwise affinities in high-dimensional space using a Gaussian kernel.
    distances = pairwise_distances(X)
    n = X.shape[0]
    affinities = np.zeros((n, n))
    for i in range(n):
        # Compute conditional probabilities p_{j|i}
        sigma_i = 1.0  # Initial guess for sigma
        # Binary search for sigma
        for _ in range(50):
            # Compute the Gaussian distribution
            exp_dist = np.exp(-distances[i] ** 2 / (2 * sigma_i ** 2))
            p = exp_dist / np.sum(exp_dist)
            # Compute the entropy of the distribution
            H = -np.sum(p * np.log2(p + 1e-10))
            # Compute the difference between the desired and actual entropy
            H_diff = H - np.log2(perplexity)
            if np.abs(H_diff) < 1e-5:
                break
            # Update sigma using a simple gradient descent approach
            sigma_i *= 2.0 ** (H_diff / 1.0)
        affinities[i] = p
    return (affinities + affinities.T) / (2 * X.shape[0])

def compute_low_dimensional_affinities(Y):
    """
    Compute the pairwise affinities in low-dimensional space using a Student's t-distribution.
    """
    distances = pairwise_distances(Y)
    return 1.0 / (1.0 + distances ** 2)

def t_sne(X, n_components=2, perplexity=30.0, n_iter=1000, learning_rate=200.0):
    """
    Perform t-SNE dimensionality reduction.
    """
    n = X.shape[0]
    Y = np.random.randn(n, n_components)
    
    P = compute_high_dimensional_affinities(X, perplexity)
    P = P / np.sum(P)
    
    for _ in range(n_iter):
        Q = compute_low_dimensional_affinities(Y)
        Q = Q / np.sum(Q)
        Q = np.maximum(Q, 1e-10)  # Avoid division by zero
        
        # Compute gradients
        grad = np.dot((P - Q), Y)
        Y -= learning_rate * grad
        
        # Optionally, print out the cost
        cost = np.sum(P * np.log(P / Q))
        print(f"Iteration {_ + 1}, Cost: {cost}")
    
    return Y

# Example usage
if __name__ == "__main__":
    from sklearn.datasets import load_iris
    import matplotlib.pyplot as plt

    # Load dataset
    data = load_iris()
    X = data.data

    # Perform t-SNE
    Y = t_sne(X, n_components=2, perplexity=30.0)

    # Plot results
    plt.scatter(Y[:, 0], Y[:, 1], c=data.target, cmap='viridis')
    plt.colorbar()
    plt.title("t-SNE Visualization")
    plt.show()