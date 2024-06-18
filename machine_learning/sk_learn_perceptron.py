import numpy as np
import matplotlib.pyplot as plt
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.validation import check_X_y, check_is_fitted, check_random_state
from sklearn.utils.multiclass import unique_labels


params = {
    'figure.facecolor': '.0',
    'axes.facecolor'  : '.1',
    'axes.labelcolor' : 'white',
    'text.color'      : 'white',
    'xtick.color'     : 'green',
    'ytick.color'     : 'green',
    'axes.edgecolor'  : 'purple'
}
plt.rcParams.update(params)


class PerceptronEstimator(BaseEstimator, ClassifierMixin):
    def __init__(self, n_iterations=20, random_state=None):
        self.n_iterations = n_iterations
        self.random_state = random_state
        self.errors       = []

    heaviside = lambda self, x: 0 if x < 0 else 1    

    def fit(self, X=None, y=None):
        random_state  = check_random_state(self.random_state)
        self.w        = random_state.random_sample(np.size(X, 1))
        X, y          = check_X_y(X, y)
        self.classes_ = unique_labels(y)
        self.X_       = X
        self.y_       = y
        for i in range(self.n_iterations):
            rand_index = random_state.randint(0,np.size(X,0))
            x_ = X[rand_index]
            y_ = y[rand_index]
            y_hat = self.heaviside(np.dot(self.w, x_))
            error = y_ - y_hat
            self.errors.append(error)
            self.w += error * x_
        return self
    
    def predict(self, x):
        check_is_fitted(self, ['X_', 'y_'])
        y_hat = self.heaviside(np.dot(self.w,x))
        return y_hat
    
    def plot(self):                 
        fignr = 1
        plt.figure(fignr,figsize=(5,5))#,facecolor='.2')   
        plt.plot(self.errors,color='green')
        plt.style.use('dark_background')     
        plt.xlabel('Iteration')
        plt.ylabel(r"$(y - \hat y)$")
        plt.show()
        
def main():
    X = np.array([[1,0,0]
                 ,[1,0,1],
                  [1,1,0],
                  [1,1,1]])
    
    y = np.array([0,1,1,1])
    
    Perceptron = PerceptronEstimator(30,10)
    Perceptron.fit(X,y) 
    
    for index, x in enumerate(X):
        p = Perceptron.predict(x)
        print("{}: {} -> {}".format(x, y[index],p))
        
    Perceptron.plot()


main()    