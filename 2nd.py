import matplotlib.pyplot as plt
import numpy as np


def plot_polygon(polygon,title):
    plt.figure()
    plt.title(title)
    plt.gca().set_aspect('equal',adjustable='box')
    plt.grid(True)
    
    polygon = np.concatenate(polygon,[polygon[0]])
    plt.plot(polygon[:,0],polygon[:,-1],'b-')
    
    plt.plot(polygon[:-1,0],polygon[-1,1],'bo')
    for i,(x,y) in enumerate(polygon[:-1]):
        plt.text(x,y,f"P{i}",ha='right')
    plt.show()
    
def translate_polygon(polygon):
    tx = float(input("Enter translation along x-axis:"))
    ty = float(input("Enter translation along y-axis:"))
    translated_polygon = polygon + np.array([tx,ty])
    return translated_polygon

