import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

def create_chart(labels, sizes):
    fig, axs = plt.subplots(1, 3, figsize=(18, 5))

    axs[0].pie(sizes, labels=labels, autopct='%1.1f%%')
    axs[0].set_title('Pie Chart')
    axs[0].axis('equal')

    bar_positions = np.arange(len(labels))
    bars = axs[1].bar(bar_positions, sizes, align='center')
    axs[1].set_xticks(bar_positions)
    axs[1].set_xticklabels(labels)
    axs[1].set_title('Bar Chart')

    ax = fig.add_subplot(133, projection='3d')
    x = np.linspace(0, len(labels), len(labels))
    y = np.zeros(len(labels))
    z = np.zeros(len(labels))

    def update_graph(num):
        ax.clear()
        ax.bar3d(x, y, z, 0.5, 0.5, sizes)
        ax.set_title('3D Bar Chart')

    ani = animation.FuncAnimation(fig, update_graph, frames=range(100), interval=200, blit=False)

    plt.show()

dataset = pd.read_csv('data25.csv', delimiter=';')

labels = dataset['Label'].tolist()
sizes = dataset['Size'].tolist()

create_chart(labels, sizes)
