import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class Calculus:
    def __init__(self,L):
        #create_symfunc = lambda coeffs: sum(coeffs[i]*self.x**i for i in range(len(coeffs)))
        self.x = sp.symbols('x')
        self.sym_func = sum(L[i]*self.x**i for i in range(len(L)))
        self.sym_dfunc = sp.diff(self.sym_func, self.x)
        self.sym_ifunc = sp.integrate(self.sym_func, self.x)
        self.func = sp.lambdify(self.x, self.sym_func, 'numpy')
        self.dfunc = sp.lambdify(self.x, self.sym_dfunc, 'numpy')
        self.ifunc = sp.lambdify(self.x, self.sym_ifunc, 'numpy')
    
    def __repr__(self):
        return '{}'.format(self.sym_func)
        
    def show_func(self):
        return self.sym_func
    
    def calcx(self,v):
        return self.func(v)
    
    def value_table(self, start=-5, stop=5, step=1):
        d = pd.Series({round(k, 6): round(self.func(k), 7) for k in np.arange(start, stop, step)})
        return d  
    
    def value_table2(self, start=-5, stop=5, step=1):
        f = {round(k, 6): round(self.func(k), 7) for k in np.arange(start, stop, step)}
        d1 = {round(k, 6): round(self.dfunc(k), 7) for k in np.arange(start, stop, step)}
        i = {round(k, 6): round(self.ifunc(k), 7) for k in np.arange(start, stop, step)}
        df = pd.DataFrame({'{}'.format(self.sym_ifunc): i,'{}'.format(self.sym_func): f, '{}'.format(self.sym_dfunc): d1})
        return df
    
    def integrate(self,transform=False):
        if transform:
            self.a = sp.Poly(sp.integrate(self.sym_func, self.x)).coeffs()
            self.a.append(0)
            return Calculus(self.a[::-1])
        else:
            return sp.integrate(self.sym_func, self.x)
        
    def derivative(self,transform=False):
        if transform:
            self.a = sp.Poly(sp.diff(self.sym_func, self.x)).coeffs()
            return Calculus(self.a[::-1])
        else:
            return sp.diff(self.sym_func, self.x)
    
    def show_curve(self, coords=[-1, 1, -1, 4],size=(3,2)): 
        xticks = list(range(coords[0]-1,coords[1]+1, 1))
        yticks = list(range(coords[2]-1,coords[3]+1, 1))
        y_ticks = len(xticks)
        x_ticks = len(yticks)
        x_ = np.linspace(coords[0], coords[1], 100)
        plt.figure(facecolor='0.3',figsize=size)
        plt.axes().set_facecolor('grey')
        plt.axis([coords[0],coords[1],coords[2],coords[3]])
        plt.plot(x_, self.func(x_),color='black')
        plt.axhline(y=0, color='k', lw=0.5,zorder=2)
        plt.axvline(x=0, color='k', lw=0.5,zorder=2)
        plt.scatter(xticks,np.zeros(y_ticks),color = 'black',zorder=2,marker='.', s=4)
        #plt.scatter(np.zeros(x_ticks), yticks,color = 'black',zorder=2,marker='.', s=4)
        plt.grid()
        plt.show()            
                
def polypown(co):
    create_polynomial = lambda coeffs: sum(coeffs[i]*x**i for i in range(len(coeffs)))
    x = sp.symbols('x')
    F = create_polynomial(co)
    f = sp.diff(F, x)
    df = sp.diff(sp.diff(F, x), x)
    F1 = sp.lambdify(x, F, 'numpy')
    f1 = sp.lambdify(x, f, 'numpy')
    df1 = sp.lambdify(x, df, 'numpy')
    x_ = np.linspace(-10, 10, 100)

    fig, axs = plt.subplots(1, 3, facecolor='0.2',figsize=(12, 4))
    
    axs[0].plot(x_, F1(x_), c = 'green')
    if len(co) == 3:
        axs[2].axhline(y=2*co[2],c='green')
        axs[1].plot(x_, f1(x_), c = 'green')
    elif len(co) == 2:
        axs[1].axhline(y=co[1],c='green')
    else:
        axs[1].plot(x_, f1(x_), c = 'green')
        axs[2].plot(x_, df1(x_),c ='green')
    axs[0].set_title("F(x) = {}".format(F), fontsize=9)
    axs[1].set_title("f(x) = {}".format(f), fontsize=9)
    axs[2].set_title("df1(x) = {}".format(df), fontsize=9)

    for n in range(3):
        axs[n].set_facecolor('black')
        axs[n].axhline(y=0, c='white', lw=0.1,zorder=0)
        axs[n].axvline(x=0, c='white', lw=0.1,zorder=0)
    plt.show()

def more_plot(L, shape, s=(10,8), sh=False):
    fig, axs = plt.subplots(shape[0], shape[1], facecolor='0.3',figsize=s, sharey=sh)
    for idx, val in enumerate(L):
        i = idx // shape[1]
        j = idx % shape[1]
        axs[i,j].set_facecolor('black')
        axs[i,j].plot(*L[idx], color='green')
        axs[i,j].grid(alpha=.3)
    plt.show()

def create_poly(L):
    instance = Calculus(L)
    return instance

def interval2(f, a, b):
    return (list(range(a, b)), [f(i) for i in range(a,b)])

interval = lambda f, a, b: (list(range(a, b)), [f(i) for i in range(a, b)])