import matplotlib.pyplot as plt
import numpy as np
import statistics
import scipy.stats

def boxplot(data):
    '''Input data has to be a list of positive numbers'''
    
    print(scipy.stats.describe(data))
    
    mean = statistics.fmean(data)
    hmean = statistics.harmonic_mean(data)
    gmean = statistics.geometric_mean(data)
    median = statistics.median(data)
    
    plt.figure(facecolor='0.6',figsize=(10,1.1),dpi=300)
    plt.axes().set_facecolor('0.4')
    plt.axis([min(data)-2,max(data)+2,-0.5,0.5])

    plt.scatter(data,np.zeros(len(data)),color = 'black',zorder=2)
    plt.axvline(x = gmean,color='red', linestyle='--',label='gmean')
    plt.axvline(x = hmean,color='blue', linestyle='--',zorder=1,label='hmean')
    plt.axvline(x = mean,color='purple', linestyle='--',label='armean')
    plt.axvline(x = median,color='yellow', linestyle='--',label='median')
    
    plt.yticks(np.arange(0))
    plt.legend(loc='lower right',prop={'size': 3})
    plt.legend().get_frame().set_alpha(0.1)
    plt.grid()
    plt.show()

def boxplot2(data,prop,p=0):

    plt.figure(facecolor='0.6',figsize=(10,1.1),dpi=300)
    plt.axes().set_facecolor('0.4')
    plt.axis([min(data)-2,max(data)+2,-0.5,0.5])
    plt.scatter(data,np.zeros(len(data)),color = 'black',zorder=2)   
    
    
    if prop == 'gmean':
        gmean = statistics.geometric_mean(data)
        plt.axvline(x = gmean,color='red', linestyle='--',label='gmean')
    elif prop == 'hmean':
        hmean = statistics.harmonic_mean(data)
        plt.axvline(x = hmean,color='blue', linestyle='--',zorder=1,label='hmean')
    elif prop == 'median':
        median = statistics.median(data)
        plt.axvline(x = median,color='yellow', linestyle='--',label='median')
    elif prop == 'mean':
        mean = statistics.fmean(data)
        plt.axvline(x = mean,color='purple', linestyle='--',label='armean')
    elif prop == 'quantil':
        L = statistics.quantiles(data,n=p)
        plt.axhline(y=20,label='quantiles',color='red', linestyle='--')
        for i in range(p-1):
            plt.axvline(x = L[i],color='red', linestyle='--',zorder=0)

    
    plt.yticks(np.arange(0))
    plt.legend(loc='lower right',prop={'size': 3})
    plt.legend().get_frame().set_alpha(0.1)
    plt.grid()
    plt.show()
    
    
def _scatter2d(data, x_d, y_d, n_clusters, _min=-2, _max=2, colors=None):
    plt.rcParams['figure.facecolor'] = '0.2'
    plt.axes().set_facecolor('black')
    x = data[:, x_d]
    y = data[:, y_d]
    
    if colors is None:
        colors = ['green'] * n_clusters
    
    for i in range(n_clusters):
        idx = data[:, -1] == i
        plt.scatter(x[idx], y[idx], c=colors[i])

    plt.xlabel(f"d{x_d}")
    plt.ylabel(f"d{y_d}")
    #plt.xlim(data[:, y_d].min()+_min, data[:, y_d].max()+_max)
    #plt.ylim(data[:, x_d].min()+_min, data[:, x_d].max()+_max)
    plt.show()
    
    
def _scatter3d(data, x_d, y_d, z_d, n_clusters, _min=-.2, _max=.2, colors=None):
    fig = plt.figure()
    fig.patch.set_facecolor('0.2')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('0.2')
    x = data[:, x_d]
    y = data[:, y_d]
    z = data[:, z_d]
    
    if colors is None:
        colors = ['green'] * n_clusters
    
    for i in range(n_clusters):
        idx = data[:, -1] == i
        ax.scatter(x[idx], y[idx], z[idx], c=colors[i])
        
    ax.set_xlabel(f"d{x_d}")
    ax.set_ylabel(f"d{y_d}")
    ax.set_zlabel(f"d{z_d}")
    #ax.set_xlim(data[:, x_d].min()+_min, data[:, x_d].max()+_max)
    #ax.set_ylim(data[:, y_d].min()+_min, data[:, y_d].max()+_max)
    #ax.set_zlim(data[:, z_d].min()+_min, data[:, z_d].max()+_max)
    plt.show()
    
    
    
def more_plot(pics, shape, c='gray', s=(8,8), sh=False):
    fig, axs = plt.subplots(shape[0], shape[1], facecolor='0.2',figsize=s, sharey=sh)
    for idx, val in enumerate(pics):
        i = idx // shape[1]
        j = idx % shape[1]
        axs[i,j].imshow(pics[idx], cmap=c)
    plt.show()
    
    
def nplot(pics ,c='gray', s=(10,8),sh=False):
    fig, axs = plt.subplots(1, len(pics), facecolor='0.2', figsize=s, sharey=sh)
    for i in range(len(pics)):
        axs[i].imshow(pics[i], cmap=c)
    plt.show()
    
    
    
def discreteImage(M):
    max_ = np.max(M)
    min_ = np.min(M)
    cmap = plt.get_cmap('jet', max_ - min_ + 1)
    plt.matshow(M, cmap=cmap, vmin = min_ - 0.5, vmax = max_ + 0.5)
    plt.colorbar(ticks=np.arange(min_, max_ + 1))
    
def scatter2d(data, x_d, y_d, _min=-1, _max=1, grid=False, alpha=.2):
    plt.rcParams['figure.facecolor'] = '0.2'
    plt.axes().set_facecolor('black')
    x = data[:, x_d]
    y = data[:, y_d]
    plt.scatter(x, y, c='green')
    plt.xlabel(f"d{x_d}")
    plt.ylabel(f"d{y_d}")
    #plt.xlim(data[:, y_d].min()+_min, data[:, y_d].max()+_max)
    #plt.ylim(data[:, x_d].min()+_min, data[:, x_d].max()+_max)
    plt.grid(grid, alpha=alpha)
    plt.show()

def scatter3d(data, x_dim, y_dim, z_dim, _min=-1, _max=1):
    x = data[:, x_dim]
    y = data[:, y_dim]
    z = data[:, z_dim]
    fig = plt.figure()
    fig.patch.set_facecolor('0.2')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('0.2')
    ax.scatter(x, y, z, c='black')
    ax.set_xlabel(f"d{x_dim}")
    ax.set_ylabel(f"d{y_dim}")
    ax.set_zlabel(f"d{z_dim}")
    ax.set_xlim(data[:, x_dim].min()+_min, data[:, x_dim].max()+_max)
    ax.set_ylim(data[:, x_dim].min()+_min, data[:, x_dim].max()+_max)
    ax.set_zlim(data[:, x_dim].min()+_min, data[:, x_dim].max()+_max)    
    plt.show()